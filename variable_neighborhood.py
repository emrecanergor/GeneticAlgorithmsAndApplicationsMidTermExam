from random import Random
import numpy as np
from NeighborHood import NeighborHood
from InitSol import InitSol
from Evaluate import Evaluate
from StoppingCriteria import StoppingCriteria

seed = 5113
myPRNG = Random(seed)
n = 24

#değerler
value =  [825594, 1677009,1676628,1523970, 943972,  97426,  69666,1296457,1679693,1902996,1844992,1049289,1252836,1319836, 953277,2067538, 675367, 853655,1826027,  65731, 901489, 577243, 466257, 369261]
#ağırlıklar
weights = [382745,799601,909247,729069,467902, 44328, 34610,698150,823460,903959,853665,551830,610856,670702,488960,951111,323046,446298,931161, 31385,496951,264724,224916,169684]
#max kapasite
max_weight = 6404180
solutionsChecked = 0
nbor = NeighborHood(n, myPRNG)
ini_sol = InitSol(n, myPRNG)
e = Evaluate(value, weights, max_weight)
stop = StoppingCriteria(iterations=50)

solutionsChecked = 0
x_curr = ini_sol.zero_creator()[0]
x_best = x_curr[:]
f_curr = e.evaluate(x_curr)
f_best = f_curr[:]
done = 0
k = 1

while done == 0:
    k = 1
    while k < 4:
        if k == 1:
            Neighborhood = nbor.one_flip_nbor(x_curr)
        elif k == 2:
            Neighborhood = nbor.one_m_flip_nbor(x_curr, 4)
        elif k == 3:
            Neighborhood = nbor.sad_nbor(x_curr, 6)
        else:
            NeighborHood = nbor.m_flip_nbor(x_curr, 2)
        s = myPRNG.choice(Neighborhood)
        solutionsChecked += 1
        if e.evaluate(s)[0] > f_best[0]:
            x_best = s[:]
            f_best = e.evaluate(s)[:]
            k = 1
        if stop.stop_stagnation(f_best):
            done = 1
            k = 5
        else:
            x_curr = x_best[:]
            f_curr = f_best[:]
            k += 1
            print("\nKontrol edilen çözüm sayısı: ", solutionsChecked)
            print("Bulunan en iyi uzaklık: ", f_best)

print("\nEn son kontrol edilen çözüm: ", solutionsChecked)
print("Bulunan en iyi değer: ", f_best[0])
print("Ağırlığı: ", f_best[1])

print("-------------------------------------------------------------------")

print("\nToplam Seçilen Nesne Sayısı: ", np.sum(x_best))
print("En iyi çözüm: ", x_best)