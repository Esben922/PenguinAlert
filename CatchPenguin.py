import sqlite3
import joblib
import requests

# Load trained model and label encoder
clf = joblib.load("penguin_classifier.pkl")
label_encoder = joblib.load("label_encoder.pkl")

# Fetch data (Replace this URL with the real API endpoint)
url = "http://130.225.39.127:8000/new_penguin/"
response = requests.get(url)
data = response.json()

# Extract features
features = [[
    data["bill_length_mm"],
    data["bill_depth_mm"],
    data["flipper_length_mm"],
    data["body_mass_g"]
]]

# Predict species
species_encoded = clf.predict(features)[0]
species = label_encoder.inverse_transform([species_encoded])[0]

# Store in SQLite database
conn = sqlite3.connect("PenguinAlert.sqlite")
cursor = conn.cursor()
cursor.execute('''
    INSERT INTO PenguinPropertiesPredicted (bill_length_mm, bill_depth_mm, flipper_length_mm, body_mass_g, species)
    VALUES (?, ?, ?, ?, ?)
''', (data["bill_length_mm"], data["bill_depth_mm"], data["flipper_length_mm"], data["body_mass_g"], species))
conn.commit()
conn.close()

# Print result
print(f"Predicted species: {species}")
