import random

class RSA:
    """RSA cryptography implementation."""
    def __init__(self):
        # __p = random.choice(self.prime_numbers_until_n())
	# __q = random.choice(self.prime_numbers_until_n())
        self.__p = 97
        self.__q = 53
        self.n = 0
        self.__chave_encrypt = ()
        self.__chave_decrypt = ()
        self.cod = []
        self.decod = []
         
    def setup(self):
        self.n = self.__p * self.__q
        phi = lambda n: n - 1
        # n1 = random.randint(1, 11)
        n1 = 7
        
        c = phi(self.__p) * phi(self.__q)

        if self.gcd(n1, c) != 1:
            while gcd(n1, self.__c) != 1:
                n1 = random.randint(1, 11)

        self.__chave_encrypt = list(self.__chave_encrypt)
        self.__chave_decrypt = list(self.__chave_decrypt)

        self.__chave_encrypt.append(self.n)
        self.__chave_encrypt.append(n1)
        self.__chave_encrypt = tuple(self.__chave_encrypt)
         
        self.__chave_decrypt.append(self.n)
        self.__chave_decrypt.append(self.decrypt_value(c, n1))
        self.__chave_decrypt = tuple(self.__chave_decrypt)
        	
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
        pre_cod = [str(ord(x) + 100) for x in msg]
        pre_cod = ''.join(pre_cod)
        l = []
        
        # inicio = 0
        # fim = inicio + random.randint(2, 4)
        tam = len(pre_cod) 
        
        while len(l) != 10:
            l = []
            inicio = 0
            fim = inicio + random.randint(2, 4)
            while fim <= tam:
                l.append(pre_cod[inicio:fim])
                inicio = fim
                fim = inicio + random.randint(2, 4)
        
        cod = [((int(i)**self.__chave_encrypt[1]) % self.__chave_encrypt[0]) for i in l]    
        cod = [str(i) for i in cod]
        cod = '#'.join(cod)
        return cod
        
	
    def decrypt(self, msg):
        msg = msg.split('#')
        l1 = []
        
        for i in msg:
            l1.append(((int(i)**self.__chave_decrypt[1]) % self.__chave_decrypt[0]))
	
        l1 = [str(i) for i in l1]
        l1 = ''.join(l1)
        tam = len(l1)
        inicio = 0
        fim = inicio + 3
	
        while fim <= tam:
            self.decod.append(l1[inicio:fim])
            inicio = fim
            fim = inicio + 3
	
        self.decod = [chr(int(i) - 100) for i in self.decod if int(i) <= 190 or int(i) >= 132]
        self.decod = ''.join(self.decod)
        
        return self.decod

    def main():
        rsa = RSA()
        rsa.setup()
        """
	4617#2017#1635#1053#32#2541#3675#4422#3526#283
	""" 
        msg = 'I LOVE YOU'
        msg2 = rsa.encrypt(msg)

        print(msg2)

        print(rsa.decrypt(msg2))

if __name__ == '__main__':
    RSA.main()
