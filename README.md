# English Premier League Player Wage Estimator: Project Overview
<img src="https://i.ibb.co/TBbGg7Q/English-Premier-League-Player-Wage-Predictor-Webpage.png" alt="English-Premier-League-Player-Wage-Predictor-Webpage" border="0">  

* Created a tool that estimates EPL player wages(MAE~7300).
* Scraped all the 2020/21 player attributes from sofifa.com.
* Engineered features so as to quantify the contribution of each feature to weekly wages.
* Optimized Linear,Lasso,RandomForest and XGBoost regressors using GridsearchCV and RandomizedsearchCV.
* Built a client facing API using flask and hosted it on Heroku platform.

### **Code and Resources used**
***
**Python Version**: 3.8  
**Packages**: Pandas,Numpy,Sklearn,Matplotlib,Seaborn,Json,Flask,Pickle  

![Python](https://img.shields.io/badge/python-3670A0?style=flat&logo=python&logoColor=ffdd54) ![Flask](https://img.shields.io/badge/flask-%23000.svg?style=flat&logo=flask&logoColor=white) ![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=flat&logo=pandas&logoColor=white) ![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=flat&logo=numpy&logoColor=white) ![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=flat&logo=jupyter&logoColor=white)  

**For Web Framework Requirements**: pip install -r requirements.txt  
**Scraper**:  ([Octoparse 8 Software](https://www.octoparse.com/))  

### **Web Scraping**
***
Used Octoparse webscraping app (above) to scrape 644 EPL player characteristics from sofifa.com.With each player I got  the following features:
* Team
* Team-contract
* Height
* Weight
* Joined
* Value
* Wage
* Skill
* International_rating
* Hits
* Name
* Age
* Rating
* Ball-control
* Agility
* Stamina
* Mentality
* Physic
* Position

### **Data Cleaning**
***
After scraping the data I needed to clean it up to make it usable for the models. So I made the following changes:  
* Made a loan column specifying whether a player is on loan loan or not.
* Created 2 new columns determining the number of years spent by the player at the club and number of years left before contract expiration.
* Converted the data from string to float,integer datatypes
* converted height and weight from imperial to metric conversion system.
* Removed features that did not facilitate wage prediction.
* Feature transformations to fit the model(linear) assumptions

### **EDA**
***
Looked at the distributions of the data and also visualized the relationships between the input features and the target (wages) and also between themselves(correlation).

### **Model Building**
***
First, I transformed the categorical variables into dummy variables. I also split the data into train and tests sets with a test size of 20%.

I tried four different models and evaluated them using R-squared,Root Mean Squared Error and Mean Absolute Error.

I tried four different models:

* Multiple Linear Regression – Baseline for the model
* Lasso Regression – Because of the sparse data from the many categorical variables, I thought a normalized regression like lasso would be effective.
* Random Forest – Again, with the sparsity associated with the data, I thought that this would be a good fit.
* XGBoost - I also chose this model because it generally does well given any sort of data.

### **Model Perfomance**
***
The XGBoost model far outperformed the other approaches on the test and validation sets.

* XGBoost : r2 is 0.937  
RMSE is 11 294.84  
Absolute mean error is 7 367.08
* Random Forest : r2 is 0.905  
RMSE is 13 862.1  
Absolute mean error is 9 244.28
* Lasso Regression: r2 is 0.904  
RMSE is 16 959.30  
Absolute mean error is 9 544.29  
* Linear Regression: r2 is 0.904  
RMSE is 19 110.26  
Absolute mean error is 10 112.30

### **Productionization**
***
In this step, I built a flask API endpoint that is hosted on Heroku. The API endpoint takes in a request with a list of values grouped as contractual,physical and perfomance player attributes and returns an estimated weekly wage.  
**Live Application:** [EPL-wage-estimator](https://epl-wage-estimator.herokuapp.com)

