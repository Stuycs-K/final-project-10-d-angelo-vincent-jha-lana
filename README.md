[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/ecp4su41)

# _VDALJH_'s ADFGVX Cipher

## Group Info

Team Members: **Vincent D'Angelo & Lana Jha**

Team Name: **VDALJH** (aka Short[er] NBA Point Guards[^1])

## Overview

Our project discusses the ADFGVX cipher, a cipher developed and utilized solely by the Germans during the First World War. In our presentation we will walk through the implementation of ADFGVX, as well as how it was eventually cracked and rendered insecure. Along the way, we'll discuss the historical context and cryptographic importance of the cipher. To accompany our presentation, we've created an encoder and decoder, and an accompanying TryHackMe room for our viewers to test their understanding.

[Presentation Video](https://drive.google.com/file/d/1OafsV-P2sRipV37MEipI77M_BSQEEydn/view?usp=sharing)  

[Presentation Slides](https://github.com/Stuycs-K/final-project-10-d-angelo-vincent-jha-lana/blob/main/PRESENTATION.mdhttps://github.com/Stuycs-K/final-project-10-d-angelo-vincent-jha-lana/blob/main/PRESENTATION.md)

## Instructions

The input for the ADFGVX cipher requires two keywords and one plaintext message. After cloning our repository, the following command will apply the cipher to the plaintext and print the ciphered text:

```
make encode ARGS="KEYWORD_1 KEYWORD_2 PLAINTEXT"
```

The following command will decode ciphered text using the two supplied keywords, and print out the plaintext:
```
make decode ARGS="KEYWORD_1 KEYWORD_2 'CIPHERTEXT'"
```
Note that the `CIPHERTEXT` has to be formatted with the separating spaces the encoding algorithm automatically adds.

Feeling confident? Test out your understanding of the cipher with this [TryHackMe room](https://tryhackme.com/jr/adfgvxcipher)!

[^1]: A quick explanation: Vincent's last name, D'Angelo, is the first name of a short[er] NBA point guard named D'Angelo Russell. Lana's last name, Jha, is the first name of a short[er] NBA point guard named J(h)a Morant.
