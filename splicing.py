f=open("dna_seq_mp.txt","r")
Dnaseq=f.read()
Dnaseq=Dnaseq.upper()
exons=[1,10,15,21,35,40]
start=0
end=1
Dnaseqexon=""
while(end<len(exons)):
     print("\n",exons[start],"\t",exons[end])
     print(Dnaseqexon[exons[start]-1:exons[end]])
     Dnaseqexon=Dnaseqexon+Dnaseq[exons[start]-1:exons[end]]
     start=start+2
     end=end+2
Rnaseq=""
print(Dnaseqexon)
for x in Dnaseqexon:
     if x=="T":
          Rnaseq=Rnaseq+"U"
     else:
          Rnaseq=Rnaseq+x
print(Rnaseq)