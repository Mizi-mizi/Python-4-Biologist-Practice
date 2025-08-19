def main():
    print ("This is the exercise of Chapter 2;")
    

    print ("\n\n"+"Q1: Calculating AT content")
    DNA= "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
    AtCount = DNA.count("AT")
    ACount = DNA.count('A')
    TCount = DNA.count('T')
    print ("The DNA sequence is: " + DNA)
    print ("AT count: " + str(AtCount))
    print ("The num of A in DNA: " + str(ACount))
    print ("The num of T in DNA: " + str(TCount))
    print ("The AT Content ratio: " + str((ACount + TCount)/len(DNA)))
    
    
    print ("\n\n"+"Q2: Complementing DNA")
    DNALength = len(DNA)
    newDNA = ""
    for i in range (DNALength):
        if (DNA[i] == 'A'):
            newDNA += 'T'
        if (DNA[i] == 'T'):
            newDNA += 'A'
        if (DNA[i] == 'C'):
            newDNA += 'G'
        if (DNA[i] == 'G'):
            newDNA += 'C'
            
    #use replacement. lowercase is something chagned, upper is original
    #Python Strings are immutable. 
    #It would work better if use list instead of string
    print ("The complement of this sequence is: " + newDNA)
    
    
    print ("\n\n"+"Q3: Restriction fragment lengths")
    RestrictionDNA = "ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT"
    siteIndex = RestrictionDNA.find("GAATTC")
    fragment1Size = siteIndex + 1
    fragment2Size = DNALength - siteIndex
    print ("Fragment 1 size: " + str(fragment1Size))
    print ("Fragment 2 size: " + str(fragment2Size))
    
    
    print ("\n\n"+"Q4: Splicing out introns, part 1")
    GenomicDNA = "ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"
    print ("The original DNA sequence is: " + GenomicDNA)
    codingRegion = GenomicDNA[0:63] + GenomicDNA[90:100000]
    print ("The coding regions of the DNA sequence: "+ codingRegion)
    
    print ("\n\nQ5: Splicing out introns, part 2")
    print ("The percentage of DNA sequence coded: " + str(len(codingRegion)/len(GenomicDNA)))
    
    
    
if __name__ == '__main__':
    main()