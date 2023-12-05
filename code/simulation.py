class simulation:
    def __init__(self):
        self.dBconn = None
        self.clock = None
        self.grid = None
        self.verbose = None
        self.next_ip = 0
        
    def add_time(self, time = 0, print_time = False):
        """
        Adds the given time to the clock.

        Parameters:
            time (int): The amount of time to add to the clock. Default is 0.
            print_time (bool): Whether to print the current clock time after adding the given time. Default is False.

        Raises:
            Exception: If the given time is less than 0.

        Returns:
            None
        """
        if self.clock is None:
            self.clock = 0
        
        if time >= 0:
            self.clock += time
            if print_time is True:
                print(self.clock)
        else:    
            raise Exception('Time must be greater than or equal to 0')
      
    def __create_grid(self, cols = 0, rws = 0, print_grid = False):
        """
        Creates a grid of the given dimensions.

        Parameters:
            cols (int): The number of columns in the grid. Default is 0.
            rws (int): The number of rows in the grid. Default is 0.
            print_grid (bool): Whether to print the grid after creating it. Default is False.

        Raises:
            Exception: If the given rows or columns are less than 0.

        Returns:
            None
        """
        if rws >= 0 and cols >= 0:
            self.grid = [[0 for i in range(cols)] for j in range(rws)]
            if print_grid is True:
                print('Grid:')
                for i in range(rws):
                    print(self.grid[i])
        else:
            raise Exception('Rows and columns must be greater than or equal to 0')
    
    def get_ip(self):
        """
        Returns the next available IP address.
        """
        self.next_ip += 1
        return self.next_ip
    
    set_verbose = lambda self, new_verbose: setattr(self, 'verbose', new_verbose)
    """
    This code defines a lambda function called set_verbose that takes two parameters: self and new_verbose.
    
    It uses the setattr function to set the verbose attribute of the object self to the value of new_verbose.
    """
    
    def start_simulation(self, columns = 0, rows = 0):
        print('Starting simulation...')
        self.__create_grid(columns, rows, self.verbose)

class gui:
    def __init__(self):
        pass
    
    def add_node(self, node):
        pass
    
    def add_node(self, node):
        pass
    
    def show_information(self):
        pass

class network:
    def __init__(self):
        self.connections = []
        self.netmask = (255, 255, 255, 0)
        
class device:
    def __init__(self):
        self.ip = None
        
    def establish_connection(self, network):
        print('Establishing connection...')
        network.devices.append(self)
        print('Connection established.')
        
class node(device):
    def __init__(self):
        self.state = None
    

class gateway(device, network):
    def __init__(self):
        self.received_data = None
    
    def receive_data(self, data):
        """
        Set the received data attribute.
        
        Args:
            data: The data to be set as the received data attribute.
        
        Returns:
            None
        """
        self.received_data = data
