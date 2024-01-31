from pkg         import * 
from environment import * 
from sequence    import *

@pyuvm.test()
class test(uvm_test):
    def __init__(self, name, Parent):
        super().__init__(name, Parent)
        
    def build_phase(self):
        self.logger.info( " [TEST] WE ARE STARTING build_phase TEST")
        self.environment_instance    = uvm_factory().create_component_by_name("environment"   ,name = "environment_instance",parent = self)
        self.reset_sequence_Instance = uvm_factory().create_object_by_name("reset_sequence"   ,name = "reset_sequence_Instance")
        self.write_correct_sequence_Instance = uvm_factory().create_object_by_name("write_correct_sequence"   ,name = "write_correct_sequence_Instance")
        self.write_err_sequence_Instance     = uvm_factory().create_object_by_name("write_err_sequence"       ,name = "write_err_sequence_Instance")
        self.read_correct_sequence_Instance  = uvm_factory().create_object_by_name("read_correct_sequence"    ,name = "read_correct_sequence_Instance")
        self.read_err_sequence_Instance      = uvm_factory().create_object_by_name("read_correct_sequence"    ,name = "read_err_sequence_Instance")
        self.dut                     = cocotb.top
        self.CLK                     = Clock(self.dut.clk, 20, units="ns")
        ConfigDB().set(self,"*","DUT",self.dut)


    def connect_phase(self):
        self.logger.info( " [TEST] WE ARE STARTING  connect_phase TEST")



    async def run_phase(self):
        self.raise_objection()
        self.logger.info( " [TEST] WE ARE STARTING run_phase TEST")
        await cocotb.start(self.CLK.start())
        await self.reset_sequence_Instance.start(self.environment_instance.agent_instance.sequencer_instance)
        
        for repition in range(3) : 
            for repition in range(256) : 
                await self.write_err_sequence_Instance.start(self.environment_instance.agent_instance.sequencer_instance)
            for repition in range(256) : 
                await self.read_err_sequence_Instance.start(self.environment_instance.agent_instance.sequencer_instance)
            
            for repition in range(256) : 
                await self.write_correct_sequence_Instance.start(self.environment_instance.agent_instance.sequencer_instance)
            for repition in range(256) : 
                await self.read_correct_sequence_Instance.start(self.environment_instance.agent_instance.sequencer_instance)
            
            for repition in range(256) : 
                await self.write_err_sequence_Instance.start(self.environment_instance.agent_instance.sequencer_instance) 
            for repition in range(256) : 
                await self.read_err_sequence_Instance.start(self.environment_instance.agent_instance.sequencer_instance)  

        await RisingEdge(self.dut.done)
        self.environment_instance.scoreboard_instance.report_test_cases()
        self.environment_instance.subscriber_instance.coverage_report()
        coverage_db.export_to_xml(filename="ALU_coverage.xml")
        self.drop_objection()



