import re

def AccessionNames():
    AccessionName = "xkn59438, yhdck2, eihd39d9, chdsye847, hedle3455, xjhd53e, 45da, de37dp"
    listOfName = AccessionName.split(", ")
    list1,list2, list3, list4, list5, list6, list7, list8, list9 = [],[],[],[],[],[],[],[],[]
    
    for name in listOfName:
        if re.search(r"5",name):
            list1.append(name)
        if re.search(r"(d|e)",name):
            list2.append(name)
        if re.search(r"d.*e",name):
            list3.append(name)
        if re.search(r"d.e",name):
            list4.append(name)
        if re.search(r"d",name) and re.search(r"e", name):
            list5.append(name)
        if re.search(r"^[xy]",name):
            list6.append(name)
            if re.search(r"e$",name):
                list7.append(name)
        #Actually can use \d instead of [1234567890]
        if re.search(r"[1234567890]{3,}",name):
            list8.append(name)
        if re.search(r"d[arp]$",name):
            list9.append(name)
        
    print("Contain the number 5: \n")
    print (list1)
    print ("Contain the letter d or e: \n")
    print (list2)
    print ("Contain the letters d and e in that order")
    print (list3)
    print ("Contain the letters d and e in that order with a single letter between them: \n")
    print (list4)
    print ("Contain both the letter d and e in any order \n")
    print (list5)
    print ("Start with x or y: \n")
    print (list6)
    print ("Start with x or y and end with e: \n")
    print (list7)
    print ("Contain three or more numbers in a row: \n")
    print (list8)
    print ("End with d followed by either a, r or p: \n")
    print (list9)

def DoubleDigest():
    file = open("dna.txt")
    dna=file.read().rstrip()
    cuttingSite = [0]
    print(len(dna))
    runs1 = re.finditer(r"A[ATCG]TAAT",dna)
    runs2 = re.finditer(r"GC[AG][AT]TG",dna)
    for run in runs1:
        
        cuttingSite.append(int(run.start())+3)
        print (run.group())
    for run in runs2:
        cuttingSite.append(int(run.start())+4)
        print (run.group())
    cuttingSite.append(len(dna))
    cuttingSite.sort()
    FragmentLength = []
    for i in range(1,len(cuttingSite)):
        FragmentLength.append(cuttingSite[i] - cuttingSite[i-1])
    
    print (FragmentLength)
            
    


def main():
    AccessionNames()
    DoubleDigest()
    

if __name__ == '__main__':
    main()