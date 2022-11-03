proteinseq="MSKFLLQSHSANACLLTLLLTLASNLDISLANFEHSCNGYMRPHPRGLCGEDLHVIISNLCSSLGGNRRF"
proteinseq=proteinseq.upper()
protlength=len(proteinseq)
print(protlength)
Ala=(proteinseq.count("A")/protlength)*100
print("% of Alanine",Ala)
Arg=(proteinseq.count("R")/protlength)*100
print("% of Arginine",Arg)
Asn=(proteinseq.count("N")/protlength)*100
print("% of Aspargine",Asn)
Cys=(proteinseq.count("C")/protlength)*100
print("% of Cysteine",Cys)
Glu=(proteinseq.count("E")/protlength)*100
print("% of Glutamic acid",Glu)
Gln=(proteinseq.count("Q")/protlength)*100
print("% of Glutamine",Gln)
Gly=(proteinseq.count("G")/protlength)*100
print("% of Glycine",Gly)
His=(proteinseq.count("H")/protlength)*100
print("% of Histidine",His)
Ile=(proteinseq.count("I")/protlength)*100
print("% of Isoleucine",Ile)
Leu=(proteinseq.count("L")/protlength)*100
print("% of Leucine",Leu)
Lys=(proteinseq.count("K")/protlength)*100
print("% of Lysine",Lys)
Met=(proteinseq.count("M")/protlength)*100
print("% of Methionine",Met)
Phe=(proteinseq.count("F")/protlength)*100
print("% of Phenylalanine",Phe)
Val=(proteinseq.count("V")/protlength)*100
print("% of Valine",Val)
Tyr=(proteinseq.count("Y")/protlength)*100
print("% of Tyrosine",Tyr)
Trp=(proteinseq.count("W")/protlength)*100
print("% of Tryptophan",Trp)










