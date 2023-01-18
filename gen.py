import random

# Dummy data
raw_data = ["This is a sample text.",
            "Another sample text for preprocessing.",
            "Here is some more text for you.",
            "And one more text for good measure."]

# Preprocessing
processed_data = [text.lower().split() for text in raw_data]

class MarkovChain:

    def __init__(self, data):
        self.data = data
        self.words = []
        self.word_freq = {}
        for sentence in self.data:
            for word in sentence:
                self.words.append(word)
        for i in range(len(self.words) - 1):
            current_word = self.words[i]
            next_word = self.words[i+1]
            if current_word in self.word_freq:
                self.word_freq[current_word].append(next_word)
            else:
                self.word_freq[current_word] = [next_word]

    def generate_text(self, seed, length):
        current_word = seed
        generated_text = current_word
        for _ in range(length):
            next_word = random.choice(self.word_freq[current_word])
            generated_text += " " + next_word
            current_word = next_word
        return generated_text

# Creating an instance of MarkovChain with the training data
mc = MarkovChain(processed_data)

# Getting user input
user_input = input("Enter some text: ")

# Tokenizing and preprocessing user input
user_input = user_input.lower().split()

# Adding user input to the training data
processed_data.append(user_input)

# Updating the MarkovChain model with the new data
mc.data = processed_data
mc.words = []
mc.word_freq = {}
for sentence in mc.data:
    for word in sentence:
        mc.words.append(word)
for i in range(len(mc.words) - 1):
    current_word = mc.words[i]
    next_word = mc.words[i+1]
    if current_word in mc.word_freq:
        mc.word_freq[current_word].append(next_word)
    else:
        mc.word_freq[current_word] = [next_word]

# Generating new text
generated_text = mc.generate_text(user_input[-1], 10)
print(generated_text)
