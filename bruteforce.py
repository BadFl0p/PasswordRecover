from hasher import *
from termcolor import colored

def is_valid(guess, hash):
    if(guess == hash):
        return 1
    else:
        return 0
        

def get_hash_function(hashf):
    if(hashf == "md5"):
        return hash_with_md5
    elif(hashf == "sha1"):
        return hash_with_sha1
    elif(hashf == "sha224"):
        return hash_with_sha224
    elif(hashf == "sha256"):
        return hash_with_sha256
    elif(hashf == "sha512"):
        return hash_with_sha512
    else:
        return "Error"


def find_pwd_rec(guess, pwd, alphabet, length, max_length, hashf):
    if(length <= max_length):
        hash_func = get_hash_function(hashf)
        if hash_func == "Error":
            print("Error")
            quit()
        for c in alphabet:
            if(is_valid(hash_func(guess+c).hexdigest(), pwd)):
                print(colored("The password is : " + guess + c, 'green'))
                quit()
            else:
                print(colored("Trying next password...", 'red'))
                find_pwd_rec(guess+c, pwd, alphabet, length+1, max_length, hashf)


def get_alphabet(choice, pwd, max_length, hashf):
    lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    if(choice == "0"):
        find_pwd_rec("", pwd, nums, 1, max_length, hashf)
    elif(choice == "1"):
        find_pwd_rec("", pwd, lowercase, 1, max_length, hashf)
    elif(choice == "2"):
        find_pwd_rec("", pwd, uppercase, 1, max_length, hashf)
    elif(choice == "01" or choice == "10"):
        find_pwd_rec("", pwd, nums+lowercase, 1, max_length, hashf)
    elif(choice == "02" or choice == "20"):
        find_pwd_rec("", pwd, nums+uppercase, 1, max_length, hashf)
    elif(choice == "12" or choice == "21"):
        find_pwd_rec("", pwd, lowercase+uppercase, 1, max_length, hashf)
    else:
        print("Error")
        quit()


pwd = input("Enter your hash : ")
hashf = input("Enter the hash function used (md5, sha1, sha224, sha256, sha512) : ")
max_length = int(input("Enter the max length you wanna test : "))
alphabet_choice = input("Enter the alphabet you wanna test (0 for nums, 1 for lowercase, 2 for uppercase, 01 for nums and lowercase, 02 for nums and uppercase, 12 for lowercase and uppercase): ")

get_alphabet(alphabet_choice, pwd, max_length, hashf)

print(colored("The password couldn't be find.", 'red'))