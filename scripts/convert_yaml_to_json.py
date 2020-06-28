__author__ = '[Kamil Adamski](https://github.com/adamsqi)'
__date__ = '2020.06.28'

"""
This module converts a yaml file to the json file.

Results:

##### yaml file
```yaml
object: foo
meta:
    name: foo
    type: foo_type
    class: foo_class
---
object: moo
meta:
    name: moo
    type: moo_type
    class: moo_class
```

# json file (after conversion)
```json
[{
    "meta": {
        "class": "foo_class",
        "name": "foo",
        "type": "foo_type"
    },
    "object": "foo"
}, {
    "meta": {
        "class": "moo_class",
        "name": "moo",
        "type": "moo_type"
    },
    "object": "moo"
}]
```
"""

import json
import yaml

from typing import Any, Dict, List
from yaml.composer import ComposerError

def convert_yaml_file_to_json_objects(yaml_fn: str, split_by: str='---') -> List[Dict[str, Any]]:
    """Convert the yaml file to the list of dicts i.e. a json representation
    There might be two types of yaml files:
    1) yaml objects separated by split string
    2) yaml objects without any separating string
    If the yaml file doesn't comprise of any separating string then
    leave the 'split_by' argument empty.
    """
    with open(yaml_fn, mode='r') as f:
        document = f.read()

    if split_by in document:
        doc_container = document.split(split_by)
    else:
        doc_container = [document]

    dict_list = []
    for doc in doc_container:
        try:
            dict_ = yaml.safe_load(doc)
            dict_list.append(dict_)
        except ComposerError as e:
            print('The separator the in yaml file might be wrongly defined. Error: {}'.format(e), flush=True)
    return dict_list

    
def save_json_in_file(document: List[Dict[str, Any]], file_name: str) -> None:
    document = str(document)
    json_str = document.replace("\'", "\"")  # replace single quite with double quotes
    json_formatted_str = json.dumps(document, indent=2)
    with open(file_name + '.json', mode='w') as f:
        f.write(json_str)
  
if __name__ == '__main__':
    file_name = 'example'
    document = convert_yaml_file_to_json_objects(file_name + '.yaml')
    save_json_in_file(document=document, file_name=file_name)