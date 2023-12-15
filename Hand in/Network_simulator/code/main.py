import simulation as net_sim
import gui as net_gui

if __name__ == '__main__':
    sim = net_sim.simulation()
    gui = net_gui.gui()
    
    toggle_gui = str(input("\nUse GUI? y/n: "))
    if toggle_gui == 'y':
        print("\nStarting GUI...\n")
        gui.set_toggle_gui(True)
    elif toggle_gui == 'n':
        print("\nIgnoring GUI...\n")
        gui.set_toggle_gui(False)
    else:
        exit("\nInvalid input")
        
    if gui.get_toggle_gui() == True:
        gui.set_simulation(sim)
        gui.start_gui()
    
    else:
        # input grid size
        x = int(input("Enter number of columns: "))
        y = int(input("\nEnter number of rows: "))
        grid_size = (x, y)
        
        # specify number of nodes
        devices = int(input("\nEnter number of devices: "))
        
        # ask if verbose or not
        debug = str(input("\nVerbose? y/n: "))
        if debug == 'y':
            sim.set_verbose(True)
        elif debug == 'n':
            sim.set_verbose(False)
        else:
            exit("\nInvalid input")
        
        sim.start_simulation(grid_size, devices);