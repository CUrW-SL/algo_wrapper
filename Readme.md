#Algo Wrapper
##Introduction
This package's intention is to provide a frame to define algorithms or data processings.
There are 3 main classes IOProcessor, Configs, Algorithm. 
    
### Config Class    
Config class is a concrete class and can be instantiated with the path to json configuration file. 
Structure of the json configuration file should be as follows and must always follow the structure;

    {
    "algo_config": {}, 
    "input_config": {},
    "output_config": {}
    }
    
### IOProcessor Class
IOProcessor class is an abstract class with two abstract methods, 'get_input(self)' and 
'push_output(self, algo_output). Implementation of these two methods specifies how input data 
should be retrieved and how output data should be pushed into wherever the implementor desires.

When instantiating an extension of IOProcessor class, it should be instantiated with a Config instance.
This way the 'get_input' and 'push_output' methods can access input and output configuration using
'self.input_config' and 'self.output_config'

### Algorithm Class
Algorithm class is also an abstract class with one abstract method 'algo(self, algo_input)'. 
The implementation of this method specifies how algo_input should be processed. It also needs
to return the output at the end of the algorithm.

When instantiating an extension of Algorithm class, it should be instantiated with an IOProcessor instance
and a Config instance.

Implementor can access 'algo_config' within the 'algo' method using 'self.algo_config'.

The 'execute(self)' method retrieve the input (by invoking IOProcessor.get_input()) feed that into the algorithm 
(by invoking algo(algo_input)) and finally push the output (by invoking IOProcessor.push_output()) 
