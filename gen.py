import random

# Open the dataset file
with open("scraped_sentences.txt", "r") as file:
    # Read the entire file into a single string
    text = file.read()

# Tokenize the text into a list of sentences
sentences = text.split("\n")

# Create a dictionary to store the Markov chain
markov_chain = {}

# Determine the order of the Markov chain
order = 1

# Build the Markov chain
for sentence in sentences:
    # Tokenize the sentence into a list of words
    words = sentence.split()
    for i in range(len(words) - order):
        # Get the current state (a tuple of the previous n-1 words)
        state = tuple(words[i:i+order])
        # Get the next word
        next_word = words[i+order]
        # If the state doesn't already exist in the dictionary, add it
        if state not in markov_chain:
            markov_chain[state] = []
        # Add the next word to the list of possible words following the state
        markov_chain[state].append(next_word)

# Get user input
user_input = input("User: ")

# Tokenize the user input
user_input_words = user_input.split()

# Get the last n-1 words of the user input
current_state = tuple(user_input_words[-order:])

# Generate a response
response = list(current_state)
for i in range(10):
    if current_state in markov_chain:
        next_word = random.choice(markov_chain[current_state])
        response.append(next_word)
        current_state = tuple(response[-order:])
    else:
        break

print("Bot: " + " ".join(response))
