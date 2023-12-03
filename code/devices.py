import psycopg2
from configparser import ConfigParser

class devices:
    def __init__(self):
        self.data = None
        self.conn = None
            
        def get_data(self):
            
            return self.data
            
        def set_data(self, new_data):
            self.data = new_data
        
        
        def db_config(self, filename='database.ini', section='postgresql'):
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
            self.conn = None
            
            try:
                # read connection parameters
                params
            
            


if __name__ == '__main__':
    