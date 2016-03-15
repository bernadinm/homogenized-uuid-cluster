import random
import os
import subprocess
import shlex

def main():
	serverNames = open('coreos-servers', 'r')
	firstPersonNames = open('names','r')
	listOfNames = [l.strip() for l in firstPersonNames]
	listOfServerNames = [s.strip() for s in serverNames]

	for names in listOfNames:
		homogenizedUuid = random.randint(1000, 2**31-2)
		cmd = "sudo useradd -u " + str(homogenizedUuid) + " " + names.lower()
		for server in listOfServerNames:
			print "The output is : " + "vagrant ssh " + server.strip() + " -c " + "'"  + cmd + "'" 
			process = subprocess.Popen(shlex.split("vagrant ssh " + server.strip() + " -c " + "'"  + cmd + "'"), shell=False,stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
			output,stderr = process.communicate()
			status = process.poll()
			print output

if __name__ == '__main__':
	main()