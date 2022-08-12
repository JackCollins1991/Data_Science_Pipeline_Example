_directory = {}

class DataStore:
    '''Provides a class for storing and retreiving data within your application.'''
    def store_data(data, name:str):
        _directory[name]= data
    def get_data(name:str):
        return _directory[name]
