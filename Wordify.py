import random
from collections import Counter

# ---------------- DICTIONARY ----------------
dictionary = [
    "a", "an", "at", "am", "as", "is", "it", "in", "on", "up", "us",
    "ant", "art", "ate", "ear", "eat", "tea", "tar", "rat", "tap",
    "cat", "car", "cap", "cop", "top", "pot", "opt", "dog", "god",
    "man", "pan", "nap", "map", "sun", "run", "fun", "fan", "can",
    "game", "gate", "mate", "rate", "tear", "star", "arts", "rats",
    "care", "race", "acre", "read", "dear", "fear", "gear", "near",
    "note", "tone", "stone", "ones", "nose", "zone", "gone",
     "milk", "silk", "talk", "walk", "bark", "dark", "park",
    "jump", "lamp", "camp", "damp", "tame", "name", "same", 
    "earth", "heart", "hater", "later", "alert", "alter",
    "table", "bleat", "plate", "pleat", "leapt",
    "stone", "notes", "tones", "onset",
    "smart", "start", "tars", "arts", "rats",
    "listen", "silent", "enlist", "inlets",
    "rescue", "secure", "recuse",
    "dealer", "leader", "realed",
    "apple", "banana", "orange", "grape", "mango",
    "water", "river", "ocean", "earth", "world",
    "school", "student", "teacher", "friend",
    "run", "walk", "talk", "play", "work", "read", "write",
    "make", "take", "give", "come", "go"
]
base_word = random.choice(dictionary)
letters = list(base_word.upper())
random.shuffle(letters)

letters_counter = Counter(base_word.upper())

# ---------------- GAME VARIABLES ----------------
score = 0
used_words = []

print("WORD GAME")
print("Make valid English words!")
print("\nLetters:", " ".join(letters))
print("\nType 'quit' to stop.\n")

# ---------------- GAME LOOP ----------------
while True:
    word = input("Enter word: ").lower().strip()

    if word == "quit":
        break

    if word == "":
        continue

    # ---------------- CHECK 1: dictionary ----------------
    if word not in dictionary:
        print("Word doesn't exist in dictionary!\n")
        continue

    # ---------------- CHECK 2: duplicate ----------------
    if word in used_words:
        print("Already used!\n")
        continue

    # ---------------- CHECK 3: letters validity ----------------
    if not Counter(word.upper()) <= letters_counter:
        print("You can only use given letters!\n")
        continue

    # ---------------- ACCEPT WORD ----------------
    used_words.append(word)
    score += len(word)

    print("Correct!")
    print("Score:", score, "\n")

# ---------------- FINAL RESULT ----------------
print("\n======================")
print("GAME OVER")
print("Final Score:", score)
print("Words you made:", used_words)
print("======================")