from mymodules.operations.data_operations import printmessage
from src.configurations import constants
from src.operations import datasource, modelorchestrator, output, preprocessor

def execute():
    datasource.DataSource.execute()
    preprocessor.Preprocessor.execute()
    modelorchestrator.ModelOrchestrator.execute()
    output.Output.execute()
    