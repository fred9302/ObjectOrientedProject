import simulation as netSim


if __name__ == '__main__':
    x = int(input("Enter number of columns: "))
    y = int(input("Enter number of rows: "))
    debug = str(input("Verbose ? y/n: "))
    if debug == 'y':
        debug = True
    elif debug == 'n':
        debug = False
    else:
        print("Invalid input")
        exit()
        
    
    sim = netSim.simulation();
    sim.start_simulation(x, y, debug);