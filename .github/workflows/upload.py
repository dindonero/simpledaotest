import pip, importlib

def install_and_import(package):
    try:
        importlib.import_module(package)
    except ImportError:
        import pip
        pip.main(['install', package])
    finally:
        globals()[package] = importlib.import_module(package)

install_and_import('requests')

def retrive_solidity_files():
    for root, dirs, files in walk('../../'):
        for file in files:
            if file.endswith('.sol'):
                print(root + "/" + file)
url = "http://18.224.107.59:5000/"



response = requests.get(url)
print(response)
