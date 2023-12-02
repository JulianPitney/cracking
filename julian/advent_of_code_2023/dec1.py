def decode_treb_calib(filename):
    
    nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    with open(filename) as file:
        lines = [line.rstrip() for line in file]
    
    sum = 0
    for line in lines:
        first = None
        second = None 
        for char in line:
            if char in nums:
                first = char
                break
        for char in line[::-1]:
            if char in nums:
                second = char
                break
        sum += int(first + second)
    
    return sum


def decode_treb_calib2(filename):

    nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    letter_nums = ["zero", "one", "two", "three", "four", "five",
                   "six", "seven", "eight", "nine"]
    
    with open(filename) as file:
        lines = [line.rstrip() for line in file]

    for line in lines:
        word = ""
        for char in line:
            if char not in nums:
                word += char
                


treb_calib = decode_treb_calib("./data/input.txt")
treb_calib2 = decode_treb_calib2("./data/input.txt")
print(treb_calib)