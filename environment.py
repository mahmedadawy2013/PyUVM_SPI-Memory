from pkg        import * 
from agent      import * 
from scoreboard import * 
from subscriber import * 
class environment(uvm_env):

    def __init__(self, name, Parent):
        super().__init__(name, Parent)

    def build_phase(self):
        self.logger.info( " [ENVIRONMENT] WE ARE STARTING  build_phase ENVIRONMENT")
        self.scoreboard_instance = uvm_factory().create_component_by_name("scoreboard",name = "scoreboard_instance",parent = self)
        self.subscriber_instance = uvm_factory().create_component_by_name("subscriber",name = "subscriber_instance",parent = self)
        self.agent_instance      = uvm_factory().create_component_by_name("agent"     ,name = "agent_instance",parent = self)
        self.Fifo_mon_score      = uvm_tlm_fifo("Fifo_mon_score" , self)
        self.Fifo_mon_subsc      = uvm_tlm_fifo("Fifo_mon_subsc" , self)



    def connect_phase(self):
        self.logger.info( " [ENVIRONMENT] WE ARE STARTING  connect_phase ENVIRONMENT")
        
        self.agent_instance.monitor_instance.mon_mail_s.connect(self.Fifo_mon_score.put_export)
        self.scoreboard_instance.score_mail.connect(self.Fifo_mon_score.get_export)

        self.agent_instance.monitor_instance.mon_mail_su.connect(self.Fifo_mon_subsc.put_export)
        self.subscriber_instance.subsc_mail.connect(self.Fifo_mon_subsc.get_export)
        self.scoreboard_instance.score_handover = self.agent_instance.driver_instance.driv_handover
        


    async def run_phase(self):
        self.logger.info( " [ENVIRONMENT] WE ARE STARTING  run_phase ENVIRONMENT")



   
                