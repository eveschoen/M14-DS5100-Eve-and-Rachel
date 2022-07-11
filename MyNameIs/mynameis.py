class MyNameIs:
    '''
    PURPOSE: this class takes a name as a string and returns an introduction printed
    
    INPUT:
    name   a string
    
    OUTPUT:
    None, just a print statement
    '''
    
    def __init__(self, name):
        '''
        PURPOSE: initializes variable name
        
        INPUT:
        name   a string
        
        OUTPUT:
        none
        '''
        self.name = name
        
    def printname(self):
        '''
        PURPOSE: takes name variable and prints it as part of an introductory statement
        
        INPUT:
        none
        
        OUTPUT:
        A print statement
        '''
        print("Hi my name is", self.name)