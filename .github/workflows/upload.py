import importlib
from os import walk

import pip
import requests as requests

url = "http://18.224.107.59:5000/"


def install_and_import(package):
    try:
        importlib.import_module(package)
    except ImportError:
        pip.main(['install', package])
    finally:
        globals()[package] = importlib.import_module(package)


def find_solidity_files_in_repo():
    solidity_files = []
    for root, dirs, files in walk('../../'):
        for file in files:
            if file.endswith('.sol'):
                solidity_files.append(root + '/' + file)
    return solidity_files


def upload_files_to_smartbugs(filenames):
    files_dict = {}
    for name in filenames:
        f = open(name, 'rb')
        files_dict[name] = f

    response = requests.post(url=url, files=files_dict)

    # Closing files
    for file in files_dict.values():
        file.close()
    return response


if __name__ == "__main__":
    install_and_import('requests')

    # Searches repo for all solidity files
    filenames = find_solidity_files_in_repo()

    # Upload Files to Smartbugs
    sarif_results = upload_files_to_smartbugs(filenames=filenames)

    print(sarif_results.text)
