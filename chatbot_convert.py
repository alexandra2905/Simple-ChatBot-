
from chatterbot import ChatBot


#libraria pt rularea unui chatbot

# se creaza o nouă instanta pt chatbot
bot = ChatBot(
    'Terminal',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.TimeLogicAdapter',
        'chatterbot.logic.BestMatch'
    ],
    database_uri='sqlite:///database.sqlite3'
)

print('Type something to begin some exercices...')

#următoarea buclă se va executa de fiecare dată când utilizatorul intră
while True:
    try:
        user_input = input()

        bot_response = bot.get_response(user_input)

        print(bot_response)


    # Apăsați ctrl-c sau ctrl-d pe tastatură pentru a ieși
    except (KeyboardInterrupt, EOFError, SystemExit):
        break