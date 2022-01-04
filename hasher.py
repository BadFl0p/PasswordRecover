import hashlib

def hash_with_md5(string):
    hash = hashlib.md5()
    string = string.encode('utf-8')
    hash.update(string)
    return hash

def hash_with_sha1(string):
    hash = hashlib.sha1()
    string = string.encode('utf-8')
    hash.update(string)
    return hash

def hash_with_sha224(string):
    hash = hashlib.sha224()
    string = string.encode('utf-8')
    hash.update(string)
    return hash

def hash_with_sha256(string):
    hash = hashlib.sha256()
    string = string.encode('utf-8')
    hash.update(string)
    return hash

def hash_with_sha512(string):
    hash = hashlib.sha512()
    string = string.encode('utf-8')
    hash.update(string)
    return hash

def display_hash(hash):
    print(hash.hexdigest())
