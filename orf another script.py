dna=input("ENTER A DNA SEQUENCE")
dna=dna.upper()
newdna=""
answer=input("IS YOUR DNA SEQUENCE FOR \n (1)STANDARD DNA \n (2)MITOCHONDRIAL DNA \n (3)PERITRICH NUCLEAR DNA \n ENTER 1/2/3")
for a in dna:
    if a=="A" or a=="T" or a=="G" or a=="C":
        newdna+=a
protein_table=dict({"AUG":"M","UUU":"F","UUC":"F","UUA":"L","UUG":"L","UCU":"S","UCC":"S","UCA":"S","UCG":"S","UAU":"Y","UAC":"Y","UAA":"Stop",
      "UAG":"Stop","UGU":"C","UGC":"C","UGA":"Stop","UGG":"W","CUU":"L","CUC":"L","CUA":"L","CUG":"L","CCU":"P","CCC":"P","CCA":"P",
      "CCG":"P","CAU":"H","CAC":"H","CAA":"Q","CAG":"Q","CGU":"R","CGC":"R","CGA":"R","CGG":"R","AUU":"I","AUC":"I","AUA":"I",
      "ACU":"T","ACC":"T","ACA":"T","ACG":"T","AAU":"N","AAC":"N","AAA":"K","AAG":"K","AGU":"S","AGC":"S","AGA":"R","AGG":"R","GUA":"V",
      "GUC":"V","GUG":"V","GUU":"V","GCU":"A","GCC":"A","GCA":"A","GCG":"A","GAU":"D","GAC":"D","GAA":"E","GAG":"E","GGA":"G","GGU":"G","GGC":"G","GGG":"G"})

protein_table_mito=dict({"AUG":"M","UUU":"F","UUC":"F","UUA":"L","UUG":"L","UCU":"S","UCC":"S","UCA":"S","UCG":"S","UAU":"Y","UAC":"Y","UAA":"Stop",
      "UAG":"Stop","UGU":"C","UGC":"C","UGA":"W","UGG":"W","CUU":"L","CUC":"L","CUA":"L","CUG":"L","CCU":"P","CCC":"P","CCA":"P",
      "CCG":"P","CAU":"H","CAC":"H","CAA":"Q","CAG":"Q","CGU":"R","CGC":"R","CGA":"R","CGG":"R","AUU":"I","AUC":"I","AUA":"M",
      "ACU":"T","ACC":"T","ACA":"T","ACG":"T","AAU":"N","AAC":"N","AAA":"K","AAG":"K","AGU":"S","AGC":"S","AGA":"Stop","AGG":"Stop","GUA":"V",
      "GUC":"V","GUG":"V","GUU":"V","GCU":"A","GCC":"A","GCA":"A","GCG":"A","GAU":"D","GAC":"D","GAA":"E","GAG":"E","GGA":"G","GGU":"G","GGC":"G","GGG":"G"})

protein_table_Peritrich_Nuclear_Code=dict({"AUG":"M","UUU":"F","UUC":"F","UUA":"L","UUG":"L","UCU":"S","UCC":"S","UCA":"S","UCG":"S","UAU":"Y","UAC":"Y","UAA":"Q",
      "UAG":"Q","UGU":"C","UGC":"C","UGA":"Stop","UGG":"W","CUU":"L","CUC":"L","CUA":"L","CUG":"L","CCU":"P","CCC":"P","CCA":"P",
      "CCG":"P","CAU":"H","CAC":"H","CAA":"Q","CAG":"Q","CGU":"R","CGC":"R","CGA":"R","CGG":"R","AUU":"I","AUC":"I","AUA":"I",
      "ACU":"T","ACC":"T","ACA":"T","ACG":"T","AAU":"N","AAC":"N","AAA":"K","AAG":"K","AGU":"S","AGC":"S","AGA":"R","AGG":"R","GUA":"V",
      "GUC":"V","GUG":"V","GUU":"V","GCU":"A","GCC":"A","GCA":"A","GCG":"A","GAU":"D","GAC":"D","GAA":"E","GAG":"E","GGA":"G","GGU":"G","GGC":"G","GGG":"G"})

def reverse(rnaf):
    rnab=""
    for y in range(len(rnaf)-1,-1,-1):
        rnab=rnab+rnaf[y]
    print("FORWARD RNA=",rnaf)
    print("REVERSE RNA=",rnab)
    return rnab

def adjust(i,rnaf):
    num=0
    rna=""
    rna=rnaf[i:]
    length=len(rna)
    num=length%3
    n=length-num
    rna=rna[0:n]
    return rna

def orf_std(k,rnaf1):
    length=len(rnaf1)
    protein1=""
    codon=""
    for i in range(0,length,3):
        codon=rnaf1[i:(i+3)]
        protein1+=p_dict.protein_table[codon]
    print("OPEN READING FRAME",(k+1),"=",protein1)

def orf_mito(k,rnaf1):
    length=len(rnaf1)
    protein1=""
    codon=""
    for i in range(0,length,3):
        codon=rnaf1[i:(i+3)]
        protein1+=p_dict.protein_table_mito[codon]
    print("OPEN READING FRAME",(k+1),"=",protein1)

def orf_Peritrich_Nuclear_Code(k,rnaf1):
    length=len(rnaf1)
    protein1=""
    codon=""
    for i in range(0,length,3):
        codon=rnaf1[i:(i+3)]
        protein1+=p_dict.protein_table_Peritrich_Nuclear_Code[codon]
    print("OPEN READING FRAME",(k+1),"=",protein1)
    
rnaf=""
for x in newdna:
    if x=="T":
        rnaf=rnaf+"U"
    else:
        rnaf=rnaf+x
rev=reverse(rnaf)
rnaf1=adjust(0,rnaf)
rnaf2=adjust(1,rnaf)
rnaf3=adjust(2,rnaf)
rnab1=adjust(0,rev)
rnab2=adjust(1,rev)
rnab3=adjust(2,rev)

if answer==1:
    orf_std(0,rnaf1)
    orf_std(1,rnaf2)
    orf_std(2,rnaf3)
    orf_std(3,rnab1)
    orf_std(4,rnab2)
    orf_std(5,rnab3)
elif answer==2:
    orf_mito(0,rnaf1)
    orf_mito(1,rnaf2)
    orf_mito(2,rnaf3)
    orf_mito(3,rnab1)
    orf_mito(4,rnab2)
    orf_mito(5,rnab3)
else:
    orf_Peritrich_Nuclear_Code(0,rnaf1)
    orf_Peritrich_Nuclear_Code(1,rnaf2)
    orf_Peritrich_Nuclear_Code(2,rnaf3)
    orf_Peritrich_Nuclear_Code(3,rnab1)
    orf_Peritrich_Nuclear_Code(4,rnab2)
    orf_Peritrich_Nuclear_Code(5,rnab3)
