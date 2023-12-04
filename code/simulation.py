import psycopg2
from configparser import ConfigParser

class simulation:
    def __init__(self):
        self.data = None
        self.dBconn = None
        self.clock = None
            
    def get_data(self):
        return self.data
            
    def set_data(self, new_data):
        self.data = new_data
        
    def add_time(self, time = 0, print_time = False):
        """
        Adds a specified amount of time to the current clock value.
        
        Parameters:
            time (int, optional): The amount of time to add to the current clock value. Defaults to 0.
        
        Raises:
            Exception: If the specified time is less than 0.
        """
        if self.clock is None:
            self.clock = 0
        
        if time >= 0:
            self.clock += time
            if print_time is True:
                print(self.clock)
        else:    
            raise Exception('Time must be greater than or equal to 0')
        
    
    def start_simulation(self):
        """
        Starts the simulation.

        This function does not take any parameters.

        Returns:
            None
        """
        self.add_time(time = 3)
        
        
    def db_config(self, filename='/home/frederik/GitHub/ObjectOrientedProject/code/database.ini', section='postgresql'):
        """
        Reads the database configuration from the specified INI file.
            
        Args:
            filename (str, optional): The name of the INI file. Defaults to 'database.ini'.
            section (str, optional): The section name in the INI file. Defaults to 'postgresql'.
            
        Returns:
            dict: A dictionary containing the database configuration parameters.
            
        Raises:
            Exception: If the specified section is not found in the INI file.
        """
            
        # create a parser
        parser = ConfigParser()
            
        # read config file
        parser.read(filename)

        # get section, default to postgresql
        db = {}
        if parser.has_section(section):
            params = parser.items(section)
            for param in params:
                db[param[0]] = param[1]
        else:
            raise Exception('Section {0} not found in the {1} file'.format(section, filename))

        return db
        
    def connect(self):
        """
        Connects to the PostgreSQL database using the provided connection parameters and print the PostgreSQL database server version.

        Parameters:
            None

        Returns:
            None
        """
            
        try:
            # read connection parameters
            params = self.db_config()
            
            # connect to the PostgreSQL server
            print('Connecting to the PostgreSQL database...')
            self.dbConn = psycopg2.connect(**params)
            
            # create a cursor
            cur = self.dbConn.cursor()
            
            # execute a statement
            print('PostgreSQL database version:')
            cur.execute('SELECT version()')
            
            # display the PostgreSQL database server version
            db_version = cur.fetchone()
            print(db_version)
            
            # close the communication with the PostgreSQL
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if self.dbConn is not None:
                self.dbConn.close()
                print('Database connection closed.')