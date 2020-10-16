""" Attribute list """

class call_list(list):
    
    """ List that distributes calls to its members and returns list of return values """
    
    def __init__(self,name,*args):
        super().__init__(*args)
        self._name = name
    
    def __call__(self,*args,**kwargs):
        
        try: return [ func_obj(*args,**kwargs) for func_obj in self ]
        except TypeError: raise TypeError(f"Not all objects in '{self._name}' are callable.")

class attr_list(list):
    
    """ A list that can access and assign attributes of it's entries like it's own """
    
    def __setattr__(self, name, value):
        
        for obj in self:
            setattr(obj, name, value)
    
    def __getattr__(self,name):
        
        try: 
            return call_list( type(self).__name__, [ getattr(obj,name) for obj in self ] )
        except AttributeError:
            raise AttributeError(f"Neither '{type(self).__name__}' object nor it's entries have attribute '{name}'")