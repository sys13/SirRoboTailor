SirRoboTailor
=============

Uses a neural net to process tailor measurements

I wrote a little machine intelligence script that can be used to help your tailors make better sizing choices, train new tailors, or perhaps replace tailors. It uses a library called PyBrain to do the machine intelligence. The program is trained with the data.csv data, inputting height, weight, age, the user's inputted measurements, and manually tailor adjusted measurements. The program takes in height, weight, age, the user's inputted measurements and outputs automated tailor adjusted measurements.
The program could be improved by auto correcting for unit misinput, though perhaps the website could do also let the user know when something seems to be in the wrong units.

Here's how to run it:
1) Download and install python 2.7
http://www.python.org/download/
2) Install pip (it's a package manager)
http://www.pip-installer.org/en/latest/installing.html
3) install pybrain, 
from the command line:
pip install pybrain
4) Install scipy and numpy (if on Windows: http://www.lfd.uci.edu/~gohlke/pythonlibs/)
5) cd to the directory that contains the data.csv and __init__.py files
for example:
cd C:\SirRobotTailor
6) Run the python script from command line
python __init__.py

To modify the data
1) in data.csv keep inputs (est) on the left, and outputs (act) on the right (est=estimated, act=actual) 
2) you can put in more inputs and outputs if you like
3) if you change the number of inputs or outputs make sure to change the number in the __init__.py file (new one attached to this email) 
Currently set as:
numberOfInputs = 7
numberOfOutputs = 4 

Output
The error rates are high but it's using made up and very limited data. Here is the output on my fake data.
out:     [2.433 , 3.943 , 18.007, 19.501]
correct: [3.1   , 5.3   , 23    , 20.1  ]
error:  13.78811793

out:     [2.433 , 3.943 , 18.007, 19.501]
correct: [6.3   , 10.5  , 5     , 32    ]
error:  191.67073394

out:     [2.433 , 3.943 , 18.007, 19.501]
correct: [7.6   , 9.4   , 38    , 35    ]
error:  348.21014011

