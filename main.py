from __init__ import *
from functions import *



dictionary,knows_ext, unknows_ext = scroll_files(DIR_PATH,folders_dict)
for k,v in dictionary.items():
    print(f"{k[0]}: {v[1]}")
print(f"{knows_ext=}\n{unknows_ext=}")