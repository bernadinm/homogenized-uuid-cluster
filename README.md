# homogenized-uuid-cluster

##Challenge Question
Create a python script that allows users to be created but maintain homogizined uuids across a series of nodes.

You can use the language of your choice to implement this solution. In the end, your code must be able to ssh on the machines ensure the users and uuids are the same.

## Solution

This program leverages vagrant to create coreos servers. This is meant simulate ssh calls on a remote machine. You specify the name of the vms in the coreos-servers file, user account names in the names file, and the uuids are randomly created from range 1000 to 2^31-2 which is the limit. I've implemented two version to this problem. 1) The first solution is speedy.py which will chunk all the request to add users in one request per server. 2) The second solution linear-deployer.py will make calls per user, however opening and closing ssh sessions adds a lot of delay. There is also a limit to how many arguments that can be passed in one line. This limit is set by the operating system. i.e getconf ARG_MAX. 

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

##Example output

   ```bash
   MacBook-Pro:dcos mingo$ python speed.py
   The output is : vagrant ssh core-01 -c 'sudo useradd -u 1694492165 paulette && sudo useradd -u 259025774 louise && sudo useradd -u 1445437099 tobie && sudo useradd -u 155613499 chasidy && sudo useradd -u 1217682952 edythe && sudo useradd -u 754110988 kandra && sudo useradd -u 742915194 thomasine && sudo useradd -u 1912226146 fatima && sudo useradd -u 1189503750 yun && sudo useradd -u 1424009968 carleen && sudo useradd -u 1102964481 boris && sudo useradd -u 765269926 claudette && sudo useradd -u 2145117381 alejandro && sudo useradd -u 67079324 max && sudo useradd -u 1073948180 nell && sudo useradd -u 1899789186 lucia && sudo useradd -u 932478187 monty && sudo useradd -u 1626674136 eleni && sudo useradd -u 326676961 palma && sudo useradd -u 1715264531 sandra && sudo useradd -u 789852135 lydia && sudo useradd -u 896466640 zaida && sudo useradd -u 644629764 cristopher && sudo useradd -u 749668699 jonelle && sudo useradd -u 1964225264 bong && sudo useradd -u 915461925 rosalie && sudo useradd -u 1803158971 kerri && sudo useradd -u 1033236007 floretta && sudo useradd -u 687533719 leola && sudo useradd -u 1170572488 arthur && sudo useradd -u 1818021014 glynda && sudo useradd -u 541840683 kendrick && sudo useradd -u 508992946 cinthia && sudo useradd -u 1360097370 alexia && sudo useradd -u 1085592141 antonette && sudo useradd -u 1670003351 katy && sudo useradd -u 155494826 stefania && sudo useradd -u 744150050 lewis && sudo useradd -u 349378686 josephina && sudo useradd -u 703256810 claudio && sudo useradd -u 487612663 janina && sudo useradd -u 1616725716 charity && sudo useradd -u 1205562326 tilda && sudo useradd -u 477629922 shiloh && sudo useradd -u 208553836 melani && sudo useradd -u 1581029310 cristine && sudo useradd -u 76027967 suzanne && sudo useradd -u 314053758 tamesha && sudo useradd -u 1499237101 prince && sudo useradd -u 361961106 jerome'
   ```
