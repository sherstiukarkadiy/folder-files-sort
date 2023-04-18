import os
import sys

try:
    DIR_PATH = "/Users/macair/Desktop/GoIT - course copy"
except IndexError:
    print("No path entered")
    sys.exit()

def create_dirs(dir_path: str) -> tuple:
    """Create new folders in user directory to move files by category:  Images,Video,Documents,Music,Archives

    Args:
        dir_path (str): directory path

    Returns:
        tuple: tuple of folders pathes
    """
    dirs = ["Images","Video","Documents","Music","Archives"]
    pathes =[]
    for dir_name in dirs:
        pathes.append(os.path.join(dir_path,dir_name))
        try:
            os.mkdir(f"{dir_path}/{dir_name}")
        except OSError:
            continue
    return tuple(pathes)
    
folders_tup = create_dirs(DIR_PATH)
folders_dict = {
    ('Images','JPEG', 'PNG', 'JPG', 'SVG'): [folders_tup[0],[]],
    ('Video','AVI', 'MP4', 'MOV', 'MKV'): [folders_tup[1],[]],
    ('Documents','DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX'): [folders_tup[2],[]],
    ('Music','MP3', 'OGG', 'WAV', 'AMR'): [folders_tup[3],[]],
    ('Archives','ZIP', 'GZ', 'TAR'): [folders_tup[4],[]]
}