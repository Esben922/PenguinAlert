# PenguinAlert

Visit the page to find out info on today's Penguin:
https://esben922.github.io/PenguinAlert/


# Details

The notebook "PenguinAlert" specifies the process of how the detection model has been made.

In the notebook you will find that the Penguins dataset (downloaded via the Seaborn package in this instance), has been put into a database using SQLite, where the data has been processed and utilized to make a predictive model on Penguin Species.

By deciding the most important features with the Embedded method by using Random Forrest Classifier and then also utilizing this to create a very precise model of 100% accuracy. 

For this a train and test split of the database data has been made of 80% train and 20% test data. 

The Random Forrest Classifier model was trained using the hyperparameter of 100 N_estimators. 

The model is then saved and utilized by a script which via github actions fetches the properties of today's penguin and classifies it. The script can be found in "CatchPenguin.py". The github action can be found in ".github/workflows" as "prediction.yaml". Be sure to see "requirements.txt" as well to ensure correct packages are installed.

For the github page that hosts this information design can be found in index.html.
