def sha(data):
    import hashlib
    s = hashlib.sha1()
    
    s.update(data.encode("utf-8"))
    h = s.hexdigest()
    return h