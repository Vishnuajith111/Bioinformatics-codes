"""
retrieve data from UniProt text format
"""

import re
#pattern_SYMBOL = "^AC\s\s\s\w+;\s\w+" #AC   Q99685
pattern_SYMBOL = "^FT\s+ACT_SITE"
pattern_SYMBOL_RP = "^FT\s+\/"
pattern_found=0


with open('MGLL_HUMAN.txt') as fh:
    seq = ""
    for line in fh:
        # print(line.strip())
        rgx_SYMBOL = re.compile(pattern_SYMBOL)
        result_SYMBOL = rgx_SYMBOL.search(line)
        rgx_SYMBOL_RP = re.compile(pattern_SYMBOL_RP)
        result_SYMBOL_RP = rgx_SYMBOL_RP.search(line)
        #print(type(result_SYMBOL))
        

        if (result_SYMBOL) :
            print (line.strip())
            print(result_SYMBOL.__dir__)
            pattern_found=1
        elif (result_SYMBOL_RP) and (pattern_found):
            print (line.strip())
            pattern_found=1
        elif (pattern_found):
            break
 