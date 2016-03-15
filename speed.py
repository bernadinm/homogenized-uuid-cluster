import random
import os
import subprocess
import shlex

def main():
	serverNames = open('coreos-servers', 'r')
	firstPersonNames = open('names','r')
	listOfNames = [l.strip() for l in firstPersonNames]
	listOfServerNames = [s.strip() for s in serverNames]
	dictofNamesPlusId = {name : random.randint(1000, 2**31-2) for name in listOfNames}

	cmd = "sudo"
	for names, nameid in dictofNamesPlusId.iteritems():
		if cmd == "sudo":
			cmd = cmd + " useradd -u " + str(nameid) + " " +  names.lower() 
		else:
			cmd = cmd + " && sudo useradd -u " + str(nameid) + " " +  names.lower() 

	for server in listOfServerNames:
		print "The output is : " + "vagrant ssh " + server.strip() + " -c " + "'"  + cmd + "'" 
		process = subprocess.Popen(shlex.split("vagrant ssh " + server.strip() + " -c " + "'"  + cmd + "'"), shell=False,stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
		output,stderr = process.communicate()
		status = process.poll()
		print output

if __name__ == '__main__':
	main()