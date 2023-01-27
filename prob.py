
import random

def generate_sentence(start):
    # Read the text file and split it into a list of sentences
    with open("scraped_data.txt", "r") as f:
        text = f.read()
    sentences = text.split(".")
    
    # Create a dictionary to store the probability of each word
    word_prob = {}
    
    # Iterate over each sentence and update the word probabilities
    for sentence in sentences:
        words = sentence.split(" ")
        for i in range(len(words) - 1):
            if words[i] not in word_prob:
                word_prob[words[i]] = {}
            if words[i+1] not in word_prob[words[i]]:
                word_prob[words[i]][words[i+1]] = 0
            word_prob[words[i]][words[i+1]] += 1
    
    # Normalize the probabilities
    for word in word_prob:
        total = sum(word_prob[word].values())
        for next_word in word_prob[word]:
            word_prob[word][next_word] /= total
    
    # Check the starting sentence for the best fit
    words = start.split(" ")
    for i in range(len(words) - 1):
        if words[i] not in word_prob:
            return "Cannot generate sentence. Starting sentence does not exist in the text file."
        if words[i+1] not in word_prob[words[i]]:
            return "Cannot generate sentence. Starting sentence does not exist in the text file."
    
    # Generate a new sentence starting with the given sentence
    sentence = start
    word = words[-1]
    while True:
        if word not in word_prob:
            break
        next_word = random.choices(list(word_prob[word].keys()), list(word_prob[word].values()))[0]
        sentence += " " + next_word
        word = next_word
    return sentence

# Test the function with a starting sentence
print(generate_sentence("I am"))








# WORKS BY START WORD

# import random

# def generate_sentence(start):
#     # Read the text file and split it into a list of sentences
#     with open("scraped_data.txt", "r") as f:
#         text = f.read()
#     sentences = text.split(".")
    
#     # Create a dictionary to store the probability of each word
#     word_prob = {}
    
#     # Iterate over each sentence and update the word probabilities
#     for sentence in sentences:
#         words = sentence.split(" ")
#         for i in range(len(words) - 1):
#             if words[i] not in word_prob:
#                 word_prob[words[i]] = {}
#             if words[i+1] not in word_prob[words[i]]:
#                 word_prob[words[i]][words[i+1]] = 0
#             word_prob[words[i]][words[i+1]] += 1
    
#     # Normalize the probabilities
#     for word in word_prob:
#         total = sum(word_prob[word].values())
#         for next_word in word_prob[word]:
#             word_prob[word][next_word] /= total
    
#     # Generate a new sentence starting with the given word
#     sentence = start
#     word = start
#     while True:
#         if word not in word_prob:
#             break
#         next_word = random.choices(list(word_prob[word].keys()), list(word_prob[word].values()))[0]
#         sentence += " " + next_word
#         word = next_word
#     return sentence

# # Test the function with a starting word
# print(generate_sentence("What"))
