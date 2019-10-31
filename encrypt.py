import hashlib

def sha(data):
    s = hashlib.sha1()
    s.update(data.encode('utf-8'))
    return s.hexdigest() 
