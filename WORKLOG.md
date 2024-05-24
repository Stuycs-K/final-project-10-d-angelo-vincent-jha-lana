# Work Log

## Vincent D'Angelo

### 5/22

Today I wrote the code for encoding a message using the ADFGVX cipher. The encoding algorithm requires the user to input their original message and two separate keys, which are used at different points in the process. There is still some testing I'd like to do with the code and some features I'm thinking of implementing (like exceptions), so I haven't merged the branch with main just yet.

### 5/23

Today I fixed a bug with my encoding program where duplicate characters in the second keyword were getting deleted. This was because Java’s TreeMap class does not allow for duplicate keys, but I fixed the error by modifying the characters of the keyword so that none were the same. I also researched the cipher's history, particularly how it was originally used and the key people involved, all information I plan to include in our presentation. 


## Lana Jha

### 5/22

Today, I reviewed the decoding of the ADFGVX cipher and coded the first half of it. The decoder requires the encrypted message and two separate keys, which are used at two points in the process. I coded the part that uses the second key. I need to test more extensively before merging with main.

### date y

info
