import simulation as net_sim


if __name__ == '__main__':
    sim = net_sim.simulation();
    
    x = int(input("Enter number of columns: "))
    y = int(input("Enter number of rows: "))
    devices = int(input("Enter number of devices: "))
    debug = str(input("Verbose? y/n: "))
    if debug == 'y':
        sim.set_verbose(True)
    elif debug == 'n':
        sim.set_verbose(False)
    else:
        print("Invalid input")
        exit()
    
    sim.start_simulation(x, y, devices);