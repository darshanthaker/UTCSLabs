import sys
import os
import logging
import socket
import time
import subprocess
import threading

class Command(object):
    def __init__(self, cmd):
	self.cmd = cmd
	self.process = None

    def run(self, timeout):
	def target():
      	    self.process = subprocess.Popen(self.cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
 	    (out, err) = self.process.communicate()

	#Start thread with target as the command to be run.	
	thread = threading.Thread(target=target)
	thread.start()	

	#Wait for however long timeout is.	
	thread.join(timeout)
	if (thread.is_alive()):
	    self.process.terminate()
	    thread._Thread__stop()
	    #Takes too long, so return success value = False
	    return False
	#Command finished successfully, so success value = True
	else:
	    return True

def main():
    command = Command("curl -L apps.cs.utexas.edu/unixlabstatus/ > ~/UTCSLabs/labstatus.txt")
    success = command.run(timeout=10)
    path = os.path.expanduser('~/UTCSLabs/labstatus.txt')
    with open(path) as file:
        while True:
            line = file.readline()
            if ('<td style="background-color: white; text-align:  left;">') in line:
                file.readline()
                file.readline()
                line2 = file.readline()
                if "0" in line2:
                    pos1 = line.find(">")
                    line = line[pos1:] 
                    pos2 = line.find("<")
                    line = line[1:pos2]
                    path2 = os.path.expanduser('~/UTCSLabs/ssh.txt')
                    file2 = open(path2, "w")
                    file2.write(line)
                    file2.close() 
                    break

if __name__ == '__main__':
    main()
