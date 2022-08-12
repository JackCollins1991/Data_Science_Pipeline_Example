from mymodules.operations.ioperator import IOperator
import src
import mymodules

class Preprocessor(IOperator):
    def execute():
        data = mymodules.operations.data_operations.datastore.DataStore.get_data(src.configurations.constants.NAME_RAW_DATA)
        
        data = example_process(data)
        
        mymodules.operations.data_operations.datastore.DataStore.store_data(data,src.configurations.constants.NAME_PROCESSED_DATA)
        

def example_process(data):
    return data