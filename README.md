# ECE-143-Group14-Final project
## Used Car Price Prediction
### Teammates: Bing Li, Jie Wu, Atman Patel, Shang Wang
This repo contains the code, dataset, presentation file and graphs for the ECE 143-Group 14 

# Dataset
[Craigslist](https://www.kaggle.com/austinreese/craigslist-carstrucks-data)
is the world's largest collection of used vehicles for sale,this data is scraped every few months, it contains most all relevant information that Craigslist provides on car sales including columns like price, condition, manufacturer, latitude/longitude, and 18 other categories. Since the dataset is large, we've only included the cleaned dataset in our github repo.

# File Structure:
    | - data
        | - maps - contains the files needed to plot the cloropleth (US states) maps
        | - cleaned_df.csv (created by Data_Cleaning.py)
    | - scripts
        | - data_cleaning.py is the code file to proceed data cleaning.
        | - prediction.py is the code file to train a model and predict.
    | - All_visuals.ipynb - contains all the important visualizations
    | - UI
        | - user_interface.py - contains the script to run user interace for prediction
    | - plots
        | - prediction_results - contains all the performance metrics in form of plots
        | - data_analysis - contains the trends found in data
    | - Presentation.pdf is the final presentation file of our project.
    | - README.md

# How to Run the Code:
- Prediction: python scripts/prediction.py
    
# Third-party modules:
    numpy
    pandas
    seaborn
    math
    matplotlib
    scikit-learn
    geopandas


