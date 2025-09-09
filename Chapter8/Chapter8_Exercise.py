import re

def DNA_Translation(dna):
    #clean inputed dna
    dna = dna.upper()
    codonList = []
    geneticCodeTable = {}
    AAs="FFLLSSSSYY**CCWWLLLLPPPPHHQQRRRRIIMMTTTTNNKKSS**VVVVAAAADDEEGGGG"
    #spliting dna
    for i in range(0,len(dna),3):
        codonList.append(dna[i:i+3])
    
    #mapping AA and base
    i = 0
    for base1 in ["T","C","A","G"]:
        for base2 in ["T","C","A","G"]:
            for base3 in ["T","C","A","G"]:
                tri = base1+base2+base3
                geneticCodeTable[tri] = AAs[i]
                i+=1
    
    #find start position
    try:
        start_position = codonList.index("ATG")
    except:
        print("No starting codon")
        return 
        
    #modifying to prevent len of dna is not a multiple of 3
    if len(codonList[-1]) != 3:
        codonList.pop(-1)
        
    #translating dna
    protein = ""
    for codon in codonList [start_position:len(codonList)]:
        Valid = True
        for base in codon:
            if re.match(r"[^ATCG]",base):
                protein += "X"
                Valid = False
        if Valid == True:
            protein = protein + geneticCodeTable[codon]
    print (protein)
                
                

def main():
    dna = input("put ur dna here:")
    DNA_Translation(dna)





if __name__ == '__main__':
    main()