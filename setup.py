from cx_Freeze import setup, Executable
import os

build_exe_options = {
    'packages': ['os', 'sys', 'streamlit', 'pandas', 'matplotlib'],
    'includes': ['streamlit.web.cli', 'streamlit.runtime.scriptrunner.magic_funcs'],
    'include_files': [("icd10_app.py", "icd10_app.py"), ("df.csv", "df.csv")],
}

base = None
if os.name == 'nt':
    base = 'Win32GUI'

setup(
    name='ICD-10 HES Usage Visualiser',
    version='1.0',
    description='ICD-10 HES Usage Visualiser',
    options={'build_exe': build_exe_options},
    executables=[Executable('run.py', base=base)],
)
