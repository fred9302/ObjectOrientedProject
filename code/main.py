import simulation as net_sim
import gui as net_gui

if __name__ == '__main__':
    sim = net_sim.simulation()
    gui = net_gui.gui()
    
    # input grid size
    x = int(input("Enter number of columns: "))
    y = int(input("\nEnter number of rows: "))
    grid_size = (x, y)
    
    # specify number of nodes
    if gui.no_nodes == 0:
        print("\nIgnoring number of nodes from GUI")
        devices = int(input("\nEnter number of devices: "))
    else:
        devices = gui.no_nodes
    
    # ask if verbose or not
    debug = str(input("\nVerbose? y/n: "))
    if debug == 'y':
        sim.set_verbose(True)
    elif debug == 'n':
        sim.set_verbose(False)
    else:
        exit("\nInvalid input")
    
    sim.start_simulation(grid_size, devices);