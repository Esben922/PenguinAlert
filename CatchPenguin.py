import json
import joblib
import requests
import datetime

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

#Save the prediction as JSON so we can gather data over time
prediction_result = {
    "timestamp": datetime.datetime.utcnow().isoformat(),
    "bill_length_mm": data["bill_length_mm"],
    "bill_depth_mm": data["bill_depth_mm"],
    "flipper_length_mm": data["flipper_length_mm"],
    "body_mass_g": data["body_mass_g"],
    "predicted_species": species
}

with open("data/prediction.json", "w") as f:
    json.dump(prediction_result, f, indent=4)

print(f"Prediction saved: {prediction_result}")
