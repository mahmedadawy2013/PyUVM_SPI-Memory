from pkg import * 
from sequence_item import * 
"""
register in the factory is done using the inheritance class driver(uvm_driver):

"""
class driver(uvm_driver):

    def __init__(self, name, Parent):
        super().__init__(name, Parent)


    def build_phase(self):
        self.logger.info( " [DRIVER] WE ARE STARTING  build_phase DRIVER")
        self.t_drive          = uvm_factory().create_object_by_name("sequence_item"   ,name = "t_drive")
        self.dut_driver       = ConfigDB().get(self,"","DUT")
        self.driv_handover     = Event(name=None) 

    def connect_phase(self):
        self.logger.info( " [DRIVER] WE ARE STARTING  connect_phase DRIVER")

    async def run_phase(self):
        while True:
            #self.logger.info( " [DRIVER] WE ARE STARTING  run_phase DRIVER")
            self.t_drive = await self.seq_item_port.get_next_item()
            await FallingEdge(self.dut_driver.clk)
            if (self.t_drive.rst == 1 ):
                self.dut_driver.rst = 1 
                self.dut_driver.wr      = self.t_drive.wr
                self.dut_driver.addr    = self.t_drive.addr
                self.dut_driver.din     = self.t_drive.din
                await RisingEdge(self.dut_driver.clk)
            else :
                self.dut_driver.rst     = self.t_drive.rst 
                self.dut_driver.wr      = self.t_drive.wr
                self.dut_driver.addr    = self.t_drive.addr
                self.dut_driver.din     = self.t_drive.din
                await RisingEdge(self.dut_driver.clk)
                await RisingEdge(self.dut_driver.done)
            self.t_drive.display("DRIVER")
            self.seq_item_port.item_done()




   
                