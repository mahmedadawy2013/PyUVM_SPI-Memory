from pkg import * 

class sequencer(uvm_sequencer):

    def __init__(self, name, Parent):
        super().__init__(name, Parent)

    def build_phase(self):
        self.logger.info( " [SEQUENCER] WE ARE STARTING  build_phase SEQUENCER")
        

    def connect_phase(self):
        self.logger.info( " [SEQUENCER] WE ARE STARTING  connect_phase SEQUENCER")

'''
Dont Implement Run Phase inside the Sequencer 
'''



   
                