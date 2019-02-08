MYfile=open("ajre.txt","r")
i=1
n=int(input('Enter a number:'))
L=readline()
MYfile.close()
MYfile=open("ajre.txt","a")
while i<=n:
    MYfile.write(L[i])
    MYfile.write("\n")
MYfile.close()