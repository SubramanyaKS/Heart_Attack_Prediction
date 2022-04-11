# Heart_Attack_Prediction

## Dataset Description
* age: The person's age in years
* sex: The person's sex (1 = male, 0 = female)
* cp: The chest pain experienced (Value 1: typical angina, Value 2: atypical angina, Value 3: non-anginal pain, Value 4: asymptomatic)
* trestbps: The person's resting blood pressure (mm Hg on admission to the hospital)
* chol: The person's cholesterol measurement in mg/dl
* fbs: The person's fasting blood sugar (&gt; 120 mg/dl, 1 = true; 0 = false)
* restecg: Resting electrocardiographic measurement (0 = normal, 1 = having ST-T wave abnormality, 2 = showing probable or definite left ventricular hypertrophy by Estes' criteria)
* thalach: The person's maximum heart rate achieved
* exang: Exercise induced angina (1 = yes; 0 = no)
* ldpeak: ST depression induced by exercise relative to rest ('ST' relates to positions on the ECG plot. See more here)
* slope: the slope of the peak exercise ST segment (Value 1: upsloping, Value 2: flat, Value 3: downsloping)
* ca: The number of major vessels (0-3)
* thal: A blood disorder called thalassemia (3 = normal; 6 = fixed defect; 7 = reversable defect)
* target: Heart disease (0 = no, 1 = yes)

## Technology used
* Python
* Flask
* HTML
* CSS
* Jupyter Notebook
* Deployed in heroku

## Project Structure
This project has four major parts :

* model.py - This contains code fot our Machine Learning model to predict employee salaries absed on trainign data in 'hiring.csv' file.
* app.py - This contains Flask APIs that receives employee details through GUI or API calls, computes the precited value based on our model and returns it.
* template - This folder contains the HTML template (index.html) to allow user to enter employee detail and displays the predicted employee salary.
* static - This folder contains the css folder with style.css file which has the styling required for out index.html file.


## Credits / References:
* Youtube
* Github
* Towardsdatascience

#### Note:
* Data cleaning, visualization and applying the algorithm all theses are in jupyter Notebook.

* Since accuracy from the kernel support vector machine is high so i used this algorithm for model deployment.

* check out the model :
https://heart-attack-prediction-model.herokuapp.com/


If you like this project fork this project and ⭐ this repository.
Thank You have a good day.
