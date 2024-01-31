from pkg import * 

class scoreboard(uvm_scoreboard):

    def __init__(self, name, Parent):
        super().__init__(name, Parent)
        self.passed_test_cases = 0 
        self.failed_test_cases = 0 

    def build_phase(self):
        self.logger.info( " [SCOREBOARD] WE ARE STARTING  build_phase SCOREBOARD")
        self.score_mail      = uvm_blocking_get_port("score_mail",self)
        self.t_scoreboard    = uvm_factory().create_object_by_name("sequence_item"   ,name = "t_monitor")
        self.passed_test_cases  = 0
        self.failed_test_cases  = 0
        self.err_test_cases     = 0
        self.read_test_cases    = 0 
        self.write_test_cases   = 0 
        self.reset_test_cases   = 0
        self.golden_memory      = [0] * 256
        self.golgen_output      = 0


    def connect_phase(self):
        self.logger.info( " [SCOREBOARD] WE ARE STARTING  connect_phase SCOREBOARD")

    async def run_phase(self):
        self.logger.info( " [SCOREBOARD] WE ARE STARTING  run_phase SCOREBOARD")
        while True :
            self.t_scoreboard = await self.score_mail.get()
            self.t_scoreboard.display("SCOREBOARD")
            """**************************  TEST CASES **************************"""
            if self.t_scoreboard.rst == 1:
                self.reset_test_case()
            elif self.t_scoreboard.done == 1 and self.t_scoreboard.wr == 1:
                self.write_test_case()    
            elif self.t_scoreboard.done == 1 and self.t_scoreboard.wr == 0:
                self.read_test_case()
            """******************************************************************"""


    def reset_test_case (self) :
        self.reset_test_cases +=1
        self.golgen_output = 0
        if self.t_scoreboard.dout == self.golgen_output:
            self.passed_test_cases += 1
            cocotb.log.info("Reset Test Case Passed ")
        else:
            self.failed_test_cases += 1
            cocotb.log.info("Reset Test Case Failed ")

    def write_test_case(self) :
        self.write_test_cases += 1
        if self.t_scoreboard.err == 1 and self.t_scoreboard.addr > 31 :
            self.err_test_cases += 1
        else :
            self.golden_memory[self.t_scoreboard.addr] = self.t_scoreboard.din

            if self.t_scoreboard.dout == self.golgen_output:
                self.passed_test_cases += 1
                cocotb.log.info("Write Test Case Passed ")
            else:
                self.failed_test_cases += 1
                cocotb.log.info("Write Test Case Failed ")


    def read_test_case(self):
        self.read_test_cases += 1 
        if self.t_scoreboard.err == 1 and self.t_scoreboard.addr > 31 :
            self.err_test_cases += 1
        else :
            self.golgen_output = self.golden_memory[self.t_scoreboard.addr]

            if self.t_scoreboard.dout == self.golgen_output:
                self.passed_test_cases += 1
                cocotb.log.info("Read Test Case Passed ")
            else:
                self.failed_test_cases += 1
                cocotb.log.info("Read Test Case Failed ")


    def report_test_cases(self):
        self.total_test_cases = self.passed_test_cases + self.failed_test_cases + self.err_test_cases
        cocotb.log.info("The Number Of Total  Test Cases is :  " + str(self.total_test_cases)) 
        cocotb.log.info("The Number Of Rest   Test Cases is :  " + str(self.reset_test_cases))    
        cocotb.log.info("The Number Of Read   Test Cases is :  " + str(self.read_test_cases))  
        cocotb.log.info("The Number Of Write  Test Cases is :  " + str(self.write_test_cases)) 
        cocotb.log.info("The Number Of err    Test Cases is :  " + str(self.err_test_cases))  
        cocotb.log.info("The Number Of Passed Test Cases is :  " + str(self.passed_test_cases))  
        cocotb.log.info("The Number Of Failed Test Cases is :  " + str(self.failed_test_cases))     
  

   
                