import os

try:
    os.system('django-admin --version')
except:
    os.system('pip install django')

path=input('enter project path : ')
project_name=os.path.split(path)
if project_name[0]=='':
    os.system(f"django-admin startproject {project_name[1]}")
else:
    os.chdir(f'{project_name[0]}')
    os.system(f"django-admin startproject {project_name[1]}")   

# pip install pyinstaller
# pyinstaller autocreateproject.py --onefile

