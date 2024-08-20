# Data Science Midterm Project

## Project/Goals
The goal of this project is to follow a process from start to finish to input raw data into a DataFrame, clean it and prepare it
to be used in a model that will predict selling prices of a house using a number of features.
This is accomplished by implementing supervised learning methods to predict prices.
It also will demonstrate the process of building and selecting the best features to increase the accuracy of the prediction models.

## Process
### (your step 1)
- View a single JSON to become familiar with its structure and possible required steps to extract as much information as possible.
- Create a process that will take each JSON file and join it into one DataFrame.
- Normalize and flatten the nested elements.
- Determine which elements need more in depth flattening like tags. 
- Find null values and determine an approach to properly address them. Some values could be dropped while some could be imputed using mean and median.
- Search through columns and get familiar with their contents. Determine their usefulness in the prediction of sale prices.
- Determine what some columns refer to like Matterport - This is a virtual tour that may attract more viewings.
- Visualize the data and determine if data has a large amount of outliers.
- Observe correlations and remove items that are redundant. 
- Expand the tags column to extract more potentially valueable features.
- Use the frequency or hits of each tag to determine which ones should be kept within the model.
- Target encode cities using the training data, to create a feature.
- Scale the data
- split the train and test data. Save each.
- Prepare models and record their performance values.
- Determine the model with the best metrics.
- Perform hyperparameter tuning with the chosen model.
- After finding the best hyperparameters, run the test data and observe the resulting metrics
- Save the best model determined from tuning.

## Results
The data had quite a number of redundant columns to sort through. 
After cleaning as best as possible, I determined that Xgboost was the best performing model. 
It had a very high R2 accounting for 99.3% of the variance in data. 
It also exhibited the lowest MSE and RMSE values indicating the lowest errors. 
I followed with hyperparameter tuning. 
This increased the performance of R2 to 99.5% 

## Challenges 
- Creating a loop to import the JSON files was a challenge
- Retaining the information that was nested when normalizing and flattening data.
- Finding a method to extract tags that had been nested in the 'tags' column without creating a massive amount of individual rows.
- Sorting through null values and determining what approach to be used, mean, median, or simply adding a 0 instead of None.
- Making decisions on what columns should be kept and which ones should be removed.


## Future Goals
(what would you do if you had more time?)
I'd like to find a better approach to dealing with null values, I tended to do a lot manually.
I created some functions after going through data manually. 
Even though I made functions, I was not able to use the functions_variables.py properly. I'd like to learn how to implement that better.
I'd like to fine tune some of the visualizations a bit better. I felt extremely rushed to get a functional product. 
I would have like to utilized the functions_variables.py better. I couldn't load my functions to notebooks when they were just stored
in the functions python file. I included them in the notebook where I used the functions. 