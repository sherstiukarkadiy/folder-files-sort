import os
import shutil 
import re

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

def normalize(file_path: str) -> None:
    """_summary_

    Args:
        file_path (str): _description_

    Returns:
        _type_: _description_
    """
    
    file_name = os.path.basename(file_path)
    file_name,file_suffix = os.path.splitext(file_name)
    cyrillic_symbols = ("а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у",
                "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я", "є", "і", "ї", "ґ")
    latin_symbols = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
                "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")
    translit_map = {}
    for c, t in zip(cyrillic_symbols, latin_symbols):
        translit_map[ord(c)] = t
        translit_map[ord(c.upper())] = t.upper()
    
    new_name = file_name.translate(translit_map)
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
        new_path = os.path.splitext(new_path)[0]
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

def delete_empty_folders(dir_path: str, counter = 0, hidd_except = True) -> int:
    """Recursively delete empty folders in such directory

    Args:
        dir_path (str): path to directory,
        counter (int, optional): start calculation number of deleted folders. Defaults to 0.,
        hidd_except (bool, optional): If True fuction ignores all hidden folders, if False - delete them too. Defaults to True.

    Returns:
        int: number of deleted folders
    """
    
    for element in os.scandir(dir_path):
        if hidd_except and element.name.startswith("."): continue
        if element.is_dir():
            try:
                os.rmdir(element.path)
            except OSError:
                counter += delete_empty_folders(element.path,counter)
            else:
                counter += 1
    return counter
        
                