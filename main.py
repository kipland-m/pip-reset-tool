import os 
import sys

class PipResetTool:
    def __init__(self):
        self.file_name = sys.argv[0]
        self.flag = sys.argv[1]
        # this will store all library to reinstall
        self.args = list(sys.argv[2].split(","))

    def pip_reset_tool(self):

        if self.flag == '-f':
            pass
        else:
            print('use -f')
            
        print('{}{}'.format("name of the file=",self.file_name))
        print('{}{}'.format("flag=",self.flag))
        print('{}{}'.format("library(s) to keep=",self.args))

    # this method will run on -f flag
    def fresh(self):
        pass

    # this method will call when -m flag is used
    def maintain(self):
        # this method will access self.args for installing selected libraries
        pass

    def install_pip(self):
        pass

    def nuke_pip(self):
        pass

    def install_packages(self):
        pass


p = PipResetTool()
p.pip_reset_tool()