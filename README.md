CS109_Volcano
=============

Project by: Jocelyn Fuentes and Sierra Okolo
Date: 10 December 2014
Course: CS109 Final Project
Project: Volcanoes

Introduction
==============
There are several modules in this folder. A description of the modules is as follows:

FINAL.ipynb: This is the main IPython Notebook. Run this to see the major portion of our efforts

helper_files: This is a directory that holds all the data files referenced throughout our code. We put the files in this directory to remove the need to redo certain calculations.

ml.py: This is our machine learning module where the logic for Random Forest is contained

rose_plot: This is a directory that holds all the files that we used to build a rose plot, which is one of the visualizations that can be seen in the main IPYNB

stats.py: This is our main statistics module where our logic is contained for the Rayleigh test, as well as our code that uses a sinusoidal model to test for commonalities in frequency between number of eruptions and tidal forces

tidal_forces.*: These collection of files were created to calculate the force at any particular place on Earth at any given time. The output after running the Fortran code was very large set of files (on the order of 12GB).  To alleviate this, the output was broken into disjoint txt files and pickled after being run throug F2PY

volcano_gui.py: This is our main visualization. It is an animated plot that show the progression over time of the eruption of various volcanoes.  This must be run separately by typing "python volcano_gui.py" on the command line.  Given that it requires several dependencies, we will include it in our screen cast in case it is unable to be run.


Install Instructions
===========================
There are two main files, FINAL.ipynb and volcano_gui.py

The major additional dependencies include the following:

	basemap - a map toolkit: installation instructions can be found here (http://matplotlib.org/basemap/users/installing.html)
	pickle
	seaborn
	urllib2
	urllib
	json
	ConfigParser

 


