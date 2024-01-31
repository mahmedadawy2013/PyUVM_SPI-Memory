import cocotb 
from cocotb.triggers import * 
from cocotb.clock    import Clock
from cocotb_coverage.crv import *
from pyuvm import * 
import queue
import pyuvm
import logging
logging.basicConfig(level=logging.NOTSET)
logger = logging.getLogger()
logger.setLevel(logging.DEBUG) 