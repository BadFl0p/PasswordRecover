# Password Recover coded in Python

## Intro

<br>The goal for this project was to take the theoretical knowledge I had on cracking hashes and trying to code the process by myself. This project doesn't use any multithreading or advance knowledge, I kept everything very simple just to see how I would code the knowledge I had.<br><br>

## Computing hashes<br>
The first thing I needed to do was hashing any input. This is what I've done in ***hasher.py***
<br>
To do so I used the library **hashlib**.
<br><br>

### The hash functions implemented are :
- *md5*<br>
- *sha1*<br>
- *sha224*<br>
- *sha256*<br>
- *sha512*<br>

<br>

## Performing a wordlist attack
<br>
The first implementation I made was a wordlist attack. For this I used a wordlist available online, taking only one million passwords.

The goal here was to get which hash function to use, then get each word in the list, hash it with the hash function specified before and compare the obtained hash to the one given by the user.

The code made for this is in ***wordlist.py***, I just reused the functions in ***hasher.py*** to compute each hash.
<br><br>

## Performing a bruteforce attack
<br>
After the wordlist attack I wanted to try implementing a bruteforce attack.<br>
Now the goal was to to get the hash function used, compute each combinaison for a given length and alphabet, then hash each combinaison and compare it to the hash given by the user at the start of the program.

This implementation is done in ***bruteforce.py***, I also used the functions in ***hasher.py*** to compute each hash.<br><br>

### Alphabets available :<br>
- Lowercases
- Uppercases
- Numbers