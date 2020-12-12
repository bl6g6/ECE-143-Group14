# ECE-143-Group14-Final project
## Used Car Price Prediction
### Teammates: Bing Li, Jie Wu, Atman Patel, Shang Wang
This repo contains the code, dataset, presentation file and graphs for the ECE143-Group 14 

# Dataset
[Craigslist](https://www.kaggle.com/austinreese/craigslist-carstrucks-data)
is the world's largest collection of used vehicles for sale,this data is scraped every few months, it contains most all relevant information that Craigslist provides on car sales including columns like price, condition, manufacturer, latitude/longitude, and 18 other categories

# Files:
    | - data
        | - cleaned_df.csv (created when Data_Cleaning.py)
    | - scripts
        | - py files
            | - Data_Cleaning.py is the code file to proceed data cleaning.
            | - Visulization.py is the code file to visualize data.
            | - prediction.py is the code file to train a model and predict.
        | - ipynb file
            | - run_all.ipynb - combination of all codes
    | - graphs
        | - graphs is the folder that saves our useful grapsh during this project. 
 

# Third-party modules:
    import numpy as np
    import pandas as pd
    import seaborn as sns
    import matplotlib.pyplot as plt


