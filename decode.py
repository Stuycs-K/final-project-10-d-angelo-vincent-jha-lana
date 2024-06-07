import sys
import math
'''
Decode Process:
first keyword: polybius square
second keyword: column
encoded_message will have spaces

first step: split the message by spaces, which represents
each column into an array -done

copy into a diffferent array in the right order - method: rearrangecolumns - done

iterate thro the array and get each pair and put into another array - method: getpairs

create the polybius square array using the keyword - method: createsquare

create a string that goes thro the polybius square to find the message - method: getmessage

return string
'''

'''Takes arguments from decode and returns the final message'''
def decode(keyword1,keyword2,encoded_message):
    array_of_columns = encoded_message.split()
    arranged_columns = rearrange_columns(array_of_columns, keyword2)
    pairs = get_pairs(arranged_columns)
    polybius_square = create_square(keyword1)
    message = get_message(polybius_square,pairs)
    return(message)

'''Takes the orignal columns and the second keyword as arguments and returns an array with the columns rearranged into their original format(non alphabetically)'''
def rearrange_columns(original_columns, keyword2):
    alphabetized = ''.join(sorted(keyword2)) #puts the keyword in alphabetical order
    position_array=[] #holds the index of where each column should be in accordance to the original keyword

    for i in range(len(alphabetized)):
        count = 0
        counter = True
        while counter==True:
            if alphabetized[i] == keyword2[count] and (i == 0 or count != position_array[i-1]):#accounts for if there are duplicate letters in the keyword
                position_array.append(count)
                counter = False
            else:
                count+=1

    rearranged = ['empty']*len(position_array)
    for i in range(len(position_array)):#uses the indexes from position array to fill up the array with the rearranged columns
        rearranged[position_array[i]]= original_columns[i]
    return rearranged

'''Takes the arranged columns as an argument and returns pairs of letters that can be decoded using the polybius square'''
def get_pairs(arranged_columns):
    pairs = []
    length = len(arranged_columns[0])
    string_of_pairs = ""
    for i in range(length):
        for j in range(len(arranged_columns)):
            if i == length-1:
                 #last row
                if(len(arranged_columns[j])==length):
                    string_of_pairs+= arranged_columns[j][i]
            else:
                string_of_pairs+= arranged_columns[j][i]
    #splitting long string into array of pairs
    for x in range(0,len(string_of_pairs),2):
        pairs.append(string_of_pairs[x:x+2])
        
    return pairs

'''Takes the first keyword as an argument and returns an array that represents the 6x6 polybius square'''
def create_square(keyword1):
    keyword = "".join(dict.fromkeys(keyword1.replace(" ","").lower()))#removes spaces from keyword and duplicated
   

    total_string = "abcdefghijklmnopqrstuvwxyz0123456789"
    final_string = ""
    for i in range(len(total_string)):
        count = 0
        for k in keyword:
            if k == total_string[i]:
                count+=1
        if count <1:
            final_string += total_string[i]
   

    #final_string has rest of alphabet
    polybius_square = [""]*6#creates an array

    #fills the array so that the 6x6 square contains the keyword + the rest of the alphabet
    for i in range(math.floor(len(keyword)/6)):
        polybius_square[0] = keyword[0:6]
    
    mod = len(keyword) % 6
    if mod != 0:
        polybius_square[math.floor(len(keyword)/6)] = keyword[math.floor(len(keyword)/6)*6:]
        polybius_square[math.floor(len(keyword)/6)] += final_string[0:6 - mod]
    final_string = final_string[6-mod:]

    final_rows=[]

    for x in range(0,len(final_string),6):
        final_rows.append(final_string[x:x+6])

    for i in range(math.ceil(len(keyword)/6),6,1):
        polybius_square[i] = final_rows[i-math.ceil(len(keyword)/6)]

    return polybius_square

'''takes the polybius square and the pairs as an argument and returns the message by converting the letters in the pairs to their orginal letter'''
def get_message(square, pairs):
     #create list of rows,columns from pairs and get message by looping
    indexes = []
    message = ""
    for p in pairs:
        indexes.append(str(convert(p[0]))+ str(convert(p[1])))
    for i in indexes:
        message+=square[int(i[0])][int(i[1])]
    return message

'''takes a letter and returns the index of where it is located in the polybius square'''
def convert(letter):
    if letter == 'A':
        return 0
    elif letter == 'D':
        return 1
    elif letter == 'F':
        return 2
    elif letter == 'G':
        return 3
    elif letter == 'V':
        return 4
    elif letter == 'X':
        return 5

#takes arguments from terminal command, calls the decode function, and prints the final message
if len(sys.argv) == 5:
    if sys.argv[1] == "decode":
        keyword1 = sys.argv[2]
        keyword2 = sys.argv[3]
        encoded_message = sys.argv[4]
        print(decode(keyword1,keyword2,encoded_message))
