import matplotlib.pyplot as plt
import numpy as np
import math
#V = L^d, where V is volume of the lattice, L is the length of the Lattice, and d is the dimensions
#L = 10, d = 2
# x subscript k = {0, 1, 0, .....}
# E subscript k = Sum[psubisuperk * psubjsuperk * epsilonAA]
# i.e. the energy of the lattice = sum of all the interactions
# epsilonAA = epsilonBB = 0, epsilonAB = epsilonBA = 1
# 10^5 runs per step of 0.1 from 4.0T to 0.1T

def boundary_function(array,i,j,E):
    something = [1,2,3,4,5,6,7,8]
    E = 0
    if i == 0 and j == 0: # NW Corner
        if array[i,j] != array[i,9]:
            E = E + 1
        if array[i,j] != array[i,j+1]:
            E = E + 1
        if array[i,j] != array[i+1,j]:
            E = E + 1
        if array[i,j] != array[9,j]:
            E = E + 1
    elif i == 0 and j == 9: # NE Corner
        if array[i,j] != array[i,j-1]:
            E = E + 1
        if array[i,j] != array[i,0]:
            E = E + 1
        if array[i,j] != array[i+1,j]:
            E = E + 1
        if array[i,j] != array[9,j]:
            E = E + 1
    elif i == 9 and j == 0: # SW Corner
        if array[i,j] != array[i,9]:
            E = E + 1
        if array[i,j] != array[i,j+1]:
            E = E + 1
        if array[i,j] != array[0,j]:
            E = E + 1
        if array[i,j] != array[i-1,j]:
            E = E + 1
    elif i == 9 and j == 9: # SE Corner
        if array[i,j] != array[i,j-1]:
            E = E + 1
        if array[i,j] != array[i,0]:
            E = E + 1
        if array[i,j] != array[0,j]:
            E = E + 1
        if array[i,j] != array[i-1,j]:
            E = E + 1
    elif i == 0 and j in something: # North Side
        if array[i,j] != array[i,j-1]:
            E = E + 1
        if array[i,j] != array[i,j+1]:
            E = E + 1
        if array[i,j] != array[i+1,j]:
            E = E + 1
        if array[i,j] != array[9,j]:
            E = E + 1
    elif i == 9 and j in something: # South Side
        if array[i,j] != array[i,j-1]:
            E = E + 1
        if array[i,j] != array[i,j+1]:
            E = E + 1
        if array[i,j] != array[0,j]:
            E = E + 1
        if array[i,j] != array[i-1,j]:
            E = E + 1
    elif i in something and j == 0: # West Side
        if array[i,j] != array[i,9]:
            E = E + 1
        if array[i,j] != array[i,j+1]:
            E = E + 1
        if array[i,j] != array[i+1,j]:
            E = E + 1
        if array[i,j] != array[i-1,j]:
            E = E + 1
    elif i in something and j == 9: # East Side
        if array[i,j] != array[i,j-1]:
            E = E + 1
        if array[i,j] != array[i,0]:
            E = E + 1
        if array[i,j] != array[i+1,j]:
            E = E + 1
        if array[i,j] != array[i-1,j]:
            E = E + 1
    else:                           # Everywhere else
        if array[i,j] != array[i,j-1]:
            E = E + 1
        if array[i,j] != array[i,j+1]:
            E = E + 1
        if array[i,j] != array[i+1,j]:
            E = E + 1
        if array[i,j] != array[i-1,j]:
            E = E + 1
    return E
    
def swapPosition(array,i0,j0,i1,j1):
    x2 = np.copy(array)
    if x2[i0, j0] == x2[i1, j1]:
        return x2
    elif x2[i0, j0] == 1 and x2[i1, j1] == 0:
        x2[i0, j0] = 0
        x2[i1, j1] = 1
        return x2
    elif x2[i0, j0] == 0 and x2[i1, j1] == 1:
        x2[i0, j0] = 1
        x2[i1, j1] = 0
        return x2

def energy_sum(array):
    E = 0
    for i in range(10):
        for j in range(10):
            E = E + boundary_function(array,i,j,0)
    return E

def whole_code(temp):
    x1 = np.arange(100)                 # Create a list with from 0 to 99
    np.random.shuffle(x1)               # Randomly shuffle the list
    x1 = x1.reshape((10,10))            # Transform the list into a 2D array
    for i in range(10):                 # Modulo every element by 2 to give either 0 or 1
        for j in range(10):
            x1[i,j] = (x1[i,j])%2
    x = []                              # Create an empty list for elements in the x and y axis
    y = []
    Esum = energy_sum(x1)
    for n in range(100000):
        i0 = np.random.choice(10)
        j0 = np.random.choice(10)
        i1 = np.random.choice(10)
        j1 = np.random.choice(10)
        x2 = swapPosition(x1,i0,j0,i1,j1)
        deltaEsite = (boundary_function(x2,i0,j0,0) + boundary_function(x2,i1,j1,0)) - (boundary_function(x1,i0,j0,0) + boundary_function(x1,i1,j1,0))
        r = np.random.uniform(low=0.0, high=1.0, size=None)
        rcompare = math.exp((-deltaEsite)/(1*temp))
        if deltaEsite < 0 or r < rcompare:
            x1 = np.copy(x2)
            y.insert(n,Esum + deltaEsite)
            x2 = np.empty([10,10])
            x.append(n)
            Esum = Esum + deltaEsite
        else:
            x.append(n)
            y.insert(n,Esum)
    avg_energy_sum = 0
    squared_energy_sum = 0
    for n in range(100000):
        avg_energy_sum = avg_energy_sum + y[n]
        squared_energy_sum = squared_energy_sum + (y[n])**2
    average_energy = avg_energy_sum/100000
    average_squared_energy = squared_energy_sum/100000
    plt.figure(1)
    plt.imshow(x1)
    plt.title('Particle Interaction at the end of the runs at T = ' + str(temp))
    print(x1)
    print('Average Energy for T = ' + str(temp) + ' is ' + str(average_energy))
    print('Average of Energy Squared = ' + str(average_squared_energy))
    return x, y

def temperature_step():
    for T in range(1,41):
        T = float(T)/10
        x, y = whole_code(T)
        plt.figure(2)
        plt.plot(x,y)
        plt.title('Regular Solution Model at T =' + str(T))
        plt.xlabel('Run number')
        plt.ylabel('Sum of energy interaction')
        plt.show()

temperature_step()