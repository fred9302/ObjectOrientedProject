import pywebio
#from simulation import simulation

class gui:
    def __init__(self):
        self.devices = 0
        self.grid_size = [0, 0]
        self.toggle_gui = None
        self.sim = None
    
    set_gui = lambda self, new_gui: setattr(self, 'toggle_gui', new_gui)
    """
    This code defines a lambda function called set_gui that takes two parameters: self and new_gui.
    
    It uses the setattr function to set the verbose attribute of the object self to the value of new_verbose.
    """
    
    def add_node(self):
        """
        Increments the number of nodes in the graph by one, where 256 is the maximum.

        Parameters:
            None

        Returns:
            None
        """
        if self.devices <= 256:
            self.devices += 1
        else:
            print('Maximum number of nodes reached.')
    
    def delete_node(self):
        """
        Decreases the number of nodes in the data structure by 1, except when the number of nodes is 0.

        Parameters:
            None

        Returns:
            None
        """
        if self.devices > 0:
            self.devices -= 1
        else:
            print('Minimum number of nodes reached.')

    def get_nodes(self):
        """
        Returns the number of nodes in the network.

        Parameters:
            None

        Returns:
            int: The number of nodes in the network.
        """
        return self.nodes
    
    def __check_nodes(self, data):
                    """
                    Checks if the given number of nodes is valid based on the dimensions of the grid.

                    Parameters:
                    - data: an integer representing the number of nodes.

                    Returns:
                    - 'Too many nodes!\nPlease choose a number of nodes that is less than the number of columns and rows in the grid.' if the number of nodes is greater than or equal to the total number of cells in the grid.
                    - None if the number of nodes is valid.
                    """
                    #self.nodes = int(data)
                    if int(data) >= self.columns * self.rows:
                        return 'Too many nodes!\nPlease choose a number of nodes that is less than the number of columns and rows in the grid.'
                    else:
                        return None
    
    def __set_columns(self, col):
        """
        Sets the number of columns in the grid.

        Parameters:
        - col: an integer representing the number of columns.

        Returns:
        None
        """
        self.grid_size[0] = col
    
    def set_simulation(self, simulation_instance):
        """
        Set the simulation instance for the object.

        Parameters:
            simulation_instance (object): The simulation instance to be set.

        Returns:
            None
        """
        self.sim = simulation_instance
    
    def __set_rows(self, row):
        """
        Sets the number of rows in the grid.

        Parameters:
        - row: an integer representing the number of rows.

        Returns:
        None
        """
        self.grid_size[1] = row
    
    def gui_handler(self):
        data = pywebio.input.input_group("Start parameters",[
            pywebio.input('Input number of columns in the grid', name='columns', type=pywebio.NUMBER, required = True, placeholder = '0', validate = self.__set_columns),
            pywebio.input('Input number of rows in the grid', name='rows', type=pywebio.NUMBER, required = True, placeholder = '0', validate = self.__set_rows),
            pywebio.input('Input the number of nodes in the network', name='nodes', type=pywebio.NUMBER, required = True, placeholder = '0', validate = self.__check_nodes),
        ])
        
        self.sim.start_simulation((data['columns'], data['rows']), data['nodes'])
        
        pywebio.put_text(f"Average throughput: {self.sim.get_avg_metrics('throughput')} MB/s")
        pywebio.put_text(f"Average packet loss: {self.sim.get_avg_metrics('packet_loss')} %")
        pywebio.put_text(f"Average delay: {self.sim.get_avg_metrics('delay')} ms")
    
    start_gui = lambda self: pywebio.start_server(self.gui_handler, port=8080)
    """
    Starts the web interface.
    
    Parameters:
        None
        
    Returns:
        None
    """
