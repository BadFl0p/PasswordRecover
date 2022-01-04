from hasher import *

string = input("Enter your string : ")

hash = hash_with_md5(string)
display_hash(hash)
hash = hash_with_sha1(string)
display_hash(hash)
hash = hash_with_sha224(string)
display_hash(hash)
hash = hash_with_sha256(string)
display_hash(hash)
hash = hash_with_sha512(string)
display_hash(hash)
