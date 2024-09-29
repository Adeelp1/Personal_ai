# import nltk
import spacy

# from nltk.chat.util import Chat, reflections
from transformers import pipeline

from plugins import weather, joke, song

class chatbot:
    def __init__(self):
        self.generator = pipeline('text-generation', model="microsoft/DialoGPT-medium")
        # Load the spaCy language model
        self.nlp = spacy.load('en_core_web_sm')

    def response_generator(self, user_input):

        # Generate a response using the model
        generated_responses = self.generator(
            user_input,
            max_length=100,
            num_return_sequences=1,
            truncation = True, # Explicitly enable truncation
            pad_token_id=50256  # Explicitly set pad_token_id to eos_token_id
            )

        # Access the first generated response
        return generated_responses[0]['generated_text']

    def detect_intent(self, user_input):

        doc = self.nlp(user_input.lower())
        
        # Basic keyword-based intent detection
        if any(token.lemma_ in ['weather', 'temperature'] for token in doc):
            city = input("which city: ")
            return weather.get_weather(city)
        elif 'joke' in user_input:
            return joke.get_joke()
        elif any(token.lemma_ in ['bye', 'goodbye'] for token in doc):
            return "goodbye"
        elif 'song' in user_input:
            query = input("Enter song name: ")
            return song.search_song(query)
        else:
            return self.response_generator(user_input)

    def get_input(self, user_input):
        return self.detect_intent(user_input)


if __name__ == "__main__":
    bot = chatbot()
    # Test the intent detection
    while True:
        user_input = input("You: ")
        intent = bot.get_input(user_input)
        print(f"Sonia: {intent}")

        if intent == "goodbye":
            break