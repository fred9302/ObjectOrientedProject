from pywebio import start_server, input, output, FLOAT, INT

class gui:
    def __init__(self):
        self.nodes = 0
        self.toggle_gui = None
    
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
        if self.nodes <= 256:
            self.nodes += 1
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
        if self.nodes > 0:
            self.nodes -= 1
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

    def gui_handler(self):
        pass
    
    start_gui = lambda self: start_server(self.gui_handler, port=8080)
    """
        Runs the web interface.

        Parameters:
            None

        Returns:
            None
        """
