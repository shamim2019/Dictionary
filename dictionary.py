#creating a dictionary of keys as integers and their squares as values.
numbers = {
    "1" : 1**2,
    "2" : 2**2,
    "3" : 3**2,
    "4" : 4**2,
    "5" : 5**2,
    "6" : 6**2,
    "7" : 7**2,
    "8" : 8**2,
    "9" : 9**2,
    "10": 10**2,
    "11": 11**2,
    "12": 12**2,
    "13": 13**2,
    "14": 14**2,
    "15": 15**2
}
for key, value in numbers.items():
    print("The square of: "  + str(key) + "  is: "   + str(value))