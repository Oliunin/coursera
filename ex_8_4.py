fname = input("Enter file name: ")
fh=open(fname)
flist=list()
flist.append('Arise')
#print(flist)
for line in fh:
    lline=line.split()
    for word in lline:
        if word not in flist:
            flist.append(word)

print(flist)
flist.sort()
print(flist)
#        print(lline)
#        if word
#    flist.extend(line.split())
#    print(flist)
#    flist.append(line.split())
#print(flist)
