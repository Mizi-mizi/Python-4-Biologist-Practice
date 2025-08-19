import os
def SplittingGenomicDNA():
    
    my_file = open("dna.txt")
    GenomicDNA = my_file.read()
    #From part 2
    codingR = GenomicDNA[0:63] + GenomicDNA[90:100000]
    print ("The coding regions of the DNA sequence: "+ codingR)
    
    NoncodingR = GenomicDNA[63:90]
    
    #create new file and write codingR in it
    codingRegion = open("codingRegion.txt","w") 
    codingRegion.write(codingR)   
    NoncodingRegion = open ("noncodingRegion.txt","w")
    NoncodingRegion.write(NoncodingR)
         

def WritingAFASTAFile():
    myFastaFile = open ("FASTA_Chapt3.txt","w")
    Header1 = ">ABC123"
    Header2 = ">DEF456"
    Header3 = ">HIJ789"
    Sequence1 = "ATCGTACGATCGATCGATCGCTAGACGTATCG"
    Sequence2 = "actgatcgacgatcgatcgatcacgact"
    Sequence3 = "ACTGAC-ACTGT--ACTGTA----CATGTG"
    Sequence2 = Sequence2.upper()
    Sequence3 = Sequence3.replace('-',"")
    myFastaFile.write(Header1 + "\n" + Sequence1 +"\n" + Header2 + "\n" + Sequence2 +"\n" + Header3 + "\n" + Sequence3)
    


def WritingMultipleFASTAFiles():
   my_file_1 = open ("ABC123.fasta","w")
   my_file_1.write("ATCGTACGATCGATCGATCGCTAGACGTATCG") 
   my_file_2 = open ("DEF456.fasta","w")
   my_file_2.write("actgatcgacgatcgatcgatcacgact".upper())
   my_file_3 = open ("HIJ789.fasta","w")
   my_file_3.write("ACTGAC-ACTGT--ACTGTA----CATGTG".replace("-",""))



def main():
    SplittingGenomicDNA()
    WritingAFASTAFile()
    WritingMultipleFASTAFiles()
    
    
    
    
    
    
    
    
if __name__ == '__main__':
    main()
    