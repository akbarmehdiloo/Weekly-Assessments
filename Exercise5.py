#Akbar Mehdiloo

import pandas as pd     #Pandas is a Python module,
iris= pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data')   # This is where I am downloading the dataset using read_csv
iris_cols=['Petal Length', 'Petal Width', 'Sepal Length','Sepal Width','Class']  # created new variable called iris_cols
iris.columns = iris_cols    # each of the column header will be equal to iris_cols
iris.drop('Class',axis=1,inplace=True)   # This will ignor the Class data series as we are intrested on numerical values
print(iris)

