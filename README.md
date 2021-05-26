# CarPricePredictor

## Table of Contents
* Overview/Problem Statement
* Dataset
* File Structure
* Major Packages/Libraries Used
* Installation/Working Environment
* Building the Web App
* Model Deployment on Heroku Platform
* App Implementation
* Drawbacks and Future Scope
* Credits

### 1. Overview/Problem Statement
* Ever wanted to sell your old car but didn't know the optimal price to sell it for? Now you can use this app to sell your car at a reasonable price.
* This ML model uses regression techniques in order to find the optimal selling price of a used car.
* For this problem Linear Regression and RandomForest were implemented, the latter giving better results.

### 2. Dataset
* The dataset was taken from CarDekho website and is available on Kaggle. All the cars present in the dataset are used cars.
* The dataset contains the following features: **Name of the Car**, **Year of Purchase**,**Selling Price**, **Present Price**, **Kilometers Driven**, **Fuel Type**, **Seller Type**, **Transmission Type**, **Number of Previous Owners**.
* [Dataset Link](https://www.kaggle.com/nehalbirla/vehicle-dataset-from-cardekho)

### 3. File Structure
```
├── static 
│   ├── car.jpg
├── templates
│   ├── index.html
├── Notebook.ipynb
├── Procfile
├── README.md
├── app.py
├── car data.csv
├── random_forest_regression_model.pkl
├── requirements.txt
```

### 4. Major Packages/Libraries Used
* pandas 
* numpy
* sci-kit learn
* matplotlib
* seaborn
* Flask
* gunicorn

### 5. Installation/Working Environment
Follow the instructions if you want to run the app from your local computer.
* The app is written using **Python 3.8.5**. You can download it from [here](https://www.python.org/downloads/).You can also download **Anaconda** which is a distribution of python from [here](https://www.anaconda.com/products/individual). I would recommend downloading anaconda since it is very useful as it comes with a lot of python libraries, Jupyter and Spyder IDE.
* Once you are done with the installation, you can clone this repository to your computer and install the required packages and libraries using the following line of code through the command prompt where your local environment is setup.
```
pip install -r requirements.txt
```

### 6. Building the Web App
* The web was developed using flask micro web framework which is written in python suitable for small scale projects such as this one. For more information you can check the offical flask website by clicking [here](https://flask.palletsprojects.com/en/2.0.x/)
* Basic HTML was needed for designing the webpage and to make sure it was responsive to user inputs. 

### 7. Model Deployment on Heroku Platform
* You will have to create a account in order to deploy the model. Login to your account and go to the deploy section.
* Connect to your github repository and deploy the model manually or through Heroku CLI.

![3](https://user-images.githubusercontent.com/83957848/119222443-06092480-bb12-11eb-8102-086761ded15b.JPG)

### 8. App Implementation
* Link: [CarPricePrediction](https://carpricepredictor99.herokuapp.com/)
* The app asks for user to enter their used car details such as current showroom price, kilometers driven by the car, number of owners, age of car, type of fuel used, whether the seller is a dealer or individual, whether the car has automatic or manual transmission. Based on these inputs, selling price of car is predicted.

![1](https://user-images.githubusercontent.com/83957848/119630765-e123f280-be2c-11eb-8b9b-50825130efd6.JPG)
![2](https://user-images.githubusercontent.com/83957848/119630793-e97c2d80-be2c-11eb-865f-98257f972f4a.JPG)

### 9. Drawbacks and Future Scope
* The model doesn't take into consideration the used cars that are no longer in production since present showroom price is needed in order to predict the selling price.
* The model doesn't take into consideration mileage and engine capacity of the car which might have some affect on selling price of the car.
* The app's front end has room for improvement using CSS or other styling techniques. I will be updating the application once I have learnt CSS.
* More algorithms can be used for more accurate results.

### 10. Credits
I would like to thank [Krish Naik](https://github.com/krishnaik06) for hosting this problem statement on his youtube channel, whose work was taken as inspiration for successful completion of this project.  




