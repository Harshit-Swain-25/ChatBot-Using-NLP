import random
import nltk
from nltk.chat.util import Chat, reflections

nltk.download('punkt', quiet=True)

pairs = [
    [r"hi|hello|hey", ["Hello there!", "Hi! How can I help you?", "Hey! What's up?"]],
    [r"what is your name?", ["I am PyBot — your friendly AI assistant."]],
    [r"how are you?", ["I am doing great! Thanks for asking.", "Feeling awesome, ready to chat!"]],
    [r"what can you do?", ["I can chat with you, and make your day better!"]],
    [r"bye|goodbye", ["Goodbye! Have a nice day!", "See you later!"]],
    [r"(.*)", ["I am not sure I understand, could you rephrase that?"]],

]

chatbot = Chat(pairs, reflections)
print("PyBot: Hello! Type 'bye' to exit")
chatbot.converse()