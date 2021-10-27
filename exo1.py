import hashlib

def hash_id(nom, prenom):
	m = hashlib.blake2b(digest_size=32)
	s = nom+":"+prenom
	m.update(str(s).encode('utf-8'))
	return m.hexdigest()

def hash_blake2(s):
	m = hashlib.blake2b(digest_size=32)
	m.update(str(s).encode('utf-8'))
	return m.hexdigest()	
	
	
def encode_entier(entier):
	return '0x{0:08X}'.format(entier)

def encode_entier_b(entier):
	return '{:032b}'.format(entier)


def hash_value(hash_ident, entier):
	m = hashlib.blake2b(digest_size=32)
	s = hash_ident+encode_entier_b(entier)
	m.update(str(s).encode('utf-8'))
	return m.hexdigest()


#hash_id("nakamoto", "satoshi")

#print(encode_entier(123))

#print(hash_value(hash_id("nakamoto", "satoshi"), 123))
