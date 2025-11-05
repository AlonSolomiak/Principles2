import matplotlib.pyplot as plt
dx = 0.01
K = 5

def get_table_from_file():
    with open("C:\\Users\\tkuis\\Documents\\Github\\Princples2\\Principles2\\Lab1\\temp_2D.txt", "r") as f:
        return [[float(num) for num in line.split(" ")] for line in f]

def find_max(A):
    max = A[0][0]
    for i in range(len(A)):
        for j in range(len(A[i])):
            if A[i][j] > max:
                max = A[i][j]
    
    return max

def find_min(A):
    min = A[0][0]
    for i in range(len(A)):
        for j in range(len(A[i])):
            if A[i][j] < min:
                min = A[i][j]
    
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

def find_flux_X(k, A):
    flux_X = [[] for row in range(len(A))]
    for row in range(len(A)):
        flux_X[row].append(-1 * k * forward_diference(A[row][0], A[row][1], dx))
        for col in range(1, len(A[row]) - 1):
            flux_X[row].append(-1 * k * central_diference(A[row][col-1], A[row][col+1], dx))
        flux_X[row].append(-1 * k * backward_diference(A[row][len(A[row])-2], A[row][len(A[row])-1], dx))

    return flux_X

def find_flux_Y(k,A):
    flux_Y = [[] for row in range(len(A))]
    for col in range(len(A[0])):
        flux_Y[0].append(-1 * k * forward_diference(A[0][col], A[1][col], dx))
        for row in range(1, len(A) - 1):
            flux_Y[row].append(-1 * k * central_diference(A[row-1][col], A[row+1][col], dx))
        flux_Y[len(A)-1].append(-1 * k * backward_diference(A[len(A)-2][col], A[len(A)-1][col], dx))

    return flux_Y



T_table = get_table_from_file()
print("Max T: " + str(find_max(T_table)))
print("Min T: " + str(find_min(T_table)))
print_table(T_table, "Section C - Temprature Distribution", "X (cm)", "Y (cm)", "T [K]")
Flux_x_table = find_flux_X(K, T_table)
print_table(Flux_x_table, "Section D - Distribution of Heat Flux in X direction", "X (cm)", "Y (cm)", "Flux_x [W/m^2]")
Flux_y_table = find_flux_Y(K, T_table)
print_table(Flux_y_table, "Section D - Distribution of Heat Flux in Y direction", "X (cm)", "Y (cm)", "Flux_y [W/m^2]")
print("Max Flux X: " + str(find_max(Flux_x_table)))
print("Min Flux X: " + str(find_min(Flux_x_table)))
print("Max Flux Y: " + str(find_max(Flux_y_table)))
print("Min Flux Y: " + str(find_min(Flux_y_table)))