import os

path_of_base_enviroment=input('path of base enviroment : ')
os.system(os.path.join(f'{path_of_base_enviroment}', 'activate.bat'))
path=input('enter project path : ')
project_name=os.path.split(path)
if project_name[0]=='':
    os.system(f"django-admin startproject {project_name[1]}")
else:
    os.chdir(f'{project_name[0]}')
    os.system(f"django-admin startproject {project_name[1]}")   




# pip install pyinstaller
# pyinstaller autocreateproject.py --onefile

