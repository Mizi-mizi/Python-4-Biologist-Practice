def my_function(protein, AA = ['A','I','L','M','F','W','Y','V']):
    count = 0
    for aa in AA:
        count += protein.count(aa.upper())
    percentage = (count / len(protein)) * 100
    return round(percentage,1)

def part1():
    assert my_function("MSRSLLLRFLLFLLLLPPLP", "M") == 5
    assert my_function("MSRSLLLRFLLFLLLLPPLP", "r") == 10
    assert my_function("MSRSLLLRFLLFLLLLPPLP", "L") == 50
    assert my_function("MSRSLLLRFLLFLLLLPPLP", "Y") == 0

def part2():
    assert my_function("MSRSLLLRFLLFLLLLPPLP", ["M"]) == 5
    assert my_function("MSRSLLLRFLLFLLLLPPLP", ['M', 'L']) == 55
    assert my_function("MSRSLLLRFLLFLLLLPPLP", ['F', 'S', 'L']) == 70
    assert my_function("MSRSLLLRFLLFLLLLPPLP") == 65
    
def main():
    part1()
    part2()

if __name__ == '__main__':
    main()