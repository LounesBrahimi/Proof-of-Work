import hashlib

def encode_entier_b(entier):
	return '{:032b}'.format(entier)

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
	
def hash_value(hash_ident, entier):
	m = hashlib.blake2b(digest_size=32)
	s = hash_ident+encode_entier_b(entier)
	m.update(str(s).encode('utf-8'))
	return m.hexdigest()
	
############################################################

def count_zero_prefix(data):
	cpt = 0
	for x in range(len(data)):
		if  data[x] == "0":
			cpt = cpt + 1
		else:
			break
	return cpt

def bin_format(integer, length):
    return f'{integer:0>{length}b}'

def encode_entier_256(entier):
	return bin_format(int(entier, 16), 256)
	
def is_valid(identite, nonce, n):
	hash = hash_value(identite, nonce)
	return count_zero_prefix(encode_entier_256(hash)) >= n
	
def mine(identite, n):
	nonce = 0
	for x in range(100000000):
		hash = hash_value(identite, x)
		if is_valid(identite, x, n):
			n = x
			break
		else:
			continue
	return n

	

#print(count_zero_prefix(encode_entier_b(123)))

#print(is_valid(hash_id("nakamoto", "satoshi"), 14460, 5))

#print(mine(hash_id("nakamoto", "satoshi"), 11))

#############################################################################

from base64 import b64decode, b64encode

etat = [("1dc653a1447946592fe2871eeb01d8fd6ae353bf04ab789199e38777da3fd0c7", 1003),
		 ("ad415c298389574a24f009671697dd58a717ec04aaa79bd39a130b1ae7a4b2a9", 8532),
		  ("b6a46ab620ab41132a7e062bee0bd7ef6af99d5c25b9021edcb949f2cd6c2bbc", 100),
		  ("d91340a0a4fc7283117fb7871a95e983455275347662345ffaaa75d674def6ec", 943),
		  ("ff9f179535d17c8f29d7eb8ad3432eb8b16ce684b48527b12a1a71f10d3e63ec", 755)]

def encode_compte(hash_ident, montant):
	m = hashlib.blake2b(digest_size=32)
	hash_entier = m.update(str(montant).encode('utf-8'))
	s = hash_ident+m.hexdigest()
	return s
	
def splite_string(s):
	chunks = [s[i:i+64] for i in range(0, len(s), 64)]
	return chunks[0]
	
def splite_string_2(s):
	chunks = [s[i:i+64] for i in range(0, len(s), 64)]
	return chunks
	
def splite_by_nombre_etats(s, n):
	chunks = [s[i:i+n] for i in range(0, len(s), n)]
	return chunks

def code_sans_nombre_etats(s):
	chunks = [s[i:i+8] for i in range(0, len(s), 8)]
	chunks.remove(chunks[0])
	str = ""
	for s1 in chunks:
		str = str + s1
	return str

def nombre_etats(s):
	chunks = [s[i:i+8] for i in range(0, len(s), 8)]
	return chunks[0]

def decode_compte(code):
	decodage = splite_string(code)
	return decodage

def encode_etat(etat):
	nombre = len(etat)
	code = ""
	max_length = 0
	for x in range(nombre):
		code1 = int(encode_compte(etat[x][0], etat[x][1]), 16)
		if  len(str(code1)) > max_length:
			max_length = len(str(code1))
	for x in range(nombre):
		code_x = str(int(encode_compte(etat[x][0], etat[x][1]), 16))
		while len(code_x) < 155:
			code_x = "0" + code_x
		code = code + code_x
	return str('{:08d}'.format(nombre))+ code

def decode_nem_compte(code):
	res = 0
	for x in range(100000000000):
		m = hashlib.blake2b(digest_size=32)
		m.update(str(x).encode('utf-8'))
		n = m.hexdigest()
		if n ==  code:
			res = x
			break
		else:
			continue
	return res
		
def decode_etat(code):
	nombre = int(nombre_etats(code))
	code = code_sans_nombre_etats(code)
	comptes = splite_by_nombre_etats(code, int(len(code)/nombre))
	original_comptes = []
	for x in range(nombre):
		code_nv = hex(int(comptes[x]))
		code_nv_nv = code_nv[:0] + code_nv[(1):]
		code_final = code_nv_nv[:0] + code_nv_nv[(1):]
		original_comptes.append(code_final)
	
	original_etat = []
	for x in range(nombre):
		decodage = splite_string_2(original_comptes[x])
		tuple = (decodage[0], decodage[1])
		original_etat.append(tuple)
		
	final_etat = []
	for x in range(nombre):
		num = decode_nem_compte(original_etat[x][1])
		tuple = (original_etat[x][0], num)
		final_etat.append(tuple)
	
	
	
	#print(original_etat)
	print("============")
	print(final_etat)
	print("============")
	return comptes
	



#print(encode_compte(etat[0][0], etat[0][1]))
print(encode_compte(etat[0][0], etat[0][1]))
print(encode_compte(etat[4][0], etat[4][1]))
print("#####################")
#print(decode_compte(encode_compte(etat[0][0], etat[0][1])))

#print(encode_entier_256("1dc653a1447946592fe2871eeb01d8fd6ae353bf04ab789199e38777da3fd0c7"))
#print(int(encode_entier_256("1dc653a1447946592fe2871eeb01d8fd6ae353bf04ab789199e38777da3fd0c7"), 2))

#print(encode_etat(etat))

#print(encode_etat(etat))
#print(decode_etat(encode_etat(etat)))

decode_etat(encode_etat(etat))
