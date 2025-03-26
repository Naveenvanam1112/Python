1. Functional Testing
Null Value Check: The script checks for null values in the dataset and replaces any null values in the bedrooms column with the mean of that column. It logs the number of null values and checks if it equals zero, indicating that there are no missing values.
Data Type Check: The code converts the bedrooms column from float to integer after handling null values.
2. Correctness Testing
Manual Calculation: The script manually calculates expected outputs using a predefined linear equation based on the coefficients and intercept. This serves as a baseline to compare against the model's predictions.
Model Predictions: The script fits a linear regression model to the dataset and makes predictions for specific test cases. It compares these predictions against expected outputs to verify the model's accuracy.
3. Performance Testing
Execution Time Measurement: The script measures the execution time for both the manual calculations and the model predictions. This helps assess the efficiency of the model.
4. Error Metrics Testing
Mean Absolute Error (MAE): The script calculates the mean absolute error between the model's predictions and the expected outputs. It checks if the MAE falls within an acceptable range (0 to 1) and logs the result.
Mean Squared Error (MSE): The script calculates the mean squared error of the predictions, providing another measure of the model's accuracy.
5. Defect Tracking
The script logs any discrepancies between expected and predicted values, including cases where the absolute difference exceeds a specified threshold (500 in this case). It logs these results for further analysis.
Summary of Tests Conducted
Null Value Handling: Ensures no null values remain in the dataset.
Data Type Validation: Confirms that the data types are appropriate for modeling.
Correctness of Predictions: Validates that the model's predictions are close to expected values.
Performance Metrics: Measures execution time and error metrics (MAE, MSE) to evaluate model performance.
Logging and Defect Tracking: Records any failures or discrepancies for review.