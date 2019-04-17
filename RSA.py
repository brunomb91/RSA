import random

class RSA:
    """RSA cryptography implementation."""
    def __init__():
        __p = random.choice(self.prime_numbers_until_n())
	__q = random.choice(self.prime_numbers_until_n())
	__n = 0
        __chave_encrypt = ()
        __chave_decrypt = ()

         
    def setup(self):
        __n = __p * __q
	phi = lambda n: n - 1
        n1 = random.randint(1, 11)
        
        c = phi(__p) * phi(__q)

        if gcd(n1, c) != 1:
            while gcd(n1, __c) != 1:
                n1 = random.randint(1, 11)

         __chave_encrypt = list(__chave_encrypt)
         __chave_decrypt = list(__chave_decrypt)

         __chave_encrypt.append(__n)
         __chave_encrypt.append(n1)
         __chave_encrypt = tuple(__chave_encrypt)
         
         __chave_decrypt.append(__n)
	 __chave_decrypy.append(decrypt_value(c, n1))
	 __chave_decrypt = tuple(__chave_decrypt)
        	
    def prime_numbers_until_n(self, n=1000):
        l = []
        for i in range(1,n):
            c = 0
            for j in range(1,i):
                if i % j == 0:
                    c += 1
        if c == 1:
            l.append(i)
        
	return l

    def gcd(self, a, b):
	if a % b == 0:
	    return b
	
	gcd = a % b
	while a % b != 0:
	    a = b
	    b = gcd
	    gcd = a % b
        
	return b
    
    def decrypt_value(self, phi_n, c):
        d = 0	
	while (d * c) % phi_n != 1:
	    d += 1
	
	return d    

    def encrypt(self, msg):
        pre_cod = [(ord(x) + 100) for x in msg]
        pre_cod = ''.join(pre_cod)
	
	
	
    def decrypt(self, msg):
        

