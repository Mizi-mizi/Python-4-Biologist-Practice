def helperMethod(data):
    newdata =  data.split("\n")
    res = []
    for line in newdata:
        Record = line.split(",")
        res.append(Record)
    clean_res = [row for row in res if row != ['']]
    return clean_res
        

def SeveralSpecies(data):
    print ("Several Species:")
    List = helperMethod(data)
    for line in List:
        if line[0] == "Drosophila melanogaster" or line[0] == "Drosophila simulans":
            print (line[2])
            
def LengthRange(data):
    print ("Length Range:")
    List = helperMethod(data)
    print (List)
    for line in List:
        if len(line[1]) >= 90 and len(line[1]) <= 110:
            print (line[2]) 
    
def ATContent(data):
    print ("ATContent")
    List = helperMethod(data)
    for line in List:
        dna=line[1].upper()
        atCount = dna.count("A") + dna.count("T")
        if (atCount/len(line[1]) < 0.5 and int(line[3]) > 200):
            print (line[2])
    
def ComplexCondition(data):
    print ("Complex Condition")
    List = helperMethod(data)
    for line in List:
        if line[0] == "Drosophila melanogaster":
            continue
        if line[2].startswith('k') or line[2].startswith('h'):
            print (line[2])

def HighLowMedium(data):
    print ("High Low Medium")
    List = helperMethod(data)
    for line in List:
        dna = line[1].upper()
        ATCount = dna.count("A") + dna.count("T")
        if ATCount / len(dna) > 0.65:
            print ("Gene Name: " + line[2] + ". Its AT content is high")
        elif ATCount / len(dna) < 0.45:
            print ("Gene Name: " + line[2] + ". Its AT content is low")
        else:
            print ("Gene Name: " + line[2] + ". Its AT content is medium")



def main():
    dataFile = open("data.csv")
    data = dataFile.read()
    SeveralSpecies(data)
    LengthRange(data)
    ATContent(data)
    ComplexCondition(data)
    HighLowMedium(data)



    
if __name__ == '__main__':
    main()