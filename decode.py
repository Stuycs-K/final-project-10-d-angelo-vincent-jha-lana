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
    return(polybius_square)
    # return("hi")

def rearrange_columns(original_columns, keyword2):
    alphabetized = ''.join(sorted(keyword2))
    # print(alphabetized)
    position_array=[]
    
    for a in alphabetized:
        count = 0
        counter = True
        while counter==True:
            if a == keyword2[count]:
                position_array.append(count)
                counter = False
            else:
                count+=1
    # print(position_array)

    rearranged = ['empty']*len(position_array)
    for i in range(len(position_array)):
        # print(i)
        rearranged[position_array[i]]= original_columns[i]
    return rearranged

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
    polybius_square = [""]*6#creates a 6x6 double array
    for i in range(math.floor(len(keyword)/6)):
        polybius_square[0] = keyword[0:6]
    
    mod = len(keyword) % 6
    if mod != 0:
        polybius_square[math.floor(len(keyword)/6)] = keyword[math.floor(len(keyword)/6)*6:]
        polybius_square[math.floor(len(keyword)/6)] += final_string[0:6 - mod]
    final_string = final_string[6-mod:]

    final_rows=[]
    #splitting final_string into array of 6's
    for x in range(0,len(final_string),6):
        final_rows.append(final_string[x:x+6])
    for i in range(math.ceil(len(keyword)/6),6,1):
        polybius_square[i] = final_rows[i-2]

    return polybius_square
'''remove spaces
make everything lower case
total_string = 'abcdefghijklmnopqrstuvwxyz0123456789'
make double array
iterate through rows adding the keyword first, keep count

for loop thro the rest of the double array starting at that point and check in this loop, go thro the total_string adn add accordingly
'''




if len(sys.argv) == 5:
    if sys.argv[1] == "decode":
        keyword1 = sys.argv[2]
        keyword2 = sys.argv[3]
        encoded_message = sys.argv[4]
        print(decode(keyword1,keyword2,encoded_message))
