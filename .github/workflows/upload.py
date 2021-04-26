from os import walk

import importlib
import pip
import requests as requests

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
        pip.main(['install', package])
    finally:
        globals()[package] = importlib.import_module(package)


def find_solidity_files_in_repo():
    solidity_files = []
    for root, dirs, files in walk('./'):
        for file in files:
            if file.endswith('.sol'):
                solidity_files.append(root + '/' + file)
    return solidity_files

def retrieve_solidity_files(filenames):
    files_list = []
    for name in filenames:
        with open(name, 'rb') as f:
            files_list.append(File(filename=name, data=f).toJson())
    return files_list

def upload_files_to_smartbugs(files_list):
    return requests.post(url=url, json=files_list)



if __name__ == "__main__":
    install_and_import('requests')

    # Searches repo for all solidity files
    filenames = find_solidity_files_in_repo()

    # Retrieves solidity files content
    files_list = retrieve_solidity_files(filenames=filenames)

    #Upload Files to Smartbugs
    sarif_results = upload_files_to_smartbugs(files_list=files_list)

    print(sarif_results.json())
