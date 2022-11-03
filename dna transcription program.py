
f=open("sequence.txt","r")
DNAsequence=f.read()
DNAsequence=DNAsequence.upper()
RNAsequence=""
for x in DNAsequence:
   if x =="T":
      RNAsequence=RNAsequence + "U"
   else:
      RNAsequence=RNAsequence + x
print(RNAsequence)