import requests
from hasher import *
from termcolor import colored

def choose_hashf(hashf, string):
    if(hashf == "md5"):
        return hash_with_md5(string).hexdigest()
    elif(hashf == "sha1"):
        return hash_with_sha1(string).hexdigest()
    elif(hashf == "sha224"):
        return hash_with_sha224(string).hexdigest()
    elif(hashf == "sha256"):
        return hash_with_sha256(string).hexdigest()
    elif(hashf == "sha512"):
        return hash_with_sha512(string).hexdigest()
    else:
        return "Error"

uhash = input("Enter your hash : ")
hashf = input("Enter the hash function used (md5, sha1, sha224, sha256, sha512) : ")
pwd_list = requests.get("https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt").text
test_count = 1

for pwd in pwd_list.split("\n"):
    hash_guess = choose_hashf(hashf, pwd)
    if(hash_guess == "Error"):
        print("Wrong input")
        quit()

    if(hash_guess == uhash):
        print(colored("The password is : " + str(pwd), 'green'))
        quit()
    else:
        print(colored("[" + str(test_count) + "]" + "Trying next password...", 'red'))

    test_count += 1

print("Password isn't in the password list.")