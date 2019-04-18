from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

import json
import os

# Create a new chatbot
chatbot = ChatBot(
    'Office',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database='./database/database.sqlite3'
)

# Set the traininer to the list trainer
# chatbot.set_trainer(ListTrainer)

trainer = ListTrainer(chatbot)

# Get all the json files in the training data folder and append them to a list
trainingFilesList = []
json_data_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'data/processed/json')
for file in os.listdir( json_data_dir ):
    if file.endswith(".json"):
        trainingFilesList.append(os.path.join(json_data_dir, file))
        
# Loop through the training files list and parse the JSON from each file
for file in trainingFilesList:
	data = json.load(open(file))
	
	# Now that we have the data for each file, train the chat bot on that data with the ListTrainer adapter
	trainer.train(data)
	print("training " + str(file))
