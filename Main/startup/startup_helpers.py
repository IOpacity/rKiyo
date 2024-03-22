import os

def get_all_files(path, extension=None):
    """
    Get a list of all files in a directory and its subdirectories.
    
    Args:
        path (str): The path to the directory.
        extension (str, optional): Filter by file extension. If provided, only files
            with this extension will be included. Defaults to None.
    
    Returns:
        list: A sorted list of file paths.
    """
    filelist = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if not (extension and not file.endswith(extension)):
                filelist.append(os.path.join(root, file))
    return sorted(filelist)
