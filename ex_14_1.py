import sqlite3
import re

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')
#CREATE TABLE Counts (email TEXT, count INTEGER, org varchar)''')

fname = 'mbox.txt'
#if (len(fname) < 1): fname = 'mbox-short.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
#    print(pieces)
    email = pieces[1]
    print(type(email))
    lorg = re.findall('@\S*', email)
    sorg=lorg[0]
    org = sorg[1:]
    org=org.strip()
    print(org)
    print(type(org))
    cur.execute('SELECT count FROM Counts WHERE org = ? ',(org,))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count)
                VALUES (?, 1)''', (org,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ? ',
                    (org,))
#    conn.commit()

# https://www.sqlite.org/lang_select.html
conn.commit()
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()
