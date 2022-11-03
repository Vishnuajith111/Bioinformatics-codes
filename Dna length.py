aminoacid=input("Enter the DNA seq \n\t")
aminoacid=aminoacid.upper()
totalamino=len(aminoacid)
A=G=C=T=total=0
for n in aminoacid:
    if n=='A':
        A+=1
    elif n=='T':
        T+=1
    elif n=='G':
        G+=1
    elif n=='C': 
        C+=1
    total+=1
print("A=",A)
print("T=",T)
print("G=",G)
print("C=",C)
print("length of DNA sequence",totalamino)
