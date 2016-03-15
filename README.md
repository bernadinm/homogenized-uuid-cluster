# homogenized-uuid-cluster

##Challenge Question
Create a python script that allows users to be created but maintain homogizined uuids across a series of nodes.

You can use the language of your choice to implement this solution. In the end, your code must be able to ssh on the machines ensure the users and uuids are the same.

## Solution

This program leverages vagrant to create coreos servers; this is meant simulate ssh calls on a remote machine. You specify the name of the vms in the coreos-servers file, user account names in the names file, and the uuids are randomly created from range 1000 to 2^31-2 which is the limit.

## Requirements

 * Python 2.7
 * Vagrant
 
### Quick Start

1. Clone this repository  

    ```bash
    git clone http://github.com/bernadinm/homogenized-uuid-cluster 
    ```

2.  Start your 6 coreos vms

	```bash
	vagrant up 
	```

3. Deploy homogenized uuids

   ```bash
   python speedy.py 
   ```
