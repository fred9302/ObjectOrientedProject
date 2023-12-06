import simulation

class gui:
    def __init__(self):
        self.no_nodes = 0
    
    def add_node(self):
        """
        Increments the number of nodes in the graph by one, where 256 is the maximum.

        Parameters:
            None

        Returns:
            None
        """
        if self.no_nodes <= 256:
            self.no_nodes += 1
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
        if self.no_nodes > 0:
            self.no_nodes -= 1
        else:
            print('Minimum number of nodes reached.')
    
    
    
    def show_information(self):
        pass