import random
import math
import networkx as nx
import matplotlib.pyplot as plt

class simulation:
    def __init__(self):
        self.clock = None
        self.grid = None
        self.verbose = None
        self.next_ip = 0
        self.nodes = []
        self.positions = []
        self.net_metrics = dict()
        self.avg_metrics = dict()
        
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
                self.__print_grid()
        else:
            exit('Rows and columns must be greater than 0')
    
    def __print_grid(self):
        """
        Prints the grid.
        """
        print('\nGrid:')
        for i in range(len(self.grid)):
            if i == len(self.grid) - 1:
                grid_string = f'{self.grid[i]}\n'
            else:
                grid_string = str(self.grid[i])
            
            grid_string = grid_string.replace('[0,', '[ ,')
            grid_string = grid_string.replace(', 0]', ',  ]')
            grid_string = grid_string.replace(' 0,', '  ,')
            grid_string = grid_string.replace(',', ' ')
            print(grid_string)
    
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
    
    def __grid_to_graph(self, columns = 0, rows = 0):
        """
        Generates the graph representation of the given grid network.

        Parameters:
            columns (int): The number of columns in the grid network. Defaults to 0.
            rows (int): The number of rows in the grid network. Defaults to 0.

        Returns:
            None
        """
        # separating the gateway position from the nodes' positions
        gateway_position = self.positions[0] # first position is the gateway
        node_positions = self.positions[1:] # the rest of the positions are the nodes
        
        # create the graph
        G = nx.Graph()
        
        # add the positions of the gateway and the nodes
        G.add_node("Gateway", pos = gateway_position)
        for i, pos in enumerate(node_positions):
            G.add_node(i, pos = pos)
        
        # connect each node to the gateway
        for i in range(len(node_positions)):
            G.add_edge("Gateway", i)
            
        # create a dictionary with the positions of the devices
        positions_dict = {i: pos for i, pos in enumerate(node_positions)}
        positions_dict["Gateway"] = gateway_position
        
        # draw the graph with the positions of the gateway and the nodes
        plt.figure(figsize=(columns, rows))
        nx.draw(G, positions_dict, with_labels = True, node_color = 'skyblue', edge_color='gray')
        nx.draw_networkx_nodes(G, positions_dict, nodelist=["Gateway"], node_color="red")
        plt.title("Network Topology of the Gateway and Nodes")
        plt.savefig('network_topology.png', bbox_inches='tight')
    
    def __generate_positions(self, columns = 0, rows = 0, devices = 0):
        """
        Generates positions for the nodes in the grid.
        """
        
        # check whether amount of nodes can fit in grid
        if devices >= columns * rows:
            exit('Error: Too many nodes. Please choose a number of nodes that is less than the number of columns and rows in the grid.')
        
        position_gen = []
        position_gen.append(list(range(0, columns)))
        position_gen.append(list(range(0, rows)))
        
        #generate positions
        for i in range(devices):
            # check if position is not already taken
            check = False
            
            while check is False:
                temp_position = None
                x = None
                y = None
                
                
                # choose 2 random coordinates from lists of possible coordinates
                x = int(random.choice(position_gen[0]))
                y = int(random.choice(position_gen[1]))
                temp_position = (x, y)
                
                if temp_position in self.positions:
                    if self.verbose is True:
                        print(f'\nError for node {i} with IP {i + 2}: Position ({temp_position[0]}, {temp_position[1]}) is already taken!\n')
                    check = False
                else:
                    check = True
            
            if self.verbose is True:
                print(f'Node {i} with IP {i + 2} has position ({temp_position[0]}, {temp_position[1]})')
            self.positions.append((temp_position[0], temp_position[1]))
        
        # generate an image of the positions in a graph
        self.__grid_to_graph(columns, rows)
        
    def __save_metrics(self, ip, throughput, packet_loss, delay):
        """
        Saves the metrics for a given IP address.

        Parameters:
            ip (int): The IP address for which the metrics are being saved.
            throughput (int): The throughput value for the IP address.
            packet_loss (int): The packet loss value for the IP address.
            delay (float): The delay value for the IP address.
        """
        self.net_metrics[ip] = {'throughput': throughput, 'packet_loss': packet_loss, 'delay': delay}
    
    def __generate_metrics(self):
        """
        Generates statistics for the nodes in the network.

        This function calculates various metrics for each node in the network, such as throughput, packet loss, distance, and delay. The metrics are based on the ESP32 performance documented in the ESP-IDF WiFi API guide. The metrics are randomly generated within certain ranges.

        Parameters:
        - None

        Returns:
        - None
        """
        if self.verbose is True:
            print('')
        for node in range(len(self.nodes)):
            # the following metrics are somewhat based on esp32 performance from: https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-guides/wifi.html
            throughput = 30 - random.randint(1, 10) # Mb/s
            packet_loss = len(self.nodes) - random.randint(1, len(self.nodes)) # %
            distance = math.sqrt((self.positions[node + 1][0] - self.positions[0][0])**2 + (self.positions[node + 1][1] - self.positions[0][1])**2)
            delay = float(10.0 + random.uniform(0.0, distance)) # ms
            
            if self.verbose is True:
                print(f"Metrics for node {node}: Throughput = {throughput} Mb/s, packet loss = {packet_loss}%, delay = {'%.2f' % delay} ms")
            
            self.__save_metrics(self.nodes[node].get_ip(), throughput, packet_loss, delay)
        if self.verbose is True:
            print('')
        
        # calculate average metrics
        self.avg_metrics['throughput'] = sum(self.net_metrics[node]['throughput'] for node in self.net_metrics) / len(self.net_metrics)
        self.avg_metrics['packet_loss'] = sum(self.net_metrics[node]['packet_loss'] for node in self.net_metrics) / len(self.net_metrics)
        self.avg_metrics['delay'] = sum(self.net_metrics[node]['delay'] for node in self.net_metrics) / len(self.net_metrics)
        print(f"\nAverage metrics: Throughput = {self.avg_metrics['throughput']} MB/s, packet loss = {self.avg_metrics['packet_loss']}%, delay = {'%.2f' % self.avg_metrics['delay']} ms")
    
    set_verbose = lambda self, new_verbose: setattr(self, 'verbose', new_verbose)
    """
    This code defines a lambda function called set_verbose that takes two parameters: self and new_verbose.
    
    It uses the setattr function to set the verbose attribute of the object self to the value of new_verbose.
    """
    
    def get_net_metrics(self):
        """
        Returns the metrics for the nodes in the network.
        """
        return self.net_metrics
    
    def get_avg_metrics(self, type):
        """
        Returns the average metrics for the nodes in the network.
        """
        if type == 'throughput':
            return self.avg_metrics.get(type)
        elif type == 'packet_loss':
            return self.avg_metrics.get(type)
        elif type == 'delay':
            return self.avg_metrics.get(type)
        else:
            return self.avg_metrics
    
    def start_simulation(self, grid = (0, 0), connections = 0):
        """
        Initializes the simulation by creating a grid, a gateway, and establishing connections with nodes.

        Parameters:
            grid (tuple): A tuple containing the number of columns and rows for the grid (default is (0, 0)).
            connections (int): The number of nodes to create and establish connections with (default is 0).

        Returns:
            None
        """
        print('\n\nStarting simulation...\n')
        
        self.__create_grid(grid[0], grid[1], self.verbose)
        
        # create gateway
        net = gateway()
        net.set_ip(self.__get_next_ip())
        
        # set position of the gateway in the middle of the grid
        self.positions.append((int(grid[0]/2), int(grid[1]/2)))
        net.set_position(self.positions[0])
        self.grid[self.positions[0][1]][self.positions[0][0]] = net.get_ip()
        if self.verbose == True:
            print (f"Gateway with IP {net.get_ip()} has position ({self.positions[0][0]}, {self.positions[0][1]})\n")
            print(f"Gateway with IP {net.get_ip()} has been created\n")
        
        
        # establish connections with nodes
        for i in range(connections):
            net.connect(ip = self.__get_next_ip())
            self.nodes.append(node())
            self.nodes[i].set_ip(self.__get_ip())
            if self.verbose == True:
                print(f"{self.nodes[i].get_name()} with IP {self.nodes[i].get_ip()} is connected to {net.get_name()} with IP {net.get_ip()}")
        
        # set positions of nodes
        self.__generate_positions(columns = grid[0], rows = grid[1], devices = connections)
        for i in range(connections):
            self.nodes[i].set_position(self.positions[i + 1])
            self.grid[self.positions[i + 1][1]][self.positions[i + 1][0]] = self.nodes[i].get_ip()
        if self.verbose == True:
            self.__print_grid()
        
        print(f'\nPositions: {self.positions}')
        
        
        self.__generate_metrics()
        

