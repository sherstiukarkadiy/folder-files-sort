from functions import *
import sys

try:
    DIR_PATH = " ".join(sys.argv[1:])
except IndexError:
    print("No path entered")
    sys.exit()
else:
    if not os.path.isdir(DIR_PATH):
        print("Invalid path entered")
        sys.exit()
        
folders_tup = create_dirs(DIR_PATH)
folders_dict = {
    ('Images','JPEG', 'PNG', 'JPG', 'SVG'): [folders_tup[0],[]],
    ('Video','AVI', 'MP4', 'MOV', 'MKV'): [folders_tup[1],[]],
    ('Documents','DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX'): [folders_tup[2],[]],
    ('Music','MP3', 'OGG', 'WAV', 'AMR'): [folders_tup[3],[]],
    ('Archives','ZIP', 'GZ', 'TAR'): [folders_tup[4],[]]
}

dictionary,knows_ext, unknows_ext = scroll_files(DIR_PATH,folders_dict)
for k,v in dictionary.items():
    print(f"{k[0]}: {v[1]}")
print(f"{knows_ext=}\n{unknows_ext=}")

delete_counter = None
while delete_counter != 0:
    delete_counter = delete_empty_folders(DIR_PATH)