import simulation as netSim


if __name__ == '__main__':
    x = int(input("Enter number of columns: "))
    y = int(input("Enter number of rows: "))
    sim = netSim.simulation();
    sim.start_simulation(x, y);