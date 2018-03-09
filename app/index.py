#
# index.py - Will respond to the first argument
import sys
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.comparisons import levenshtein_distance

messageToBot = sys.argv[1] # Get argument from the system

chatbot = ChatBot(
    'Office',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database='./office.sqlite3',
    statement_comparison_function=levenshtein_distance
)
chatbot.set_trainer(ListTrainer)
print( str( chatbot.get_response(sys.argv[1]) ) ) # Get the response and return it to the terminal
