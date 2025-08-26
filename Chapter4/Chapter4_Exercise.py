def ProcessingDNAInAFile():
    inputFile=open("input.txt")
    input = inputFile.read()
    #actually python can split automatically according to /n
    #no need to manually split it. 
    ListInput = input.split("\n")
    print(ListInput)
    outputFile = open("output.txt","w")
    for dna in ListInput:
        dna = dna[14:len(dna)]
        outputFile.write(dna+"\n")
        print (len(dna))


def MultipleExonsFromGenomicDNA():
    Exons = open("exons.txt")
    GenomicDNA = open("genomic_dna.txt").read()
    outputFile = open("Extracted_Exons.txt","w")
    for exon in Exons:
        #if typecast into integer, it seems like /n will be ignored. 
        #no need to manually rstrip()
        #exon = exon.rstrip()
        exonposition = exon.split(",")
        sub = GenomicDNA[int(exonposition[0]):int(exonposition[1])]
        outputFile.write(sub)
          



def main():
    ProcessingDNAInAFile()
    MultipleExonsFromGenomicDNA()


if __name__ == '__main__':
    main()    
