# The Office Chat Bot
A chatterbot.py instance that I trained to speak with phrases from the TV show 'The Office'

## Training
First, make sure the JSON data sets are built and that chatterbot is installed

```bash
pip install chatterbot
php data/processor.php
```

Next, you can run train.py to train the bot, and store the data in a SQLlite database in /app/database

```bash
python app/train.py
```

Now, you should be able to communicate with it
```bash
python app/index.py "Hello Dwight"
Response: Did you do her?
```