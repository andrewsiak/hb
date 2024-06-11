def romanToInt(string):  
        # create a hashmap
        # I = 1
        # V = 5
        # X = 10
        # L = 50
        # C = 100
        # D = 500
        # M = 1000
    integer = 0

    roman_dict = {
        "I": 1, 
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
        }

    for index, char_in_string in enumerate(string): 
        
        if index + 1 == len(string) or roman_dict[char_in_string] >= roman_dict[string[index+1]]:
            integer = integer + roman_dict[char_in_string]
        else:
            integer = integer - roman_dict[char_in_string]
        print(integer)
        print(char_in_string)

    print("final:", integer)
    return integer
    
    # pop from end of list add to integer value from dictionary
    # unless I X or C

    # if I is before V or X using list.index
    # if X is before L or C using list.index
    # if C is before D or M using list.index

test_1 = "III"
print("Test 3:", romanToInt(test_1))

test_2 = "LVIII"
print("Test 58:", romanToInt(test_2))

test_3 = "MCMXCIV"
print("Test 1994:", romanToInt(test_3))

# TODO update print tests to return true false tests