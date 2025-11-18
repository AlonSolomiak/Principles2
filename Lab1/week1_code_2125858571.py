import matplotlib.pyplot as plt
dx = 0.01
K = 5
path = "C:\\Users\\tkuis\\Documents\\Github\\Princples2\\Principles2\\Lab1\\"

# Section a
def get_table_from_file():
    with open(path + "temp_2D_hw.txt", "r") as f:
        return [[float(num) for num in line.split(" ")] for line in f]

# Section b
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

# Section c
def print_table(A, title, xlabel, ylabel, label):
    extent = 0, len(A)-1, 0, len(A[0])-1
    plt.imshow(A, cmap=plt.cm.plasma, interpolation='bicubic', extent=extent, origin='lower')
    plt.title(title)
    plt.colorbar(cmap='plasma', label=label)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

# Section d
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

# Section e
def print_plots(Xs, Ys, titles, xlabels, ylabels):

    fig, axes = plt.subplots(len(Xs), 1)

    for i in range(len(Xs)):
        axes[i].plot(Xs[i], Ys[i])
        axes[i].set_title(titles[i])
        axes[i].set_xlabel(xlabels[i])
        axes[i].set_ylabel(ylabels[i])

    plt.tight_layout()
    plt.show()

def create_file(path, table):
    with open(path, "w") as f:
        for row in table:
            for value in row:
                f.write(str(value) + " ")
            f.write("\n")

# Section f
def caclulate_heat_flowrate_per_width(flux_table, row):
    Q_dot_per_width = 0
    for col in range(len(flux_table[row])):
        Q_dot_per_width += flux_table[row][col] * dx
    return Q_dot_per_width


def main():
    T_table = get_table_from_file()
    print("////section b////")
    print("min temp: " + str(find_min(T_table)))
    print("max temp: " + str(find_max(T_table)))
    print_table(T_table, "Temprature Distribution", "X [cm]", "Y [cm]", "T [K]")
    Flux_x_table = find_flux_X(K, T_table)
    print_table(Flux_x_table, "Distribution of Heat Flux in X direction", "X [cm]", "Y [cm]", "Flux X [W/m^2]")
    Flux_y_table = find_flux_Y(K, T_table)
    print_table(Flux_y_table, "Distribution of Heat Flux in Y direction", "X [cm]", "Y [cm]", "Flux Y [W/m^2]")
    print("////section d////")
    print("max q''x: " + str(find_max(Flux_x_table)))
    print("min q''x: " + str(find_min(Flux_x_table)))
    print("max q''y: " + str(find_max(Flux_y_table)))
    print("min q''y: " + str(find_min(Flux_y_table)))
    print_plots([range(len(T_table[7])), range(len(Flux_y_table[7]))],
                [T_table[7], Flux_y_table[7]],
                ["Temperature as a Function of x on y=7cm", "q''y as a Function of x on y=7cm"],
                ["x [cm]", "x [cm]"],
                ["T [K]", "q''y [W/m^2]"])
    create_file(path + "tempY7.txt", [range(len(T_table[7])), T_table[7]])
    create_file(path + "YfluxY7.txt", [range(len(Flux_y_table[7])), Flux_y_table[7]])
    print("////section f////")
    print("total heat flowrate per unit width via y = 0.07 m is " + str(caclulate_heat_flowrate_per_width(Flux_y_table, 6)) + " W/m")

if __name__ == "__main__":
    main()