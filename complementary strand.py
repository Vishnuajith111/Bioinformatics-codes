Dnaseq=input("Enter the Dnaseq \n")
Dnaseq=Dnaseq.upper()
compDNA=""
for x in Dnaseq:
    if x=="T":
         compDNA=compDNA+"A"
    if x=="A":
         compDNA=compDNA+"T"
    if x=="G":
         compDNA=compDNA+"C"
    if x=="C":
         compDNA=compDNA+"G"
    if x==("A","T","G","C"):
        print("Error in input,use only A,T,G,C")
print(compDNA)
