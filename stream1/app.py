import json
from pathlib import Path
import torch
import torch.nn as nn
import streamlit as st

# Path
BASE = Path(__file__).parent

# Config
with open(BASE / "config.json") as f:
    c = json.load(f)

MAX_LEN = c["max_len"]

# Vocabulary
with open(BASE / "vocab.json") as f:
    vocab = json.load(f)

UNK = vocab["<UNK>"]

# Model
class LSTMClassifier(nn.Module):
    def __init__(self, n, ed=128, hd=128, nl=1, do=0.3):
        super().__init__()
        self.embedding = nn.Embedding(n, ed, padding_idx=0)
        self.lstm = nn.LSTM(ed, hd, nl, batch_first=True)
        self.dropout = nn.Dropout(do)
        self.fc = nn.Linear(hd, 1)

    def forward(self, x):
        x = self.embedding(x)
        _, (h, _) = self.lstm(x)
        return self.fc(self.dropout(h[-1])).squeeze(1)

# Load
model = LSTMClassifier(
    len(vocab),
    c["embedding_dim"],
    c["hidden_dim"],
    c["num_layers"],
    c["dropout"]
)

model.load_state_dict(
    torch.load(BASE / "best_lstm.pt", map_location="cpu")
)

model.eval()

# Encode
def encode(text):
    x = [vocab.get(w, UNK) for w in text.split()]
    return (x[:MAX_LEN] + [0] * MAX_LEN)[:MAX_LEN]

# Predict
def predict(q, options):
    scores = []

    for option in options:
        x = torch.tensor(
            [encode(q + " " + option)],
            dtype=torch.long
        )

        with torch.no_grad():
            scores.append(model(x).item())

    top3 = sorted(
        range(5),
        key=lambda i: scores[i],
        reverse=True
    )[:3]

    return scores, top3

# Interface
st.title("Smart MCQ Solver")

q = st.text_area("Question")

options = [
    st.text_input("Option A"),
    st.text_input("Option B"),
    st.text_input("Option C"),
    st.text_input("Option D"),
    st.text_input("Option E")
]

# Run
if st.button("Solve MCQ"):
    if not q.strip() or any(not x.strip() for x in options):
        st.warning("Enter the question and all five options.")
    else:
        scores, top3 = predict(q, options)

        letters = ["A", "B", "C", "D", "E"]

        st.subheader("Top 3 Predictions")
        st.write(" ".join(letters[i] for i in top3))

        st.subheader("Scores")

        for i, score in enumerate(scores):
            st.write(f"{letters[i]}: {score:.4f}")