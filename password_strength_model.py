import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
import pickle

# Load dataset
data = pd.read_csv('password_strength.csv')
data = data.dropna()

X = data['password']
y = data['strength']

# Convert text to character-level features
vectorizer = CountVectorizer(analyzer='char')
X_vect = vectorizer.fit_transform(X)

# Split & train
X_train, X_test, y_train, y_test = train_test_split(X_vect, y, test_size=0.2, random_state=42)
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Evaluate
accuracy = model.score(X_test, y_test)
print(f"Model Accuracy: {accuracy*100:.2f}%")

# Save model and vectorizer
with open('strength_model.pkl', 'wb') as m:
    pickle.dump(model, m)
with open('vectorizer.pkl', 'wb') as v:
    pickle.dump(vectorizer, v)
