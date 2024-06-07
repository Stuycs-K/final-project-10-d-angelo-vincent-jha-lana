# ADFGVX Cipher
## _Part One: History_
![alt text](http://idata.over-blog.com/2/21/11/03/Nebel.jpg "Fritz Nebel, The Creator")
![alt text](https://static-images.lpnt.fr/cd-cw1618/images/2016/12/20/6475173lpw-6475235-article-jpg_3972919_660x287.jpg "Georges Painvin, The Destroyer")

### A long time ago, there was a war.  


+ In early 1918, the Germans needed a cipher that would provide moving troops with encryption that was both convenient and secure.  

+ The man tasked with the job was Signal Corps Lieutenant **Fritz Nebel** (1891–1977), and he soon developed what he called the _Geheimschrift der Funker 1918_ (in short _GedeFu 18_).  

+ By June, the cipher was being used to blare messages from German radio stations all over the Western Front. The Germans prided themselves on their invention, and believed it was **uncrackable**.  

## _Part Two: The Cipher_

The following is the encoding algorithm Fritz Nebel developed over a century ago.
### Section One: Polybius Square
The first part of the encoding process requires us to make a Polybius Square. Also known as a Polybius Checkerboard, this device was first used by the Ancient Greeks to represent complex messages with a smaller set of characters.  

Say we want to encode the message `attacktmrw`. This step requires the first of two keywords we'll need for the whole process, so let's choose `belgium`. The headings of our Polybius square will be the letters `a`, `d`, `f`, `g`, `v`[^1], and `x`. Instead of simply inserting the entire alphabet and the digits `0` to `9` into the square, first extract the characters that comprise the first keyword and move them to the front. Using our example, our square would look something like this.   

![alt text](https://raw.githubusercontent.com/Stuycs-K/final-project-10-d-angelo-vincent-jha-lana/presentation_encode/data/square.png "square")

Each letter of our plaintext message is then encrypted as the two "code" letters that represent its position, starting with the letter that marks its row (the y-axis, if you will). So, `a` becomes `DD`. `t` becomes `GF`, and so on. After this first step, `attacktmrw` is now written as `DDGFGFDDDFFDGFDAGAGV`.  

### Section Two: Columnar Transposition

Now, we need our second keyword, so let's choose `short`. That intermediate ciphered text we just created in the last step is written in rows beneath `short`. We now have this:
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

## _Part Three: Cracking the Cipher_


The ADFGVX cipher was cracked by Lieutenant Georges Painvin of the French Cipher Bureau in June of 1918. He used techniques like cribbing and similarities in messages to do this.

### Section 1: Challenges

What makes this cipher so hard to crack is the fact that there is a transposition involved after the checkerboard subsitution. If only the substition was done, the cipher could be cracked using frequency analysis. The use of only 5 or 6 letters implies the checkerboard, and the use of the checkerboard, implies the splitting of the message into pairs, or digraphs. The frequency of these pairs, or digraphs, could then be anaylzed and compared to frequencies of plaintext letters and then matched. 

However, because of the transposition that occurs, these digraphs are seperated from their pair in a different order. 

After the checkerboard substitution, digraphs respresenting each plaintext letter in the message are formed. The digraphs are placed into columns, which each pair in the digraph being placed in a different column. Here is a visual that shows this:


|**C**    |**A**    |**R**    |**G**|**O**|
|:---:|:---:|:---:|:---:|:---:|
|A|F|A|D|A|
|D|A|F|G|F|
|D|X|A|F|A|
|D|D|F|F|X|
|G|F|X|F||

When the columnar transposition occurs, all digraphs are separated. For example, in the image above, look at the digraph 'FG', which are in the second row and under the 'R' and 'G' column. In the image below, the 'FG' digraph has been separated, with the 'F' going from the 3rd column to the last, and the 'G' going from the 4th column to the 3rd to 'FA' after the transposition. If you look at other pairs, you can find a similar separation.

|**A**    |**C**    |**G**    |**O**|**R**|
|:---:|:---:|:---:|:---:|:---:|
|F|A|D|A|A|
|A|D|G|F|F|
|X|D|F|A|A|
|D|D|F|X|F|
|F|G|F||X|

As a result, the frequencies will be fractioned, leading to an inaccurate comparison of digraph frequencies to plaintext frequencies. 

### Section 2: Process

When Painvin first encountered an encoded message, he noticed that there were only 5(eventually 6) letters present and based on this, assumed that there was a checkerboard type encoder involved. His next step, was to test out simple substituion ciphers within the checkerboard. When those tests came out negative, he knew that in addition to a checkerboard substition, there was some sort of transposition. 

Eventually, Painvin found two ciphertexts that were very similar and intercepted at the same time, to be almost identical for the first several characters. He guessed that the plaintexts for both were also identical, at least in the beginning of the message. Using this assumption, this would mean that the top few entires of the columns for both messages are the same. If you look through the ciphertext and find places where they agree with each other, those places would be the beginnings of the columns. Then, you could find the column lengths from this, and divide the ciphertexts into columns of those lengths, with longer columns being at the beginning. Using both ciphertexts, if a column is long for both cipherboths, it would be placed in the beginning. If a column was short for both ciphertexts, it would be placed at the end. If the coluns from both don't agree in length, then it would go in the middle. From this approximate column placings, many orderings can be tried, and from these ordering, frequency analysis can be used on the digraphs that occur. Eventually, one combination will lead to the plaintext message.

## _Part Four: Strengths and Weaknesses_
|**Strengths**    |**Weaknesses**    |
|:---:|:---:|
|difficult to decrypt without the key|vulnerable to plaintext and frequency analysis attacks|
|versatile as it can be used for image and text encryption|vulnerable to brute force attacks when a key is repeated or small|
|good level of security|should not be used to encrypt high security information, like for military or government purposes|


## _Part Five: Final Words_

Nebel did not actually learn that his cipher had been broken during WW1 until the 1960s. A few years later, in 1968, Georges Painvin and Fritz Nebel, once opponents one half century ago, met in person to discuss their shared history. By this time, Nebel had stated that his original plan for the ADFGVX cipher involved a _double_ columnar transposition, but his superiors decided to go with the simpler single columnar transposition for practical purposes. In their meeting, Painvin admitted that, if the cipher had been implemented as originally planned, he surely would not have been able to crack it.

### So what exactly is double columnar transposition, and why is it so much more challenging to crack?

Double columnar transposition is just columnar transposition done two times. It can be done by using one key two times or by using two separate keys. Clearly, as it pertains to cryptographic complexity, this is the more appealing option.

But according to American historian David Kahn, the ADFGVX cipher was _already_ "the toughest field cipher the world had yet seen," so it's also fair to see why the Germans didn't think the extra complexity was necessary.

Unfortunately for the Germans, the French had, according to American cryptologist Herbert Yardley, "a first-rate analytical genius" named Georges Painvin, who "had a way of solving messages in code which resembled witchcraft."

![alt text](https://raw.githubusercontent.com/Stuycs-K/final-project-10-d-angelo-vincent-jha-lana/presentation_conclusion/data/painvin.png)

Although the ADFGVX cipher isn't remembered for being an incredibly powerful cipher, it still has its mark on history, as Painvin's work against it had major implications for the First World War. It's importance is perhaps best stated by Painvin's own words.

The following is a segment from David Kahn's _The Codebreakers – The Story of Secret Writing_:

![alt text](https://raw.githubusercontent.com/Stuycs-K/final-project-10-d-angelo-vincent-jha-lana/presentation_conclusion/data/kahn_paragraph.png)
