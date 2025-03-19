import sqlite3
import joblib
import requests

#Load our model
clf = joblib.load("models/penguin_classifier.pkl")
label_encoder = joblib.load("models/label_encoder.pkl")

#API endpoint where we fetch data
url = "http://130.225.39.127:8000/new_penguin/"
response = requests.get(url)
data = response.json()

#I expect the following features
features = [[
    data["bill_length_mm"],
    data["bill_depth_mm"],
    data["flipper_length_mm"],
    data["body_mass_g"]
]]

#I use the model to predict species
species_encoded = clf.predict(features)[0]
species = label_encoder.inverse_transform([species_encoded])[0]

#I connect to our database for the predicted penguins and store the data
conn = sqlite3.connect("data/PenguinAlert.sqlite")
cursor = conn.cursor()
cursor.execute('''
    INSERT INTO PenguinPropertiesPredicted (bill_length_mm, bill_depth_mm, flipper_length_mm, body_mass_g, species)
    VALUES (?, ?, ?, ?, ?)
''', (data["bill_length_mm"], data["bill_depth_mm"], data["flipper_length_mm"], data["body_mass_g"], species))
conn.commit()
conn.close()

print(f"Predicted species: {species}")
