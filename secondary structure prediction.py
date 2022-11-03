ALPHA=dict(
A="1.42",
R="0.98",
D="1.01",
N="0.67",
C="0.70",
E="1.51",
Q="1.11",
G="0.57",
H="1.00",
I="1.08",
L="1.21",
K="1.14",
M="1.45",
F="1.13",
P="0.57",
S="0.77",
T="0.83",
W="1.08",
Y="0.69",
V="1.06"
) #print (float(ALPHA['A']))

BETA=dict(
A="0.83",
R="0.93",
D="0.54",
N="0.89",
C="1.19",
E="0.37",
Q="1.10",
G="0.75",
H="0.87",
I="1.60",
L="1.30",
K="0.74",
M="1.05",
F="1.38",
P="0.55",
S="0.75",
T="1.19",
W="1.37",
Y="1.47",
V="1.70",
) #print (float(BETA['A']))

TURN=dict(
A="0.66",
R="0.95",
D="1.46",
N="1.56",
C="1.19",
E="0.74",
Q="0.98",
G="1.56",
H="0.95",
I="0.47",
L="0.59",
K="1.01",
M="0.60",
F="0.60",
P="1.52",
S="1.43",
T="0.96",
W="0.96",
Y="1.14",
V="0.50"
) #print (float(TURN['A']))


fh=open("rv0183.fasta")
header=fh.readline()
seq=fh.read()
#print ("**",header,"**\n\n**",seq,"**")    

c=0
for i in range(len(seq)):
    # checking if any special character is present in given string or not
    if not(seq[i] >= 'A' and seq[i] <= 'Z'):
      c+=1   # if special character found then add 1 to the c; 
      # if c value is greater than 0 then print no  means special character is found in string      
      print (ascii(seq[i]))
"""      # EXECUTE ABOVE STATEMENTS
if c:
    print("string is not accepted")
else:
    print("string accepted")
"""    
print("Protein sequence not accepted" if c else "Protein sequence accepted")

seq=seq.replace("\n",'')
"""   ### RUN THIS BLOCK TO CHECK THE OPROTEIN SEQUENCE AGAIN
c=0
for i in range(len(seq)):
    if not(seq[i] >= 'A' and seq[i] <= 'Z'):
      c+=1
print("Protein sequence not accepted" if c else "Protein sequence accepted")
"""

print (seq)    

start=0
stop=4
check=True
PROPENSITY_TETRA_ALPHA=[]
PROPENSITY_TETRA_BETA=[]
PROPENSITY_TETRA_TURN=[]
SECONDARY_STRUCTURE_INITIAL=[]


while(check):
    TETRAPEPTIDE=seq[start:stop:]
    for index,alphabet in enumerate(TETRAPEPTIDE):
        print (index, alphabet, ALPHA[alphabet], BETA[alphabet], TURN[alphabet])
    if (len(TETRAPEPTIDE)<4):
        break
    print (TETRAPEPTIDE)
    print (start,float(ALPHA[TETRAPEPTIDE[0]]),float(ALPHA[TETRAPEPTIDE[1]]),float(ALPHA[TETRAPEPTIDE[2]]),float(ALPHA[TETRAPEPTIDE[3]]))
    
    PROPENSITY_TETRA_ALPHA.append(float(ALPHA[TETRAPEPTIDE[0]])+float(ALPHA[TETRAPEPTIDE[1]])+float(ALPHA[TETRAPEPTIDE[2]])+float(ALPHA[TETRAPEPTIDE[3]]))
#    print (PROPENSITY_TETRA_ALPHA[start])
    PROPENSITY_TETRA_ALPHA[start]=(PROPENSITY_TETRA_ALPHA[start])/4
    print (PROPENSITY_TETRA_ALPHA[start])
    
    PROPENSITY_TETRA_BETA.append(float(BETA[TETRAPEPTIDE[0]])+float(BETA[TETRAPEPTIDE[1]])+float(BETA[TETRAPEPTIDE[2]])+float(BETA[TETRAPEPTIDE[3]]))
#    print (PROPENSITY_TETRA_BETA[start])
    PROPENSITY_TETRA_BETA[start]=(PROPENSITY_TETRA_BETA[start])/4
    print (PROPENSITY_TETRA_BETA[start])

    PROPENSITY_TETRA_TURN.append(float(TURN[TETRAPEPTIDE[0]])+float(TURN[TETRAPEPTIDE[1]])+float(TURN[TETRAPEPTIDE[2]])+float(TURN[TETRAPEPTIDE[3]]))
#    print (PROPENSITY_TETRA_TURN[start])
    PROPENSITY_TETRA_TURN[start]=(PROPENSITY_TETRA_TURN[start])/4
    print (PROPENSITY_TETRA_TURN[start])
    
    if ( (PROPENSITY_TETRA_ALPHA[start]>=PROPENSITY_TETRA_BETA[start]) and  (PROPENSITY_TETRA_ALPHA[start]>=PROPENSITY_TETRA_TURN[start]) ):
        SECONDARY_STRUCTURE_INITIAL.append("H")
    elif ( (PROPENSITY_TETRA_BETA[start]>PROPENSITY_TETRA_BETA[start]) and  (PROPENSITY_TETRA_BETA[start]>=PROPENSITY_TETRA_TURN[start]) ):
        SECONDARY_STRUCTURE_INITIAL.append("E")
    else:
        SECONDARY_STRUCTURE_INITIAL.append("T")
    start+=1
    stop+=1

print (list(seq))
print ("\nSECONDARY_STRUCTURE_INITIAL=\n",SECONDARY_STRUCTURE_INITIAL)    