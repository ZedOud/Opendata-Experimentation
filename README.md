##Opendata-Experimentation

###Purpose
This demonstrates the use of the csv module and matplotlib to parse data. The included data was downloaded from a publicly available Phoenix police opendata website. An attempt was made to introduce special structures from collections like defaultdict and Counter.

###Description
This script grabs the datetime data from each recorded crime incident and group crimes by category in crimes. Than I graphed the number of frequency of crimes in each category by the time of day. This results in a graph of the frequency of certain types of crimes depending on the time of day.

###Note
You can uncomment
  {line 27: i -= 1}
to limit the number of entries pulled from the data.

Why not use a slice in this line?
  {line 23: for row in r:}
Again, this is an introductory example that was meant to be run through quickly, so it's much faster to un/comment line 27 than to change the indexes of a slice on line 23.

###Results
####Presentation
I was attempting to introduce freshman and sophomore students to a simple application of data visualization and analysis techniques. I wanted to introduce various techniques, especially those unique and easily accessible to Python, that would abstract portions of the process.

  Although the code contained no comments, it served as a presentation piece, and my audience was able to walk away with a few new tools under their belt. The next week a few came back with their own exploration of the data.

####Experiment
As for the actual data experiment performed, I was trying to find patterns in the times of day of various crimes. I imagined this as an exercise to produce persuasive data for recommendations to concerned parties about when they should be concerned most about certain crimes occurring.

  The results certainly changed some preconceptions I had of the times of day that certain types of crimes occur. The results are quite remarkable. I will attempt to post a screencap of the results of running this script in the future.
