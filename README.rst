===========
RecruitAPI
===========

Description
------------

This is the command line tool to help you extract restaurant data from
Recruit Open API

Before you use
---------------
Make sure that you have the following environment ready and packages installed.

* Python 3.6
* pandas=0.23.4
* pyhdb=0.3.4

How to Use
-----------
After setting up the required environment, now you are ready to use the command line tool.
As an example, if you want to extract 300 records (default=200) of restaurant data,
specify 300 after the parameter -max, as shown here::

/Recruit API/cmdtool $ python main.py -max=200

For additional features, refer to the command_line help::

/Recruit API/cmdtool $ python main.py -h
