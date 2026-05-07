import pandas as pd
import pickle
import os
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from preprocess import clean_text

# ===============================
# 1️⃣ Load Dataset
# ===============================
data = pd.read_csv("A:\yoga-ml-module\data\ml_dataset.csv")
data.columns = data.columns.str.strip()
data = data.dropna()

# ===============================
# 2️⃣ Clean Text
# ===============================
data["description"] = data["description"].apply(clean_text)

# ===============================
# 3️⃣ Shuffle Dataset
# ===============================
data = data.sample(frac=1, random_state=42).reset_index(drop=True)

# ===============================
# 4️⃣ Features & Labels
# ===============================
X = data["description"]
y = data["body_part"]

# ===============================
# 5️⃣ Stratified Split
# ===============================
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# ===============================
# 6️⃣ TF-IDF
# ===============================
vectorizer = TfidfVectorizer(ngram_range=(1,2))
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

# ===============================
# 7️⃣ Train Logistic Regression
# ===============================
model = LogisticRegression(max_iter=1000)
model.fit(X_train_tfidf, y_train)

# ===============================
# 8️⃣ Evaluate
# ===============================
y_pred = model.predict(X_test_tfidf)

print("\n===== BODY PART MODEL (Back / Knee / Neck) =====")
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n")
print(classification_report(y_test, y_pred))

# ===============================
# 9️⃣ Save Model
# ===============================
os.makedirs("models", exist_ok=True)

pickle.dump(model, open("A:\yoga-ml-module\models/body_model.pkl", "wb"))
pickle.dump(vectorizer, open("A:\yoga-ml-module\models/body_vectorizer.pkl", "wb"))

print("\nBody model saved successfully!")