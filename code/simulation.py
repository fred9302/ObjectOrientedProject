import psycopg2
from configparser import ConfigParser

class simulation:
    def __init__(self):
        self.dBconn = None
        self.clock = None
        self.grid = None
        self.verbose = None
        
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
    
    set_verbose = lambda self, new_verbose: setattr(self, 'verbose', new_verbose)
    """
    This code defines a lambda function called set_verbose that takes two parameters: self and new_verbose.
    
    It uses the setattr function to set the verbose attribute of the object self to the value of new_verbose.
    """
    
    def start_simulation(self, columns = 0, rows = 0):
        print('Starting simulation...')
        self.__create_grid(columns, rows, self.verbose)