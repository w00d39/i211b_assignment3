import pandas as pd
"""
Will be using snake case for this assignment for consistency as the columns are snake case in the csv files.
Uncomment the print statments to see the output of the functions for correlation
"""

try:
# Load the data
    petal_df = pd.read_csv('Petal_Data.csv') #load the petal data
    petal_df = petal_df.drop(columns=['Unnamed: 0']) #drop the unnamed column


    sepal_df = pd.read_csv('Sepal_Data.csv') #load the sepal data
    sepal_df = sepal_df.drop(columns=['Unnamed: 0']) #drop the unnamed column

    # Merge the two dataframes
    iris_df = pd.merge(petal_df, sepal_df)
    # Group the data by species
    iris_species = iris_df.groupby('species')

    #testing/ lil taste of the data plus making sure it merged correctly
    #print(iris_df.head(5))
    #print(iris_df.shape)



except FileNotFoundError: #catch the file not found error
    print("File not found")

def corr_iris(): #function to calculate the correlation of the iris data
    num_columns = iris_df.select_dtypes(include=['float64']).columns #select the columns that are float64 so it does not error out
    iris_corr = iris_species[num_columns].corr() #calculate the correlation between variables for each iris species 
    return iris_corr #return the correlation


def avg_iris (): #function to calculate the average of the iris data
    
    avg_sepial_length = iris_species['sepal_length'].mean()
    avg_sepial_width = iris_species['sepal_width'].mean()

    avg_petal_length = iris_species['petal_length'].mean()
    avg_petal_width = iris_species['petal_width'].mean()

    avg_iris_df = pd.DataFrame({'species': avg_sepial_length.index,
                                'avg_sepial_length': avg_sepial_length.values,
                                'avg_sepial_width': avg_sepial_width.values, 
                                'avg_petal_length': avg_petal_length.values,
                                'avg_petal_width': avg_petal_width.values})
    
    return avg_iris_df

def median_iris (): #function to calculate the median of the iris data

    median_sepial_length = iris_species['sepal_length'].median()
    median_sepial_width = iris_species['sepal_width'].median()

    median_petal_length = iris_species['petal_length'].median()
    median_petal_width = iris_species['petal_width'].median()

    median_iris_df = pd.DataFrame({'species': median_sepial_length.index,
                                   'median_sepial_length': median_sepial_length.values,
                                   'median_sepial_width': median_sepial_width.values,
                                   'median_petal_length': median_petal_length.values,
                                   'median_petal_width': median_petal_width.values})
    return median_iris_df

def sd_iris (): #function to calculate the standard deviation of the iris data

    sd_sepial_length = iris_species['sepal_length'].std()
    sd_sepial_width = iris_species['sepal_width'].std()

    sd_petal_length = iris_species['petal_length'].std()
    sd_petal_width = iris_species['petal_width'].std()

    sd_iris_df = pd.DataFrame({'species': sd_sepial_length.index,
                                'sd_sepial_length': sd_sepial_length.values,
                                'sd_sepial_width': sd_sepial_width.values,
                                'sd_petal_length': sd_petal_length.values,
                                'sd_petal_width': sd_petal_width.values})
    return sd_iris_df


print(avg_iris())
print(median_iris())
print(sd_iris())
print(corr_iris())

"""

The versicolor irises and the virginica irises are the most similar because they are the closest to each other based on mean, median, standead deviation, and correlation.
 Especially when looking at the petals half of the columns they are the closest to each other. Yet in the correlation matrix they have more differing points yet not enough for them to be closer to the setsosa iris.
The setsosa irises are the least similar because it is not as close to the others when looking at the variety of stats and the correlation matrices. The only way that it could be argued otherwise is on sepial width 
they tend to be closer to the versicolor irises. But anywhere else that iris is the third wheel in the group. To be honest though they are all similar and there is no in your face value difference when looking at the 
stats and correlation matrices yet still versicolor and virginica irises are the most similar out of the three.

"""