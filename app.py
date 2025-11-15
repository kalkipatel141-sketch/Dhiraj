# app.py
# MAIN FAKE NEWS DETECTION APPLICATION
import pandas as pd
import joblib
import os
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

print("🔍 AI FAKE NEWS DETECTOR")
print("=" * 50)

class FakeNewsDetector:
    def __init__(self):
        self.model = None
        self.vectorizer = None
        self.load_model()
    
    def load_model(self):
        """Load trained AI model"""
        try:
            if os.path.exists('fake_news_model.pkl') and os.path.exists('vectorizer.pkl'):
                print("📂 Loading AI model...")
                self.model = joblib.load('fake_news_model.pkl')
                self.vectorizer = joblib.load('vectorizer.pkl')
                print("✅ AI model loaded successfully!")
            else:
                print("❌ Model not found. Please run 'train_model.py' first.")
                print("💡 Training model now...")
                self.train_new_model()
        except Exception as e:
            print(f"❌ Error loading model: {e}")
    
    def train_new_model(self):
        """Train a new model if not exists"""
        try:
            from train_model import train_fake_news_model
            self.model, self.vectorizer = train_fake_news_model()
        except:
            print("❌ Could not train model. Please check dataset.csv")
    
    def predict_news(self, text):
        """Predict if news is real or fake"""
        if self.model is None or self.vectorizer is None:
            return "Model not available", 0
        
        # Convert text to features
        text_features = self.vectorizer.transform([text])
        
        # Make prediction
        prediction = self.model.predict(text_features)[0]
        probability = self.model.predict_proba(text_features)[0]
        
        # Get confidence score
        confidence = max(probability)
        
        return prediction, confidence
    
    def analyze_text(self, text):
        """Analyze text and provide detailed results"""
        prediction, confidence = self.predict_news(text)
        
        # Manual rule-based checks (for educational purposes)
        fake_indicators = ['breaking', 'shocking', 'conspiracy', 'secret', 'hoax', 
                          'rumor', 'viral', 'exposed', 'miracle', '100%']
        
        trusted_sources = ['bbc', 'reuters', 'associated press', 'official', 
                          'research', 'study', 'report']
        
        detected_indicators = [word for word in fake_indicators if word in text.lower()]
        trusted_mentioned = any(source in text.lower() for source in trusted_sources)
        
        return {
            'prediction': prediction,
            'confidence': confidence,
            'indicators': detected_indicators,
            'trusted_source': trusted_mentioned
        }

def main():
    # Initialize detector
    detector = FakeNewsDetector()
    
    if detector.model is None:
        return
    
    print("\n🎯 AI FAKE NEWS DETECTOR READY!")
    
    while True:
        print("\n" + "=" * 50)
        print("\nChoose an option:")
        print("1. Check news text")
        print("2. Check example news")
        print("3. View model info")
        print("4. Exit")
        
        choice = input("\nEnter your choice (1-4): ").strip()
        
        if choice == '1':
            print("\n📝 Enter the news text you want to check:")
            news_text = input("> ").strip()
            
            if news_text:
                result = detector.analyze_text(news_text)
                
                print("\n" + "🔍 ANALYSIS RESULTS:")
                print("=" * 30)
                print(f"🤖 AI Prediction: {result['prediction'].upper()}")
                print(f"📊 Confidence: {result['confidence']*100:.1f}%")
                
                if result['indicators']:
                    print(f"🚨 Suspicious words: {', '.join(result['indicators'])}")
                else:
                    print("✅ No suspicious words detected")
                
                if result['trusted_source']:
                    print("📰 Trusted source mentioned")
                else:
                    print("⚠️  No trusted source mentioned")
                
                print("\n💡 VERDICT:")
                if result['prediction'] == 'fake':
                    print("❌ This might be FAKE NEWS! Verify from official sources.")
                else:
                    print("✅ This seems LEGITIMATE. Still verify facts.")
            else:
                print("❌ Please enter some text!")
        
        elif choice == '2':
            examples = [
                "Breaking news! Shocking conspiracy about government secrets exposed!",
                "Reuters reports economic growth in developing countries",
                "Miracle cure discovered for all diseases - doctors shocked!",
                "Scientific study confirms climate change effects on agriculture",
                "Viral rumor claims new phone update will damage your device"
            ]
            
            print("\n📖 EXAMPLE NEWS:")
            for i, example in enumerate(examples, 1):
                print(f"{i}. {example}")
            
            try:
                ex_choice = int(input("\nSelect example (1-5): ")) - 1
                if 0 <= ex_choice < len(examples):
                    result = detector.analyze_text(examples[ex_choice])
                    
                    print(f"\n📝 Text: {examples[ex_choice]}")
                    print(f"🤖 AI Prediction: {result['prediction'].upper()}")
                    print(f"📊 Confidence: {result['confidence']*100:.1f}%")
                else:
                    print("❌ Invalid choice!")
            except:
                print("❌ Please enter a valid number!")
        
        elif choice == '3':
            print("\n📊 MODEL INFORMATION:")
            print("Algorithm: Logistic Regression")
            print("Features: TF-IDF Vectorization")
            print("Training: Supervised Machine Learning")
            print("Accuracy: ~85-90% (on sample data)")
            print("\n💡 This is a SIMPLE AI model for educational purposes.")
            print("Real-world systems use more complex deep learning.")
        
        elif choice == '4':
            print("\n🙏 Thank you for using AI Fake News Detector!")
            print("Stay informed, verify facts! 🛡️")
            break
        
        else:
            print("❌ Invalid choice! Please enter 1, 2, 3, or 4")

# Start application
if __name__ == "__main__":
    main()