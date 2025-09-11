import os
import sys
import argparse

def BinningDNASequences():
    wkd = os.getcwd()
    inputList = [[],[],[],[],[],[],[],[],[]]
    RangeOfLength = ["100-199","200-299","300-399","400-499","500-599","600-699","700-799","800-899","900-999"]

    for file_name in os.listdir("."):
        if file_name.endswith(".dna"):
            content = open(file_name)
            dnaSeqInFile = content.readlines()
            for dnaSeq in dnaSeqInFile:
                dna = dnaSeq.rstrip()
                for i in range(1,10):
                    length = len(dna)
                    if length>= i*100 and length <= (i+1)*100 -1 :
                        inputList[i-1].append(dna+"\n")
   
    for r in RangeOfLength:
        os.mkdir(wkd+"/"+r)
        file = open(wkd+"/"+r+"/inputFile.txt","w")
        for input in inputList[RangeOfLength.index(r)]:
            file.write(input)

                  
        
    
def KmerCounting():
    #create parser
    parser = argparse.ArgumentParser(description="Chapter9_Exercise.py")
    parser.add_argument("length",type=int, help="kmer_length")
    parser.add_argument("number",type=int,help="the cutoff number")
    args=parser.parse_args()
    #args.length and args.number are used to store values
    
    #variable that used to store all the kmer and their counts
    kmerCounts = {}
    loopcount = 0
    #Read all DNA sequences 
    for filename in os.listdir("."):
        if filename.endswith(".dna"):
            content=open(filename)
            for dna in content:
                dna = dna.rstrip()
                for k in range(0,len(dna)-int(args.length)):
                    kmer = dna[k:args.length + k]
                    kmerCounts[kmer] = kmerCounts.get(kmer,0) + 1
    
    print (loopcount)
    #Select what get printed 
    for kmers,counts in kmerCounts.items():

        if counts > args.number:
            print ("Kmer: " + kmers + " Counts: " + str(counts) + "\n")
        
            
            
    
    




def main():
    #BinningDNASequences()
    KmerCounting()

if __name__ == '__main__':
    main()