import gui

class simulation:
    def __init__(self):
        self.dBconn = None
        self.clock = None
        self.grid = None
        self.verbose = None
        self.next_ip = 0
        self.nodes = []
        
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
        if rws > 0 and cols > 0:
            self.grid = [[0 for i in range(cols)] for j in range(rws)]
            if print_grid is True:
                print('Grid:')
                for i in range(rws):
                    print(self.grid[i])
        else:
            print('Rows and columns must be greater than 0')
    
    def __get_next_ip(self):
        """
        Iterates next_ip and returns the next available IP address.
        """
        self.next_ip += 1
        return self.next_ip
    
    def __get_ip(self):
        """
        Returns the value of variable next_ip which is the next available IP address.
        """
        return self.next_ip
    
    set_verbose = lambda self, new_verbose: setattr(self, 'verbose', new_verbose)
    """
    This code defines a lambda function called set_verbose that takes two parameters: self and new_verbose.
    
    It uses the setattr function to set the verbose attribute of the object self to the value of new_verbose.
    """
    
    def start_simulation(self, grid = (0, 0), connections = 0):
        print('Starting simulation...')
        self.__create_grid(grid[0], grid[1], self.verbose)
        
        # create gateway
        net = gateway()
        net.set_ip(self.__get_next_ip())
        if self.verbose == True:
            print(f"Gateway with IP {net.get_ip()} has been created")
        
        # establish connections with nodes
        for i in range(connections):
            net.connect(ip = self.__get_next_ip())
            self.nodes.append(node())
            self.nodes[i].set_ip(self.__get_ip())
            if self.verbose == True:
                print(f"Node {i} with IP {self.nodes[i].get_ip()} is connected to the gateway with IP {net.get_ip()}")

class network:
    def __init__(self):
        self.connections = []
        self.netmask = (255, 255, 255, 0)
    
    def connect(self, ip = None): # if this method is called from simulation method sim must be self
        self.connections.append(ip)
        
class device:
    def __init__(self):
        self.ip = None
        self.position = None
        
    """ def establish_connection(self, network):
        print('Establishing connection...')
        network.devices.append(self)
        print('Connection established.') """
    
    def set_ip(self, ip = None):
        """
        Sets the IP address for the object.

        Parameters:
            ip (int): The last number of the IP address to be set. If not provided, no IP address will be set.

        Returns:
            None
        """
        if ip is not None:
            self.ip = ip
        else:
            print('No IP address provided.')
    
    def get_ip(self):
        """
        Get the IP address.

        Returns:
            str: The IP address.
        """
        return self.ip
    
    def set_position(self, position = None):
        """
        Sets the position of the object.

        Parameters:
            position (tuple): The position to be set. If not provided, no position will be set.

        Returns:
            None
        """
        if position is not None:
            self.position = position
        else:
            print('No position provided.')
            
    def get_position(self):
        """
        Get the position of the object.

        Returns:
            tuple: The position of the object.
        """
        return self.position
    
class node(device):
    def __init__(self):
        super().__init__()
        self.state = None
        
    def set_state(self, state = False):
        """
        Set the state of the object to the given state.

        Parameters:
            state (any): The new state to set.

        Returns:
            None
        """
        self.state = state
    
    def get_state(self):
        """
        Get the current state of the object.
        
        Returns:
            The current state of the object.
        """
        return self.state
    

class gateway(network, device):
    def __init__(self):
        super(network, device).__init__()
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
