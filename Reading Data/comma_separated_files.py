import pandas as pd

# Define the column names as a list
names = ['age', 'workclass', 'fnlwgt', 'education', 'educationnum', 'maritalstatus', 'occupation', 'relationship', 'race',
        'sex', 'capitalgain', 'capitalloss', 'hoursperweek', 'nativecountry', 'label']

# CSV doesn’t have column names, names should be and supplied
# Read in the CSV file from the webpage using the defined column names
df = pd.read_csv("./data/adult.data", header=None, names=names)
                      
print(df.head())