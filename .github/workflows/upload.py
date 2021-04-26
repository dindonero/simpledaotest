import pip, importlib
from os import walk

url = "http://18.224.107.59:5000/"

class File:
    def __init__(self, filename, data):
        self.filename = filename
        self.data = data
        
    def toJson(self):
        return {
            'filename': self.filename,
            'data': self.data
        }

def install_and_import(package):
    try:
        importlib.import_module(package)
    except ImportError:
        import pip
        pip.main(['install', package])
    finally:
        globals()[package] = importlib.import_module(package)

def retrieve_solidity_files_from_repo():
    solidity_files = []
    for root, dirs, files in walk('./'):
        for file in files:
            if file.endswith('.sol'):
                solidity_files.append(root + '/' + file)
    return solidity_files
                

                
if __name__ == "__main__":
    install_and_import('requests')
    files = retrieve_solidity_files_from_repo()
    
    response = requests.get(url)
    print(response)
