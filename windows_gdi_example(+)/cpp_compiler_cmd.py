'''
cpp_compiler, cmd version 1.0.1
'''
import sys
import os
import ctypes
import subprocess

def script_path():
    path = os.path.realpath(os.path.dirname(sys.argv[0]))
    os.chdir(path)
    return path
    
def compile(file, quiet):
    try:
        ''' mingw downloaded from https://sourceforge.net/projects/mingw-w64/ '''
        compilerPath = "D:\\Programy\\mingw\\mingw64\\bin\\g++.exe"          # path to exe file
        # commands = [compilerPath, "-v", "-o", file.split('.')[0] + ".exe", file]
        # commands = [compilerPath, "-o", file.split('.')[0] + ".exe", file]
        commands = [compilerPath, "-o", file.split('.')[0] + ".exe", file, '-lgdiplus', '-lgdi32']      # for GDI
        help = [compilerPath, "--help"]
        info = subprocess.getoutput(commands)
        if not quiet:
            print(info)
        return True
    except:
        return False
    
def run(file):
    try:
        commands = [file]
        subprocess.call(commands)
        return True
    except:
        return False
        
        
if __name__ == "__main__":
    # ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)
    path = script_path()
    args = sys.argv[1:]
    args = ['gdi_example.cpp']
    fileName = os.path.basename(sys.argv[0]).lower()
    if 'q' in fileName.lower():
        quiet = True
    else:
        quiet = False
    # args = ['some.cpp']     # remove that before running pyinstaller!!!
    if args:
        file = args[0]
        if file.endswith(".cpp"):
            status = compile(file, quiet)
            operation = "compile"
        elif file.endswith(".exe"):
            status = run(file)
            operation = "run_exe"
        else:
            print(">>> wrong file format: {}".format(file))
            status = False
            operation = "None"
        print(">>> operation->  <{}>\n    file------>  <{}>\n    status---->  <{}>".format(operation, file, status))
    else:
        print(">>> specify .cpp or .exe file as argument")
    input(">>> press enter to exit... ")
    
'''
info:
    -i think it need to be cleared
    
'''