class network:
    def __init__(self):
        self.connections = []
        self.netmask = (255, 255, 255, 0)
        super().__init__()
    
    def connect(self, ip = None): # if this method is called from simulation method sim must be self
        self.connections.append(ip)
        
class device:
    def __init__(self):
        self.ip = None
        self.type = None
        self.position = None
        self.name = None
        super().__init__()
    
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
            if self.type == 0:
                self.name = f'Gateway {self.ip - 1}'
            elif self.type == 1:
                self.name = f'Node {self.ip - 2}'
        else:
            print('No IP address provided.')
    
    def get_ip(self):
        """
        Get the IP address.

        Returns:
            int: The IP address.
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
            #print (f'{self.name} with IP {self.ip} has position ({self.position[0]}, {self.position[1]})')
        else:
            print('No position provided.')
            
    def get_position(self):
        """
        Get the position of the object.

        Returns:
            tuple: The position of the object.
        """
        return self.position
    
    def get_name(self):
        """
        Get the name of the object.

        Returns:
            str: The name of the object.
        """
        return self.name
    
class node(device):
    def __init__(self):
        super().__init__()
        self.state = None
        self.type = 1
        
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
        super().__init__()
        self.received_data = None
        self.type = 0
    
    def receive_data(self, data):
        """
        Set the received data attribute.
        
        Args:
            data: The data to be set as the received data attribute.
        
        Returns:
            None
        """
        self.received_data = data

