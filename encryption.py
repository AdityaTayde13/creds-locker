from hashlib import sha256

def hashMaster(pass1):
   return sha256(pass1.encode('UTF-8')).hexdigest()




