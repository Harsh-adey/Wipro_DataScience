import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score

# used only 100000 rows to make it easy to handle.
df = pd.read_csv("yelp_academic_dataset_review.csv", nrows=100000)

df = df[['text', 'stars']].dropna()
df['text'] = df['text'].astype(str)

print("Dataset shape:", df.shape)
print(df.head())


X = df['text']
y = df['stars']   # Ratings (1–5)


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


tfidf = TfidfVectorizer(max_features=5000, stop_words='english')
X_train_tfidf = tfidf.fit_transform(X_train)
X_test_tfidf = tfidf.transform(X_test)


# 5. Train Model

model = LogisticRegression(max_iter=200)
model.fit(X_train_tfidf, y_train)


y_pred = model.predict(X_test_tfidf)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))


def predict_rating(review_text):
    review_tfidf = tfidf.transform([review_text])
    prediction = model.predict(review_tfidf)
    return prediction[0]

print("\nExample Prediction:")
print("Review: 'The food was amazing and the service was excellent!'")
print("Predicted Rating:", predict_rating("The food was amazing and the service was excellent!"))
