import pip, importlib

def install_and_import(package):
    try:
        importlib.import_module(package)
    except ImportError:
        import pip
        pip.main(['install', package])

install_and_import('requests')
        
url = "http://18.224.107.59:5000/"



response = requests.get(url)
print(response)
