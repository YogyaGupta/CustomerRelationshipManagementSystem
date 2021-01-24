import sys

from cx_Freeze import *
includefiles = ['customer.ico']
excludes = []
packages = []
base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

shortcut_table=[
    ('DesktopShortcut', # Shortcut
     'DesktopFolder', # Directory_
     'CustomerRelationshipManagementSystemComplete', # Name
     'TARGETDIR' , # Component_
     '(TARGETDIR)\CustomerRelationshipManagement.exe' , # Target
     None, #Arguments
     None, #Description
     None, #Hotkey
     None, #Icon
     None, #IconIndex
     None, #ShowCmd
     'TARGETDIR', #WkDir
    )
]
msi_data = {'Shortcut': shortcut_table}

bdist_msi_options = {'data' : msi_data}
setup(
    version='0.1',
    description='Customer Relationship Management System Developed by Tanya Nebhwani and Yogya Gupta',
    name='Customer Relationship Management System',
    options={'build.exe' : {'include_files' : includefiles}, 'bdlist_msi' : bdist_msi_options,},
    executables=[
        Executable(
            script='customer_relationship.py',
            base=base,
            icon='customer.ico',
        )
    ]
)