import os
from pathlib import Path

DEFAULT_STORAGE_LOCATION = os.path.join(Path( __file__ ).parent.absolute(),'temp')

class ModelResults:
    '''This class determines the key metrics to be recorded by each candiate model.'''
    def __init__(self):
        self.metric_result = None
        self.roc_data = None
        self.variable_importance = None


class CandidateModel:
    '''
    A base class which can be extended into classes which will fullfill the following contract: they use their override of the fit_and_evaluate method to
    hyperparameter search for the best version of its model. store_results() is then used to fulfill the contract for the key results required: the key metric 
    (ie: accuracy, recall etc), the data for the roc curve, the variable importance.
    '''
    def fit_and_evaluate(self):
        self.results:ModelResults = None
        return self.results
    
    def store_results(self,storage_location):
        self.results = ModelResults()
        return


class CandidateComparer:
    '''Instantiate an object of this class and supply it with a list of the CandidateModel class. Invoke the execute() method to then perform a search for the best model in
    the list. The class will then provide the best model and an ROC graph comparing all candiate models'''
    def __init__(self,candidates:list[CandidateModel], metric:str, do_roc=False, storage_location=None):
        self.roc = None
        self.best_model = None
        self.candidates = candidates
        self.metric = metric
        self.do_roc = do_roc
        if storage_location == None:
            storage_location = DEFAULT_STORAGE_LOCATION
        else:
            self.storage_location = storage_location
        return
    
    def _fit_candiates(self):
        for candidate in self.candidates:
            candidate.fit_and_evaluate()
            candidate.store_results(self.storage_location)
    
    def _compare_results(self):
        best = None
        self.best_model = best
    
    def _super_roc(self):
        fig = None
        self.roc = fig
    
    
    def execute(self):
        self._fit_candiates(self)
        self._compare_results(self)
        if(self.do_roc == True):
            self._super_roc(self)
        
        