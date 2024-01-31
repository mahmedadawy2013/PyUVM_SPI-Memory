from pkg       import * 
from sequencer import * 
from driver    import * 
from monitor   import *

class agent(uvm_agent):

    def __init__(self, name, Parent):
        super().__init__(name, Parent)

    def build_phase(self):
        self.logger.info( " [AGENT] WE ARE STARTING  build_phase AGENT")
        self.sequencer_instance  = uvm_factory().create_component_by_name("sequencer"  ,name = "sequencer_instance",parent = self)
        self.driver_instance     = uvm_factory().create_component_by_name("driver"     ,name = "driver_instance"   ,parent = self)
        self.monitor_instance    = uvm_factory().create_component_by_name("monitor"    ,name = "monitor_instance"  ,parent = self)

        


    def connect_phase(self):
        self.logger.info( " [AGENT] WE ARE STARTING  connect_phase AGENT")
        self.driver_instance.seq_item_port.connect(self.sequencer_instance.seq_item_export)

    async def run_phase(self):
        self.logger.info( " [AGENT] WE ARE STARTING  run_phase AGENT")




   
                