# Lab2_task3

the link to pythonanywhere: http://sofiiayamkova.pythonanywhere.com/

This task is to create a web app, with which you can display on the map data about friends (people you are subscribed to) of the specified account on Twitter.


There is a directory in which we have some files:
1) app.py has 2 functions. The first one returns a html form and the second one "draws" everything on the map. This program "takes" data from twitter_tools.py
2) Templates is the directory with html file(index), which is a result of the prigramm app.py. This in a html form, where you can enter users screen name.
3) twitter_tools.py has one main function get_frends. It returns a list of screen names and coordinates of the location. If there are no data from Twitter, it works with file "friends.json", if there is - from the Twitter IP.

Example of the look of web-app from the very beggining:

![image](https://user-images.githubusercontent.com/96056537/154680946-df31acf1-995c-4c27-9cea-23c110b3b7de.png)

Example of the map on pythonanywhere.com(of the screenname, that was on the previous photo):

![image](https://user-images.githubusercontent.com/96056537/154680517-6f30157c-bef8-40e5-9f11-96836ab0c026.png)
