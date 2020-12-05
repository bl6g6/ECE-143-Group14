### ECE 143--Final Project--Group 14
## cleaning data---by: Bing Li

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# read csv file
dataset = pd.read_csv('./vehicles.csv')

# show details
dataset.describe()

# #### There are car values with 0 prices, should be cleaned.
# #### max odometer are 10^7 miles, should be removed
# #### whole column of county is empty, should be removed.

# visulize first 5 rows of the data
dataset.head(5)

# #### There are columns such as "id", "url", "image_url", which are clearly nothing to do with car prices,
# should be removed.

# show summary of the data
dataset.info()

# #### The counts of some columns are not equal to count of index number, which means there are missing values among
# those features.

# # Cleaning data
# ### 1. remove outliers
# visualize car prices distribution
fig, ax = plt.subplots(figsize=(10, 2))
ax.set_title('Box plot of car price')
sns.boxplot(x='price', data=dataset)
##### There are some car prices that are so large that needs to be removed.


# remove outilers using interquartile range in terms of price colunm
init_size = dataset.count()['id']
q1 = dataset['price'].quantile(0.25)
q3 = dataset['price'].quantile(0.75)
iqr = q3 - q1  # Interquartile range
fence_low = q1 - 1.5 * iqr
fence_high = q3 + 1.5 * iqr
dataset = dataset.loc[(dataset['price'] > fence_low) & (dataset['price'] < fence_high)]
filtered_size = dataset.count()['id']
print(init_size - filtered_size, '(', '{:.2f}'.format(100 * (init_size - filtered_size) / init_size), '%', ')',
      'outliers removed from dataset')

## For odometer we do the similiar things
fig, ax = plt.subplots(figsize=(10, 2))
ax.set_title('Box plot of car odometer')
sns.boxplot(x='odometer', data=dataset)

# #### Odometer near or equal to zero is fine since the car could be very new, but some odometry like 10*7 miles is
# not possible, so we need to remove outpilers as well. This time we set a higher boundary to accept more samples.


# remove outilers using interquartile range in terms of price colunm
init_size = dataset.count()['id']
q1 = dataset['odometer'].quantile(0.25)
q3 = dataset['odometer'].quantile(0.75)
iqr = q3 - q1
dataset = dataset.loc[(dataset['odometer'] <= q3 + 3 * iqr)]
filtered_size = dataset.count()['id']
print(init_size - filtered_size, '(', '{:.2f}'.format(100 * (init_size - filtered_size) / init_size), '%', ')',
      'outliers removed from dataset')

# ### 2. drop uncorrelated columns

# #### We only keep columns that have impact on car prices. #### There are some columns that are obviously unrelated
# with car price such as id, url, title_status, image_url, vin(vehicle identity number), description, region_url,
# region and county(since it is a null column). Since model car models can represent their manufacturers,
# so we can drop manufacturer as well.

## determine how geographical coordinate affect car price
fig, ax = plt.subplots(figsize=(15, 10))
ax.set_title('Geographical distribution of the cars colored by prices')
sns.scatterplot(x='long', y='lat', data=dataset, hue='price', ax=ax)

# #### We can see that the used car geographical distribution is concentrate on the U.S. However, the distribution of
# car prices are very random, no direct relationship between price and latitude or longtitude. Thus, we could drop
# these columns.


## determine how states affect car price
fig, ax = plt.subplots(figsize=(15, 10))
ax.set_title('Mean car price of each state')
dataset.groupby(['state']).mean()['price'].plot.bar(ax=ax)

# #### We can see that state can affect car price to some extent, so we choose to keep this feature

# drop unnecessary columns
dataset = dataset.drop(
    columns=['id', 'url', 'region', 'region_url', 'title_status', 'vin', 'image_url', 'description', 'county', 'long',
             'lat'])

# ## 3. remove other impossible samples


# visualize relationship between prices and odometer.
fig, ax = plt.subplots(figsize=(20, 15))
ax.set_title('Scatter plot between car price and odometer')
sns.scatterplot(x='odometer', y='price', data=dataset)

# set a minimum threshold 1000 miles to make the car price reasonable
dataset = dataset[dataset['price'] > 1000]
# since the minimum car made year is 1900, car less than 1980 can cause too much uncertainty
dataset = dataset[dataset['year'] > 1980]
# # The cheapest new car is around 2000$, but here there are some with 1000$ around
# # so we set a boundary to the sum of price and odometer
dataset = dataset[(dataset['price'] + dataset['odometer']) > 2000]

# ## 3. Deal with missing samples.

# visualize how missing values are distributed in each remained columns.
fig, ax = plt.subplots(figsize=(10, 8))
ax.set_title('Distribution of the missing values (white lines)')
sns.heatmap(dataset.isnull(), yticklabels=False, cbar=False)

# #### We can see that 'size' has too many missing values, so we drop it.
# #### For those columns that have very few missing values, we delete those rows.
# #### Columns that have not too many and not too few missing values, we replace them with str 'null'.

# drop size column
dataset = dataset.drop(columns=['size'])
# delete the rows for those columns that have very few null values
the_columns = ['price', 'year', 'model', 'fuel', 'transmission', 'odometer', 'drive', 'type', 'paint_color', 'state']
for i in the_columns:
    dataset = dataset[dataset[i].notnull()]
# replace missing values with str 'null'.
dataset = dataset.replace(np.nan, 'null', regex=True)

# visualize whether there are missing values
fig, ax = plt.subplots(figsize=(10, 8))
ax.set_title('Distribution of the missing values (white lines)')
sns.heatmap(dataset.isnull(), yticklabels=False, cbar=False)

# ## 4. remove model with little samples

# #### To get better results, we remove those rows with model number less than 10.

dataset['model'].value_counts()

dataset = dataset.groupby('model').filter(lambda x: len(x) > 10)

dataset['model'].value_counts()

### 5. Remove duplicate rows
##### This could aviod overfitting and save computational time

dataset = dataset.drop_duplicates()

### Visualize and store dataset after data cleaning
dataset.info()

# store cleaned data
dataset.to_csv(r'./cleaned_df.csv', index=False)
