from pkg            import * 
from sequence_item  import * 
from sequencer      import *
from agent          import *
import random

class reset_sequence(uvm_sequence):

    def __init__(self, name):
        super().__init__(name)
        


    async def body(self):
        cocotb.log.info( " [SEQUENCE] WE ARE STARTING  body SEQUENCE")
        self.sequence_item_instance = uvm_factory().create_object_by_name("sequence_item"   ,name = "sequence_item_instance")
        await self.start_item(self.sequence_item_instance)
        self.sequence_item_instance.randomize_with(lambda rst: rst == 1  )
        #self.sequence_item_instance.display("SEQUENCE")
        await self.finish_item(self.sequence_item_instance)

class write_correct_sequence(uvm_sequence):

    def __init__(self, name):
        super().__init__(name)
        

    async def body(self):
        cocotb.log.info( " [SEQUENCE] WE ARE STARTING  body SEQUENCE")
        self.sequence_item_instance = uvm_factory().create_object_by_name("sequence_item"   ,name = "sequence_item_instance")
        await self.start_item(self.sequence_item_instance)
        self.sequence_item_instance.randomize_with(lambda rst,wr: rst == 0 and wr == 1   )
        self.sequence_item_instance.addr = random.randint(0, 31)
        #self.sequence_item_instance.display("SEQUENCE")
        await self.finish_item(self.sequence_item_instance)


class read_correct_sequence(uvm_sequence):

    def __init__(self, name):
        super().__init__(name)
        
        
    async def body(self):
        cocotb.log.info( " [SEQUENCE] WE ARE STARTING  body SEQUENCE")
        self.sequence_item_instance = uvm_factory().create_object_by_name("sequence_item"   ,name = "sequence_item_instance")
        await self.start_item(self.sequence_item_instance)
        self.sequence_item_instance.randomize_with(lambda rst,wr: rst == 0 and wr == 0   )
        self.sequence_item_instance.addr = random.randint(0, 31)
        #self.sequence_item_instance.display("SEQUENCE")
        await self.finish_item(self.sequence_item_instance)

class write_err_sequence(uvm_sequence):

    def __init__(self, name):
        super().__init__(name)
        

    async def body(self):
        cocotb.log.info( " [SEQUENCE] WE ARE STARTING  body SEQUENCE")
        self.sequence_item_instance = uvm_factory().create_object_by_name("sequence_item"   ,name = "sequence_item_instance")
        await self.start_item(self.sequence_item_instance)
        self.sequence_item_instance.randomize_with(lambda rst,wr: rst == 0 and wr == 1   )
        self.sequence_item_instance.addr = random.randint(32, 255)
        #self.sequence_item_instance.display("SEQUENCE")
        await self.finish_item(self.sequence_item_instance)


class read_err_sequence(uvm_sequence):

    def __init__(self, name):
        super().__init__(name)
        
        
    async def body(self):
        cocotb.log.info( " [SEQUENCE] WE ARE STARTING  body SEQUENCE")
        self.sequence_item_instance = uvm_factory().create_object_by_name("sequence_item"   ,name = "sequence_item_instance")
        await self.start_item(self.sequence_item_instance)
        self.sequence_item_instance.randomize_with(lambda rst,wr: rst == 0 and wr == 0   )
        self.sequence_item_instance.addr = random.randint(32, 255)
        #self.sequence_item_instance.display("SEQUENCE")
        await self.finish_item(self.sequence_item_instance)