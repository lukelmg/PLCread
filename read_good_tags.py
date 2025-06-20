"""
Reads all tags containing the word 'good' from a PLC and prints their values.
"""

from pylogix import PLC

comm = PLC()
comm.IPAddress = '192.168.1.210'

ret = comm.Read("Count_Bin_Good_Parts_Bin")
print(ret.TagName, ret.Value, ret.Status)

comm.Close()