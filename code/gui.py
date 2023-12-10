from pywebio.input import *
from pywebio.output import *
from pywebio.pin import *
from pywebio import start_server

class gui:
    def __init__(self):
        self.devices = 0
        self.grid_size = [0, 0]
        self.sim = None
        self.toggle_gui = None
    

    def __check_nodes(self, data):
        """
        Check if the given data is valid for the grid.

        Parameters:
            data (int): The data to be checked.

        Returns:
            bool or None: Returns False if the data is greater than or equal to the grid size, otherwise returns None.
        """
        if data >= self.grid_size[0] * self.grid_size[1]:
            return f'The number of nodes must be less than the number of columns multiplied by the number of rows, which is {self.grid_size[0] * self.grid_size[1]}'
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

    def __set_rows(self, row):
        """
        Sets the number of rows in the grid.

        Parameters:
        - row: an integer representing the number of rows.

        Returns:
        None
        """
        self.grid_size[1] = row        

    set_toggle_gui = lambda self, new_gui: setattr(self, 'toggle_gui', new_gui)
    """
    This code defines a lambda function called set_gui that takes two parameters: self and new_gui.
    
    It uses the setattr function to set the toggle_gui attribute of the object self to the value of new_gui.
    """
    
    get_toggle_gui = lambda self: getattr(self, 'toggle_gui')
    """
    This code defines a lambda function called get_gui that takes one parameter: self.
    
    It uses the getattr function get the toggle_gui attribute of the object self.
    """

    def get_nodes(self):
        """
        Returns the number of nodes in the network.

        Parameters:
            None

        Returns:
            int: The number of nodes in the network.
        """
        return self.devices
    
    def set_simulation(self, simulation_instance):
        """
        Set the simulation instance for the object.

        Parameters:
            simulation_instance (object): The simulation instance to be set.

        Returns:
            None
        """
        self.sim = simulation_instance
    
    def __gui_handler(self):
        data = input_group("Start parameters",[
            input('Input number of columns in the grid', name='columns', type=NUMBER, required = True, placeholder = '0', validate = self.__set_columns),
            input('Input number of rows in the grid', name='rows', type=NUMBER, required = True, placeholder = '0', validate = self.__set_rows),
            input('Input the number of nodes in the network', name='nodes', type=NUMBER, required = True, placeholder = '0', validate = self.__check_nodes),
        ])
        self.devices = data['nodes']
        
        self.sim.start_simulation((data['columns'], data['rows']), data['nodes'])
        
        img = open('./network_topology.png', 'rb').read()
        
        put_text(f"Average throughput: {self.sim.get_avg_metrics('throughput')} MB/s")
        put_text(f"Average packet loss: {'%.2f' % self.sim.get_avg_metrics('packet_loss')} %")
        put_text(f"Average delay: {self.sim.get_avg_metrics('delay')} ms")
        
        put_image(img, width = '500px')
    
    start_gui = lambda self: start_server(self.__gui_handler, port=8080)
    """
    Starts the web interface.
    
    Parameters:
        None
        
    Returns:
        None
    """
