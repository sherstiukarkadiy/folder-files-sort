import os
import shutil 
import re

def normalize(file_path: str) -> None:
    file_name = os.path.basename(file_path)
    file_name,file_suffix = os.path.splitext(file_name)
    cyrillic_symbols = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
    latin_symbols = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
                "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")
    translation = {}
    for c, t in zip(cyrillic_symbols, latin_symbols):
        translation[ord(c)] = t
        translation[ord(c.upper())] = t.upper()
    
    new_name = file_name.translate(translation)
    new_name = re.sub(r'[^\w]','_',new_name)
    return new_name + file_suffix

def replace_files(old_path: str, new_path: str) -> None:
    """Move files in a new folder
    Args:
        old_path (str): old path including file name
        new_path (str): new path including file name
    """
    new_path = f"{new_path}/{normalize(old_path)}"
    if 'Archive' in new_path:
        os.path.splitext(new_path)
        shutil.unpack_archive(old_path,new_path)
    else:
        shutil.move(old_path, new_path)
    return

def scroll_files(dir_path: str,folders_dict: dict, *,knows_list: list = [],unknows_list: list = [] ) -> tuple:
    """Recursivly scroll all files in direction and underdirections to add their names to Image,Video,Documents,
       Music or Archives by file extencion
        
        THe function calls function 'replace_files' to move them in other folder by file extencion
    Args:
        dir_path (str): direction path
        folders_dict (dict): dictionary of new dictionary names, file extencions and pathes
    Returns:
        tuple: return new dictionary, set of all knows extencions and set of all uknows extencions in the directory
    """
    
    for file in os.scandir(dir_path):
        
        for name in folders_dict:
            if file == name[0]:
                continue
            pass
        
        if file.is_dir():
            scroll_files(file.path,folders_dict, knows_list=knows_list,unknows_list=unknows_list)
            continue
        
        file_suffix = os.path.splitext(file.path)[1].removeprefix(".").upper()
        for key, val in folders_dict.items():
            if file_suffix in key:
                replace_files(file.path, val[0])
                val[1].append(file.name)
                knows_list.append(file_suffix)
                break
        else:
            unknows_list.append(file_suffix)
            
    return folders_dict, set(knows_list), set(unknows_list)