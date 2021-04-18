#Initialize sınıfı
class InitSol(object):

    def __init__(self, n, myPRNG):
        self.n = n
        self.myPRNG = myPRNG

    # Tüm değerlerin 0 olarak set edilmesini sağlayan fonksiyon
    def zero_creator(self):
        x = list()
        x.append([0 for i in range(self.n)])
        return x