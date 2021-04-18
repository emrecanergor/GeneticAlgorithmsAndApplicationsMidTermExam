import itertools


class NeighborHood(object):

    def __init__(self, num_of_neighbor, random_gen):
        self.n = num_of_neighbor
        self.myPRNG = random_gen

    # One-flip Neighborhood - Tüm değerleri ters çevirir ve mahalle listesine ekler
    def one_flip_nbor(self, x):
        nbrhood = []
        for i in range(0, self.n):
            nbrhood.append(x[:])
            if nbrhood[i][i] == 1:
                nbrhood[i][i] = 0
            else:
                nbrhood[i][i] = 1
        return nbrhood

    # m-flip Neighborhood - iki biti birden çevirir.
    def m_flip_nbor(self, x, m):
        nbrhood = []
        for i, j in itertools.combinations(range(0, self.n), m):
            xtemp = x[:]
            if xtemp[i] == 1:
                xtemp[i] = 0
            else:
                xtemp[i] = 1
            if xtemp[j] == 1:
                xtemp[j] = 0
            else:
                xtemp[j] = 1
            nbrhood.append(xtemp)
        return nbrhood


    #  1-m-flip Neighborhood - önce one flip yapılır, sonra m kadar daha çevirilir. 
    def one_m_flip_nbor(self, x, m):
        nbrhood = []
        for i in range(0, self.n):
            nbrhood.append(x[:])
            if nbrhood[i][i] == 1:
                nbrhood[i][i] = 0
            else:
                nbrhood[i][i] = 1
            for v in range(self.myPRNG.randint(0,m)):
                randi = self.myPRNG.randint(0,23)
                if nbrhood[i][randi] == 1:
                    nbrhood[i][randi] = 0
                else:
                    nbrhood[i][randi] = 1
        return nbrhood

    # Rastgele seçimli 3 işleme bağlıdır => 1) swap, 2) add, 3) delete
    # Rastgele seçilen 2 konumun birbiri ile içerikleri takas edilir
    # Rastgele seçilen bir nesne eklenir
    # Rastgele seçilen bir nesne silinir
    # sad - swap, add or delete

    def sad_nbor(self, x, z):
        nbhood = []
        for i in range(0, self.n):
            for c in range(self.myPRNG.randint(1, z)):
                option = self.myPRNG.randint(0, 2)
                m = self.myPRNG.randint(0, 23)
                if option == 0:
                    o = self.myPRNG.randint(0, 23)
                    x[m], x[o] = x[o], x[m]
                elif option == 1:
                    x[m] = 1
                elif option == 2:
                    x[m] = 0
                nbhood.append(x)
        return nbhood