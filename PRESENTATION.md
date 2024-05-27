# ADFGVX Cipher
## _Part One: History_
![alt text](http://idata.over-blog.com/2/21/11/03/Nebel.jpg "Fritz Nebel, The Creator")
![alt text](https://static-images.lpnt.fr/cd-cw1618/images/2016/12/20/6475173lpw-6475235-article-jpg_3972919_660x287.jpg "Georges Painvin, The Destroyer")

### A long time ago, there was a war.  


+ In early 1918, the Germans needed a cipher that would provide moving troops with encryption that was both convenient and secure.  

+ The man tasked with the job was Signal Corps Lieutenant **Fritz Nebel** (1891–1977), and he soon developed what he called the _Geheimschrift der Funker 1918_ (in short _GedeFu 18_).  

+ By June, the cipher was being used to blare messages from German radio messages all over the Western Front. The Germans prided themselves on their invention, and believed it was **uncrackable**.  

## _Part Two: The Cipher_

The following is the encoding algorithm Fritz Nebel developed over a century ago.
### Section One: Polybius Square
The first part of the encoding process requires us to make a Polybius Square. Also known as a Polybius Checkerboard, this device was first used by the Ancient Greeks to represent complex messages with a smaller set of characters.  

Say we want to encode the message `attacktmrw`. This step requires the first of two keywords we'll need for the whole process, so let's choose `belgium`. The headings of our Polybius square will be the letters `a`, `d`, `f`, `g`, `v`[^1], and `x`. Instead of simply inserting the entire alphabet and the digits `0` to `9` into the square, first extract the characters that comprise the first keyword and move them to the front. Using our example, our square would look something like this.   

![alt text](https://raw.githubusercontent.com/Stuycs-K/final-project-10-d-angelo-vincent-jha-lana/presentation_encode/data/square.png "square")

Each letter of our plaintext message is then encrypted as the two "code" letters that represent its position, starting with the letter that marks its row (the y-axis, if you will). So, `a` becomes `DD`. `t` becomes `GF`, and so on. After this first step, `attacktmrw` is now written as `DDGFGFDDDFFDGFDAGAGV`.  

### Section Two: Columnar Transposition

Now, we need our second keywork, so let's choose `short`. That intermediate ciphered text we just created in the last step is written in rows beneath `short`. We now have this:
|**S**    |**H**    |**O**    |**R**|**T**|
|:---:|:---:|:---:|:---:|:---:|
|D|D|G|F|G|
|F|D|D|D|F|
|F|D|G|F|D|
|A|G|A|G|V|

Next, we number each letter of the keyword in alphabetical order, creating this:
|**S**    |**H**    |**O**    |**R**|**T**|
|:---:|:---:|:---:|:---:|:---:|
|4|1|2|3|5|
|D|D|G|F|G|
|F|D|D|D|F|
|F|D|G|F|D|
|A|G|A|G|V|

Finally, read off the intermediate ciphered text down the columns, starting with the column labeled `1` and ending with the column labeled `5`. Our final ciphered text, therefore, is `DDDG GDGA FDFG DFFA GFDV`.

[^1]: These specific letters were deliberately chosen because they appear very dissimilar when written in Morse code, making communicating messages a lot easier and a lot less prone to human error. Initially, the headings of the Polybius square only had the letters `a`, `d`, `f`, `g`, and `x`. The `v` was added a few months later to allow for the encryption of the full alphabet and the digits `0` to `9` (in total, 36 characters).
