from pkg import * 


class  sequence_item(uvm_sequence_item,Randomized):
    randc_queue      = queue.Queue(maxsize=256)
    def __init__(self,name):
        super().__init__(name)
        Randomized.__init__(self)
        self.rst         =  0  
        self.wr          =  0  
        self.addr        =  0
        self.din         =  0
        self.dout        =  0
        self.done        =  0 
        self.err         =  0 

        self.add_rand("rst"        , list(range(0,2)                              )   ) 
        self.add_rand("wr"         , list(range(0,2)                              )   ) 
        self.add_rand("addr"       , list(range(0,256)                            )   ) 
        self.add_rand("din"        , list(range(0,256)                            )   ) 
        
        self.add_constraint(lambda addr,randc_queue : addr not in randc_queue.queue)
    
    def post_randomize(self):
        self.randc_queue.put(self.addr)
        if self.randc_queue.full():
            while not self.randc_queue.empty():
                self.randc_queue.get()


    def display(self,name = "TRANSACTION"):
        cocotb.log.info("******************"+str(name)+"*******************")
        cocotb.log.info("the Value of rst        is   " + str(self.rst    ))
        cocotb.log.info("the Value of wr         is   " + str(self.wr     ))
        cocotb.log.info("the Value of addr       is   " + str(self.addr   ))
        cocotb.log.info("the Value of din        is   " + str(self.din    ))
        cocotb.log.info("the Value of dout       is   " + str(self.dout   ))
        cocotb.log.info("the Value of done       is   " + str(self.done   ))
        cocotb.log.info("the Value of err        is   " + str(self.err    ))
        cocotb.log.info("**************************************************")
