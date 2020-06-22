__author__ = '[Kamil Adamski](https://github.com/adamsqi)'
__date__ = '2020.06.21'

"""
This is a script for auto generation of README.md content. The script parses all .py script files within the repository and creates a README.md file.


Inspired by: [Brandon Amos](https://github.com/bamos/python-scripts/blob/master/README.md)
"""

import ast
import os
import re

from typing import List, Set

UNPARSABLE_FILES = ['.git', '.gitignore', 'README.md', 'generate_readme.py']
README_TEMPLATE = """This is a collection of short Python scripts I use as utility tools or just for testing of various features.

{content}
"""

def main():
    generator = ReadmeGenerator()
    generator.generate()

class ReadmeGenerator():
    def __init__(self):
        pass
        
    def generate(self):
        content = self._prepare_content()
        with open('README.md', mode='w') as f:
            ready_content = README_TEMPLATE.format(content=content)
            f.write(ready_content)
    
    def _prepare_content(self) -> str:
        scripts_finder = ValidScriptsFinder()
        valid_script_names = scripts_finder.find()
        content = self._get_all_content_from_scripts(script_names=valid_script_names)
        return content
        
    def _get_all_content_from_scripts(self, script_names: List[str]) -> str:
        content = ''
        script_names = sorted(script_names)
        for name in script_names:
            script_link = self._generate_script_link(script_name=name)
            meta_text = self._parse_single_file(name=name)
            content += '### ' + script_link + '\n\n' + meta_text + '\n\n\n'
        return content
        
    def _generate_script_link(self, script_name: str) -> str:
        url_base = 'https://github.com/adamsqi/python-scripts/blob/master/'
        url = url_base + script_name
        return f'[{script_name}]({url})'
    
    def _parse_single_file(self, name: str) -> str:
        content = self._read_file(file_path=name)
        meta_text = self._extract_doc_string(content)
        return meta_text
        
    def _read_file(self, file_path: str) -> str:
        with open(file_path, mode='r') as f:
            return f.read()
            
    def _extract_doc_string(self, content: str) -> str:
        ast_module = ast.parse(content)
        ast_f = ast.literal_eval
        author, date, doc_string = [ast_f(m.value) for m in ast_module.body[0:3]]
        
        return f"""
+ Author: {author}

+ Created at: {date}

#### Description: {doc_string}
"""
        

class ValidScriptsFinder():
    
    def __init__(self):
        pass
        
    def find(self) -> List[str]:
        script_names = self._get_valid_script_names_within_cwd()
        return script_names
     
    def _get_valid_script_names_within_cwd(self) -> List[str]:
        all_file_names = self._get_all_files_within_cwd()
        file_names = set(all_file_names) - set(UNPARSABLE_FILES)
        valid_file_names = self._exclude_files_with_ignored_extensions(file_names)
        return valid_file_names
        
    def _get_all_files_within_cwd(self) -> List[str]:
        files = [file for file in os.listdir(self._get_current_dir_path())]
        return files
        
    def _get_current_dir_path(self) -> str:
        dir_path = os.getcwd()
        return dir_path
        
    def _exclude_files_with_ignored_extensions(self, file_names: Set[str]) -> List[str]:
        ignored_extensions = self._read_git_ignore()
        result = [name for name in file_names if not any(sub in name for sub in ignored_extensions)]  # only files without ignored extensions
        return result
        
    def _read_git_ignore(self) -> List[str]:
        with open('.gitignore', mode='r') as f:
            data = f.read()
        data = data.split('\n')
        data = [el.replace('*', '') for el in data]
        return data
        
if __name__ == '__main__':
    main()