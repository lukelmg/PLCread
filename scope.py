from pylogix import PLC

with PLC() as comm:
    comm.IPAddress = '192.168.1.210'
    ret = comm.Read('Program:Nolek_Leak_Tester')
    print(ret.TagName, ret.Value, ret.Status)