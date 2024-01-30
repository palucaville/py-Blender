# fetchBTC.py
A Blender script** to fetch the price of Bitcoin in US dollars.

https://youtu.be/wnJzZx4RdkA?si=cMNmbFgu5Y87s__D

Blender is a Open Source program to create 3d object, texture and animate. 
By using the pyhong bge module "bpy" we can interact and extend the program.

The script will use Python **requests** to call Coindesk API for the current price of Bitcoin, get the current time-date from the system, turn the strings  into text objects and render them.
At each run all objects are given a **random ** color and moved down.
The number of lines and the requests time interval can be easily set.

How to use:
Open Blender
- delete the Cube and hide the Camera.(or they will be pushed down)
- in the Script Tab Open fetchBTC.py or paste it into a new file.
- adjust the number of times to fetch and the time interval
= click Run

**python requirements:
requests==2.28.2**

from cmd line:
 - curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
 - python get-pip.py
 - pip install requests

todo:
more interaction
fetching different crypto
...
