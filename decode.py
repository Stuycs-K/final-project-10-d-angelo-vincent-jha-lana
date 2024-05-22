'''
Decode Process:
first keyword: polybius square
second keyword: column
encoded_message will have spaces

first step: split the message by spaces, which represents
each column into an array - method: getcolumns

copy into a diffferent array in the right order - method: rearrangecolumns

iterate thro the array and get each pair and put into another array - method: getpairs

create the polybius square array using the keyword - method: createsquare

create a string that goes thro the polybius square to find the message - method: getmessage

return string
'''
'''Takes arguments from decode and returns the final message'''
def decode(keyword1,keyword2,encoded_message):
    #
    return("hi")
    
if len(sys.argv) == 4:
    if sys.argv[1] == "decode":
        keyword1 = sys.argv[2]
        keyword2 = sys.argv[3]
        encoded_message = sys.argv[4]
        print(decode(keyword1,keyword2,encoded_message))
