import numpy as np
import pandas as pd

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression, SGDRegressor, RidgeCV, SGDRegressor
from sklearn.ensemble import RandomForestClassifier, ExtraTreesRegressor, BaggingRegressor, AdaBoostRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import r2_score

import matplotlib.pyplot as plt


def convert_to_onehot(df, columns):
    """
    Description:    Function to convert categorical columns to onehot columns
    Parameters:     df - the dataframe in question
                    columns - categorical columns to convert to onehot 
    Return:         dataframe with onehot columns
    """
    df_dummy = pd.get_dummies(df, columns=columns)
    # df_dummy.drop(columns=columns, inplace=True)
    return df_dummy

def process_features(df):
    """
    Description:    Convert all the features into a form that is ingestible by the ML pipeline
    Parameters:     df - Cleaned dataframe (after running data_cleaning.py)
    Return:         Dataframe with processed features - ready for prediction task
    """

    ## TODO: Do this in data cleaning
    
    df = df.drop(columns=['model'])
    ## We will handle the categorical columns by using onehot encoding 
    onehot_these_columns = ["manufacturer","condition","fuel","transmission","drive","type","paint_color"]
    df = convert_to_onehot(df, onehot_these_columns)
    ## Year
    df['year'] = df['year']-df['year'].min()

    ## Cylinders
    mean_cylinder = (4+6+8)/3
    replace_cylinders = {'3 cylinders':3, '4 cylinders':4, '5 cylinders':5, 
            '6 cylinders':6, '8 cylinders':8, '10 cylinders':10, 
            '12 cylinders':12, 'null':mean_cylinder, 'other':mean_cylinder}
    df['cylinders'].replace(replace_cylinders, inplace=True)

    ## State
    state_buckets = {}
    for k,v in dict(df.groupby("state")['price'].mean()).items():
        state_buckets[k] = int(v/1000)
    df['state'].replace(state_buckets, inplace=True)

    return df


def loss_MSE(y_true, y_pred):
    return mean_squared_error(y_true, y_pred)**0.5

# find whether our prediction is correct within a certain threshold
def accuracy(y_true, y_pred, thresh=100):
    return np.sum(np.where(abs(y_true-y_pred)<thresh, 1, 0)) / len(y_true)

def acc_r2(y_true, y_pred):
    return round(r2_score(y_true, y_pred) * 100, 2)

def get_results(model, y_train, y_test, y_pred_train, y_pred_test, threshold):
    mse_train = loss_MSE(y_train, y_pred_train)
    mse_test = loss_MSE(y_test, y_pred_test)
    acc_train = accuracy(y_train, y_pred_train, threshold)
    acc_test = accuracy(y_test, y_pred_test, threshold)
    r2_train = acc_r2(y_train, y_pred_train)
    r2_test = acc_r2(y_test, y_pred_test)
    return mse_train, mse_test, acc_train, acc_test, r2_train, r2_test

def save_plots(f_path, results):

    ax1 = results.set_index('model_name')[['mse_test','mse_train']].plot(kind='bar', grid=True, title='Mean Squared Error')
    plt.xticks(rotation=45)
    ax1.figure.savefig(f_path + '/mse.png', bbox_inches='tight')

    ax2 = results.set_index('model_name')[['acc_test','acc_train']].plot(kind='bar', grid=True, title='Accuracy')
    plt.xticks(rotation=45)
    ax2.figure.savefig(f_path + '/accuracy.png', bbox_inches='tight')

    ax2 = results.set_index('model_name')[['r2_test','r2_train']].plot(kind='bar', grid=True, title='R2 Score')
    plt.xticks(rotation=45)
    ax2.figure.savefig(f_path + '/r2 score.png', bbox_inches='tight')

def predict(df):
    """
    Description:    Run predictive ML algorithms on the processed features and provide results
    Parameters:     df - processed df ready for ML pipeline
    Return:         Performance results
    """

    model_results = dict()

    models = {'Linear Regression':LinearRegression(), 'Extra Trees Regression':ExtraTreesRegressor(max_depth=18),
    'Bagging Regression':BaggingRegressor(), 'Ridge Regression':RidgeCV(), 'AdaBoost Regression':AdaBoostRegressor(),
    'Decision Tree Regression':DecisionTreeRegressor(max_depth=15)}

    y = df['price']
    X = df.drop(columns=['price'])

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=1, shuffle=True)

    threshold = 2000

    results = {'model_name':[], 'mse_train':[], 'mse_test':[], 
                'acc_train':[], 'acc_test':[], 'r2_train':[],'r2_test':[]}


    for name,model in models.items():
        print("\n-------------- ",name," --------------")
        model.fit(X_train, y_train)
        train_pred = model.predict(X_train)
        test_pred = model.predict(X_test)

        mse_tr, mse_te, acc_tr, acc_te, r2_tr, r2_te = get_results(model, y_train, y_test, \
                                                                    train_pred, test_pred, threshold)
        
        print("Train: MSE = {}, Accuracy = {}, R2 Score = {}".format(mse_tr, acc_tr, r2_tr))
        print("Test: MSE = {}, Accuracy = {}, R2 Score = {}".format(mse_te, acc_te, r2_te))

        results['model_name'].append(name)
        results['mse_train'].append(mse_tr)
        results['mse_test'].append(mse_te)
        results['acc_train'].append(acc_tr)
        results['acc_test'].append(acc_te)
        results['r2_train'].append(r2_tr)
        results['r2_test'].append(r2_te)

    df_results = pd.DataFrame(results)

    
    save_plots(f_path = "prediction_plots", results=df_results)


if __name__=="__main__":
    ## import data
    print("Importing Data")
    df_cleaned = pd.read_csv('cleaned_df_with_manufact.csv', keep_default_na=False)

    print("Processing features")
    df_processed = process_features(df_cleaned)
    
    print("Running the model and saving results as plots")
    predict(df_processed)

    print("\n\nSUCCESSFULLY COMPLETED")


