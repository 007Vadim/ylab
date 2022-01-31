import numpy as np
from python_tsp.exact import solve_tsp_dynamic_programming
a=[(0,2),(5,2),(8,3),(2,5),(6,6)]
resul = [[0 if i == j else ((a[j][0] - a[i][0]) ** 2 + (a[j][1] - a[i][1]) ** 2) ** 0.5 for j in range(len(a))] for i in range(len(a))]
distance_matrix = np.array(resul)
permutation, distance = solve_tsp_dynamic_programming(distance_matrix)
s = 0
r=''
for i in range(1,len(permutation)):
    s+=((a[permutation[i]][0] - a[permutation[i-1]][0]) ** 2 + (a[permutation[i]][1] - a[permutation[i-1]][1]) ** 2) ** 0.5
        #print(a[permutation[i-1]], a[permutation[i]])
        #print([((a[permutation[i]][0] - a[permutation[i-1]][0]) ** 2 + (a[permutation[i]][1] - a[permutation[i-1]][1]) ** 2) ** 0.5])
    if i == 1:
        r+=str(a[0])+ ' -> ' +f'{str(a[permutation[i]])}' + f'{[s]}' + ' -> '
    elif i != 4:
        r+=(f'{a[permutation[i]]}' + f'{[s]}'+ ' -> ')
    else:
        r+=(f'{a[permutation[i]]}' + f'{[s]}' + ' -> ')
s+=((a[permutation[4]][0] - a[permutation[0]][0]) ** 2 + (a[permutation[4]][1] - a[permutation[0]][1]) ** 2) ** 0.5
print(r + str(a[0]) + str(s) + f' = {s}')
