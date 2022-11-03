import re
pattern1="GAATTCC"
pattern2= "CTTAAGG"
seq1=""
seq2=""


with open("ECOLI.fasta") as fh:
    fh.readline()
    for i in fh:
        seq1+=i.strip()
        seq2+=i.strip()

site1=re.compile(pattern1)
result1=site1.search(seq1)
pat_found1=result1.group()
span_site1=result1.span()

print("Restriction site found:",result1)
print("Restriction site pattern:",pat_found1)
print("Restriction site location:",span_site1)

site2=re.compile(pattern2)
result2=site2.search(seq2)
pat_found2=result2.group()
span_site2=result2.span()

print("Restriction site found:",result2)
print("Restriction site pattern:",pat_found2)
print("Restriction site location:",span_site2)
