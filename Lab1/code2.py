import matplotlib.pyplot as plt
dx = 0.01
K = 5

def get_table_from_file():
    with open("C:\\Users\\tkuis\\Documents\\Github\\Princples2\\Principles2\\Lab1\\temp_2D_hw.txt", "r") as f:
        return [[float(num) for num in line.split(" ")] for line in f]

def find_max(table):
    max = table[0][0]
    for i in range(len(table)):
        for j in range(len(table[i])):
            if table[i][j] > max:
                max = table[i][j]
    
    return max

def find_min(table):
    min = table[0][0]
    for i in range(len(table)):
        for j in range(len(table[i])):
            if table[i][j] < min:
                min = table[i][j]
    
    return min

def print_table(A, title, xlabel, ylabel, label):
    extent = 0, len(A)-1, 0, len(A[0])-1
    plt.imshow(A, cmap=plt.cm.plasma, interpolation='bicubic', extent=extent, origin='lower')
    plt.title(title)
    plt.colorbar(cmap='plasma', label=label)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

def forward_diference(f1, f2, dx):
    return (f2-f1)/dx

def backward_diference(f0, f1, dx):
    return (f1-f0)/dx

def central_diference(f0, f2, dx):
    return (f2-f0)/(2*dx)

def find_flux_X(k, table):
    flux_X = [[] for row in range(len(table))]
    for row in range(len(table)):
        flux_X[row].append(-1 * k * forward_diference(table[row][0], table[row][1], dx))
        for col in range(1, len(table[row]) - 1):
            flux_X[row].append(-1 * k * central_diference(table[row][col-1], table[row][col+1], dx))
        flux_X[row].append(-1 * k * backward_diference(table[row][len(table[row])-2], table[row][len(table[row])-1], dx))

    return flux_X

def find_flux_Y(k,table):
    flux_Y = [[] for row in range(len(table))]
    for col in range(len(table[0])):
        flux_Y[0].append(-1 * k * forward_diference(table[0][col], table[1][col], dx))
        for row in range(1, len(table) - 1):
            flux_Y[row].append(-1 * k * central_diference(table[row-1][col], table[row+1][col], dx))
        flux_Y[len(table)-1].append(-1 * k * backward_diference(table[len(table)-2][col], table[len(table)-1][col], dx))

    return flux_Y



T_table = get_table_from_file()
print("Max T: " + str(find_max(T_table)))
print("Min T: " + str(find_min(T_table)))
print_table(T_table, "Temprature Distribution", "X [cm]", "Y [cm]", "T [K]")
Flux_x_table = find_flux_X(K, T_table)
print_table(Flux_x_table, "Distribution of Heat Flux in X direction", "X [cm]", "Y [cm]", "Flux X [W/m^2]")
Flux_y_table = find_flux_Y(K, T_table)
print_table(Flux_y_table, "Distribution of Heat Flux in Y direction", "X [cm]", "Y [cm]", "Flux Y [W/m^2]")
print("Max Flux X: " + str(find_max(Flux_x_table)))
print("Min Flux X: " + str(find_min(Flux_x_table)))
print("Max Flux Y: " + str(find_max(Flux_y_table)))
print("Min Flux Y: " + str(find_min(Flux_y_table)))