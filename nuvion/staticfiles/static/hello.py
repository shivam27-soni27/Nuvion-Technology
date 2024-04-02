import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

# Sample greetings dataset
greetings = [
    "Hello!",
    "Hi there!",
    "How are you?",
    "Good morning!",
    "Good afternoon!",
    "Good evening!",
    "Hey!",
    "What's up?",
    "Nice to meet you!",
    "Greetings!",
    # Add more greetings as needed
]

# Tokenize characters
chars = sorted(list(set(''.join(greetings))))
char_indices = dict((c, i) for i, c in enumerate(chars))

# Generate input sequences and corresponding target characters
maxlen = max([len(g) for g in greetings]) - 1
sequences = []
next_chars = []
for greeting in greetings:
    for i in range(len(greeting) - 1):
        sequences.append(greeting[:i+1])
        next_chars.append(greeting[i+1])

# Vectorize sequences
x = np.zeros((len(sequences), maxlen, len(chars)), dtype=np.bool)
y = np.zeros((len(sequences), len(chars)), dtype=np.bool)
for i, sequence in enumerate(sequences):
    for t, char in enumerate(sequence):
        x[i, t, char_indices[char]] = 1
    y[i, char_indices[next_chars[i]]] = 1

# Build the model
model = Sequential([
    LSTM(128, input_shape=(maxlen, len(chars))),
    Dense(len(chars), activation='softmax')
])

model.compile(loss='categorical_crossentropy', optimizer='adam')

# Train the model
model.fit(x, y, batch_size=32, epochs=50)
