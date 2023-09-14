# ORPER SCHOOL PROJECT

Repository containing a code to process a set of inputs and return output data. For confidentiality, the input data are not available and a test subject was added.

# Architecture of the code
Main Code: ExtractData.py : This code is used to set up the initial variables such as which subject, with or without a mask etc.
ExtractData.py then calls PreProcessingFucntions.py : This code will simply modfy the row index, columns index of the data from the selected subject. 
Finally, CalculationFucntion.py will be used to normalise the data and extract the final dataframe.

Structure: ExtractData.py > Calls i) PreProcessingFucntions.py then call ii) CalculationFucntion.py 

# Python Version and Requirement
Python 3.8
With the librairies:
  - pandas as pd # version 2.1.0
  - numpy as np # version 1.25.2
  - seaborn as sns # version 0.12.2
  - matplotlib.pyplot as plt # version 3.7.3

# Authors
- [@oTomo](https://www.github.com/Thomas-Paul-Fr)
