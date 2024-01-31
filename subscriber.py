from pkg import * 
from sequence_item import * 
from cocotb.triggers import * 
import cocotb
import cocotb.queue
from cocotb_coverage.coverage import *

@CoverPoint("top.dout"       , vname="dout"       , bins =  list(range(  0, 256  )))
@CoverPoint("top.done"       , vname="done"       , bins =  list(range(  0, 2    ))) 
@CoverPoint("top.err"        , vname="err"        , bins =  list(range(  0, 2    ))) 
def sample(dout,done,err):
    pass

class subscriber(uvm_subscriber):


    def build_phase(self):
        self.logger.info( " [SUBSCRIBER] WE ARE STARTING  build_phase SUBSCRIBER")
        self.subsc_mail    = uvm_blocking_get_port("score_mail",self)
        self.t_subscriber  = uvm_factory().create_object_by_name("sequence_item"   ,name = "t_monitor")

    def connect_phase(self):
        self.logger.info( " [SUBSCRIBER] WE ARE STARTING  connect_phase SUBSCRIBER")

    async def run_phase(self):
        self.logger.info( " [SUBSCRIBER] WE ARE STARTING  run_phase SUBSCRIBER")
        while True :
            self.t_subscriber = await self.subsc_mail.get()
            #self.t_subscriber.display("SUBSCRIBER")
            sample(self.t_subscriber.dout,self.t_subscriber.done,self.t_subscriber.err) 
    
    def coverage_report(self):
        dout_tb       = coverage_db["top.dout"].coverage          
        dout_tb_p     = coverage_db["top.dout"].cover_percentage  
        cocotb.log.info("The dout_tb   coverage is : "+str(dout_tb))
        cocotb.log.info("The dout_tb_p coverage percentage is : "+str(dout_tb_p))


