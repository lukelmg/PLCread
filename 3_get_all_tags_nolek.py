"""
Get the tag list from the PLC

This will fetch all the controller and program
scoped tags from the PLC.  In the case of
Structs (UDTs), it will not give you the makeup
of each  tag, just main tag names.
"""
from pylogix import PLC

with PLC() as comm:
    comm.IPAddress = '192.168.1.211'
    tags = comm.GetTagList()
    
    if tags.Status != 'Success':
        print(f"Failed to get tag list: {tags.Status}")
    elif tags.Value is None:
        print("No tags returned from PLC.")
    else:
        with open("tags.txt", "w") as f:
            for t in tags.Value:
                f.write(f"{t.TagName}, {t.DataType}\n")