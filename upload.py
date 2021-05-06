from os import walk

import requests

url = "http://18.224.107.59:5000/"


def find_solidity_files_in_repo():
    solidity_files = []
    for root, dirs, files in walk('./'):
        for file in files:
            if file.endswith('.sol'):
                solidity_files.append(root + '/' + file)
    return solidity_files


def create_body(user_hash, tools):
    return {
        'user-hash': user_hash,
        'tools': tools
    }


def upload_files_to_smartbugs(filenames, body):
    files_dict = {}
    for name in filenames:
        f = open(name, 'rb')
        files_dict[name] = f

    response = requests.post(url=url, data=body, files=files_dict)

    # Close files
    for file in files_dict.values():
        file.close()
    return response


if __name__ == "__main__":
    # Searches repo for all solidity files
    filenames = find_solidity_files_in_repo()

    # Create Body Data
    body = create_body(user_hash='0001testvalue', tools='oyente')

    # Upload Files to Smartbugs
    sarif_results = upload_files_to_smartbugs(filenames=filenames, body=body)

    # Save SARIF file on user repo
    with open('results.sarif', 'w') as sarif_file:
        sarif_file.write(sarif_results.text)
