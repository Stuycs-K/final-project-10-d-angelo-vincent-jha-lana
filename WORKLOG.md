# Work Log

## Vincent D'Angelo

### 5/22

Today I wrote the code for encoding a message using the ADFGVX cipher. The encoding algorithm requires the user to input their original message and two separate keys, which are used at different points in the process. There is still some testing I'd like to do with the code and some features I'm thinking of implementing (like exceptions), so I haven't merged the branch with main just yet.

### 5/23

Today I fixed a bug with my encoding program where duplicate characters in the second keyword were getting deleted. This was because Java’s TreeMap class does not allow for duplicate keys, but I fixed the error by modifying the characters of the keyword so that none were the same. I also researched the cipher's history, particularly how it was originally used and the key people involved, all information I plan to include in our presentation.

### 5/24

Began PRESENTATION.md today. I entered a lot of the information about the historical context surrounding the cipher, and played around with markdown, of course. There are some other parts of the history that I want to include, but I'll add those later in the presentation.

### 5/27

Today I continued my work on PRESENTATION.md. I explained how one uses the ADFGVX cipher to encode messages using images, tables, and footnotes, among another things. I also included a little bit more about the history the cipher in my explanation.

### 5/28

Today I mostly researched Georges Painvin, the man who broke the cipher, and read about how he did it and just generally about his life. I plan to include much of the information I researched today at the end of our presentation. I also added some much needed elaborating comments to the Encode.java file.

### 5/29

Today I wrote the conclusion part of our PRESENTATION.md, which was mostly historical. Now our presentation is almost completed; all that remains is the third section about how the cipher was broken.

### 5/30

I wrote the README file today, explaining our project as well as how to use our code. This definitely may be added to later. I also created the makefile and input all the java-relevant commands.

### 5/31

Today I changed my Encode program a bit so that it could properly handle spaces in the input. I also began drafting the TryHackMe room.

### 6/2

I finished writing the TryHackMe room this weekend. All I have to do is actually create the room and put everything I wrote in it. I also did some more testing, and noticed some apparent errors that we'll work on later this week.

### 6/3

I completed the entire TryHackMe room today. I also read over all our presentation and readme to make sure it all sounded good. I feel at this point we are wrapping up, and putting the finishing touches on everything before we record the video.

### 6/4

Day off today, so I just read through the TryHackMe room and edited it a bit.

### 6/5

Today I edited the README and added some further instructions for how to format the input when one tries to decode.

### 6/7 

Today was a big day for finishing touches. I read through PRESENTATION.md and fixed some spelling mistakes. I also added the TryHackMe room to the project officially, by adding a link to it in our README. I also created a references/resources section into the WORKLOG. 

## Lana Jha

### 5/22

Today I reviewed the decoding of the ADFGVX cipher and coded the first half of it. The decoder requires the encrypted message and two separate keys, which are used at two points in the process. I coded the part that uses the second key. I need to test more extensively before merging with main.

### 5/23

Today I tested the functions I coded yesterday and fixed syntax/logic issues including 2D arrays, lists, and strings. I also started the second half of the decoder, which utilizes a polybius square, represented by a 2D array, and the first key.

### 5/24

Today I finished decode. I fixed my issues with the 2D array and instead used a 1D array to represent the polybius square. I did the second half of the decoder with the first key and the code can now succesfully return the original message.

### 5/27

Today I did more research about the history and the cracking of the cipher and plan to start adding to the presentation.

### 5/28

Today I started the section on cracking the cipher for our presentation. I split the section into two parts: challenges and the process. I worked mostly on the challenges section.

### 5/29

Today I researched about how the cipher was actually cracked, but did not add to the presentation.

### 5/30

Today I finished the section of the presentation on how the cipher was cracked, and finalized both the challenges and the process parts of the section.

### 5/31

Today I added another section to the presentation on strengths and weaknesses of the cipher, merged all of my additions to the presentation on main, and tested out our makefile with our encode and decode files.

### 6/2

Today I tested out and tried to fix a bug that occured in decode, but I am not sure where the error has occured.

### 6/3

Today I fixed the error I was having yesterday with the polybius square, and I started working on another error with the columns.

### 6/4

Today I fixed the error I was working on yesterday with the columns. It had to do with a difference in the encoder and decoder when doing the columnar transposition, specifically with duplicate letters in the secondkey.

### 6/5 

Today I worked on writing the script that we will use in our presentation.

### 6/7

Today I cleaned up the code in the decode.py file and added comments to the functions.

# Resources/References
- _The American Black Chamber_ (1931) by Herbert Yardley
- _Secret History - The Story of Cryptology_ (2013) by Craig Bauer
- _The Codebreakers - The Story of Secret Writing_ (1967) by David Kahn
- [Chris Christensen from Northern Kentucky University](https://www.nku.edu/~christensen/1901cscmat483%20section%2012%20ADFGVX.pdf)
- [Cripto Corner](https://crypto.interactive-maths.com/adfgvx-cipher.html)
- [ADFGVX Cipher Decoder](https://www.dcode.fr/adfgvx-cipher)
