from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np
import logging
from sklearn import metrics
import time


# Setup logging for defect tracking
logging.basicConfig(filename='test_results.log', level=logging.INFO, format='%(asctime)s - %(message)s')
# read the dataset
data = pd.read_csv("C:\\Users\\vanam\\OneDrive\\文档\\Datasets\\house multi linear.csv")

print(data)
"""   area  bedrooms  age   price
0  2600       3.0   20  550000
1  3000       4.0   15  565000
2  3200       NaN   18  610000
3  3600       3.0   30  595000
4  4000       5.0    8  760000
5  4100       6.0    8  810000"""

"""functional testing"""
# check is there any null values if yes replace with the feature column mean
print("Null values are:\n", data.isnull().sum())
# null values in bedrooms feature, replace it with mean
data['bedrooms'] = data['bedrooms'].replace(np.nan, data['bedrooms'].mean())

# changing the bedrooms datatype from float to integer
data['bedrooms'] = data['bedrooms'].astype(int)

# print the data after modification
print("data after modification\n", data)
"""data after modification
    area  bedrooms  age   price
0  2600         3   20  550000
1  3000         4   15  565000
2  3200         4   18  610000
3  3600         3   30  595000
4  4000         5    8  760000
5  4100         6    8  810000"""

# Checking the null values
null = data.isnull().sum().sum()
logging.info(f'Null values : {null}')
if null != 0:
    logging.error(f'Test Case FAILED | Expected: 0 | Predicted:{null}')
    print(f'Test Case ❌ FAILED | Expected: 0 | Predicted: {null}')
else:
    print(f'Test Case ✅ PASSED | Expected: 0 | Predicted: {null}')

"""correctness testing"""
# for 3 coefficients the equation will be y=m1*x1+m2*x2+m3*x3+b
# Let
start_time = time.time()
m1, m2, m3 = 112.06244, 23388.88007, -3231.71790
intercept = 221323.00186

""" for the dataset let us test for the known values by using formula """
area = [4000, 3500, 3200, 2800]
bedrooms = [4, 6, 3, 2]
age = [30, 25, 27, 40]
actual_pred = []
# calculation using y=mx+b
for i, (a, b, a1) in enumerate(zip(area, bedrooms, age)):
    y1 = m1 * a + m2 * b + m3 * a1 + intercept
    actual_pred.append(y1)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time for manual: {execution_time:.6f} seconds")

# actual predictions are
"""[666177. 673082. 562833. 452607.]"""

#predicting the values for some test cases
# splitting the dataset
start_time = time.time()
x = data.iloc[:, :-1]
# checking if the x values are greater than 0
for i in x.values:
    if np.all(i[0])<=0:
        logging.error(f"Test Case Failed | Expected Greater than 0 | Predicted:{i}")
        print(f'Test Case ❌ FAILED | Expected: Greater than 0 | Predicted: {i}')
    else:
        print(f'Test Case ✅ PASSED | Expected: Greater than 0 | Predicted: {i[0]}')
y = data.iloc[:, -1]
# fitting the model
model = LinearRegression()
model.fit(x.values, y.values)
# predicting the values for test_cases
test_cases = [([4000, 4, 30], 666177), ([3500, 6, 25], 673082), ([3200, 3, 27], 562833), ([2800, 2, 40], 452607)]
inputs = [case[0] for case in test_cases]
expected_outputs = [case[1] for case in test_cases]
predictions = model.predict(inputs)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time for using model: {execution_time:.6f} seconds")
mae = metrics.mean_absolute_error(predictions, expected_outputs)
logging.info(f"mean absolute error is")
# checking the mean absolute error
if 0>=mae<=1:
    logging.error(f'Test Case FAILED | Expected: 0 To 1 | Predicted:{mae}')
    print(f'Test Case ❌ FAILED | Expected: 0 To 1 | Predicted: {mae}')
else:
    print(f'Test Case ✅ PASSED for mean absolute error| Expected: 0 To 1 | Predicted: {mae}')

mse = metrics.mean_squared_error(predictions, expected_outputs)
print("mean squared error is:", mse)
test_case = []
# Check results and log defects
for i, (pred, expected) in enumerate(zip(predictions, expected_outputs)):
    if abs(pred - expected) > 500:  # Acceptable error threshold: 5000
        logging.error(f'Test Case {i + 1} FAILED | Expected: {expected} | Predicted: {pred}')
        test_case.append(f'Test Case {i + 1} ❌ FAILED ')
    else:
        test_case.append(f'Test Case {i + 1} ✅ PASSED ')
# for sample data testing
df = pd.DataFrame(inputs, columns=['area', 'bedrooms', 'age'])
df['predicted'] = np.round(predictions).astype(int)
df['expected_outputs'] = expected_outputs
df['bias'] = df['expected_outputs'] - df['predicted']
df['test_case'] = test_case
print(df)
print(model.coef_)

