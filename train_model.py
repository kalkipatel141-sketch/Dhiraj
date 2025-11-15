# train_model.py
# AI MODEL TRAINING SCRIPT
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib
import os

print("🚀 TRAINING AI MODEL FOR FAKE NEWS DETECTION...")
print("=" * 50)

def train_fake_news_model():
    # Check if dataset exists
    if not os.path.exists('dataset.csv'):
        print("❌ dataset.csv not found! Please create the dataset first.")
        return None
    
    # Load dataset
    print("📊 Loading dataset...")
    data = pd.read_csv('dataset.csv')
    print(f"Dataset loaded: {len(data)} samples")
    
    # Prepare features and labels
    X = data['text']  # News text
    y = data['label'] # Labels: real/fake
    
    print("\n📈 Dataset Info:")
    print(f"Real news: {sum(y == 'real')}")
    print(f"Fake news: {sum(y == 'fake')}")
    
    # Convert text to numerical features using TF-IDF
    print("\n🔧 Converting text to features...")
    vectorizer = TfidfVectorizer(max_features=1000, stop_words='english')
    X_features = vectorizer.fit_transform(X)
    
    # Split data into training and testing
    X_train, X_test, y_train, y_test = train_test_split(
        X_features, y, test_size=0.2, random_state=42
    )
    
    # Train AI model
    print("🤖 Training AI model...")
    model = LogisticRegression()
    model.fit(X_train, y_train)
    
    # Test model accuracy
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    
    print(f"\n✅ Model Training Complete!")
    print(f"📊 Accuracy: {accuracy * 100:.2f}%")
    
    # Save model and vectorizer
    joblib.dump(model, 'fake_news_model.pkl')
    joblib.dump(vectorizer, 'vectorizer.pkl')
    
    print("💾 Model saved as 'fake_news_model.pkl'")
    print("💾 Vectorizer saved as 'vectorizer.pkl'")
    
    return model, vectorizer

# Train model when script runs
if __name__ == "__main__":
    train_fake_news_model()
    print("\n🎉 Training completed! Now run 'app.py'")