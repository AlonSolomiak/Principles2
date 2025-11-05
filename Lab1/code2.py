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


def print_table(A):
    extent = 0, len(A), 0, len(A[0])
    plt.imshow(A, cmap=plt.cm.plasma, interpolation='bicubic', extent=extent, origin='lower')
    plt.title("Targil 2")
    plt.colorbar(cmap='plasma', label='T[K]')
    plt.xlabel('X [cm]')
    plt.ylabel('y [cm]')
    plt.show()


def forward_diference(f1, f2, dx):
    return (f2-f1)/dx

def backward_diference(f0, f1, dx):
    return (f1-f0)/dx

def central_diference(f0, f2, dx):
    return (f2-f0)/(2*dx)

def find_flux_X(k, A):
    flux_X = [[] for row in range(len(A))]
    for i in range(len(A)):
        flux_X[i].append(-1 * k * forward_diference(A[i][0], A[i][1], dx))
        for j in range(1, len(A[i]) - 1):
            flux_X[i].append(-1 * k * central_diference(A[i][j-1], A[i][j+1], dx))
        flux_X[i].append(-1 * k * backward_diference(A[i][j-2], A[i][j-1], dx))

    return flux_X


def find_flux_Y(k,A):
    flux_Y = [[] for row in range(len(A))]
    for i in range(len(A[0])):
        print(flux_Y)
        flux_Y[0].append(-1 * k * forward_diference(A[0][i], A[1][i], dx))
        for j in range(1, len(A) - 1):
            flux_Y[j].append(-1 * k * central_diference(A[j-1][i], A[j+1][i], dx))
        flux_Y[len(A)-1].append(-1 * k * backward_diference(A[len(A)-2][i], A[len(A)-1][i], dx))

    return flux_Y



table = get_table_from_file()
print(table)
print(find_max(table))
print(find_min(table))
print_table(table)
Flux_x_table = find_flux_X(K, table)
print_table(Flux_x_table)
Flux_y_table = find_flux_Y(K, table)
print(Flux_y_table)
print_table(Flux_y_table)