# PROFESSIONAL FAKE NEWS DETECTOR
import pandas as pd

class ProfessionalFakeNewsDetector:
    def __init__(self):
        self.fake_indicators = {
            'ABSURD_CLAIMS': ['free for everyone', 'miracle cure', 'world first', 'secret revealed', 'they dont want you to know'],
            'SENSATIONAL_WORDS': ['shocking', 'breaking', 'urgent', 'emergency', 'exposed', 'leaked'],
            'VAGUE_SOURCES': ['experts say', 'studies show', 'sources claim', 'rumors suggest'],
            'FAKE_PATTERNS': ['airports closed', 'atms closed', 'pilot captured', 'holiday declared'],
            'URGENCY_TRIGGERS': ['act now', 'limited time', 'immediately', 'last chance']
        }
        
        self.real_indicators = ['investigation', 'official statement', 'confirmed', 'verified', 'government announced']

    def analyze_news(self, title, text):
        print(f"\n🔍 ANALYZING: {title}")
        print("=" * 60)
        
        content = title + " " + text
        content_lower = content.lower()
        
        red_flags = []
        warnings = []
        credibility_points = 0
        
        # FAKE INDICATORS CHECK
        for claim in self.fake_indicators['ABSURD_CLAIMS']:
            if claim in content_lower:
                red_flags.append(f"Absurd claim: '{claim}'")
        
        for word in self.fake_indicators['SENSATIONAL_WORDS']:
            if word in content_lower:
                warnings.append(f"Sensational language: '{word}'")
        
        for source in self.fake_indicators['VAGUE_SOURCES']:
            if source in content_lower:
                red_flags.append(f"Vague source: '{source}'")
        
        # REAL INDICATORS CHECK
        for indicator in self.real_indicators:
            if indicator in content_lower:
                credibility_points += 1
        
        # DISPLAY RESULTS
        if red_flags:
            print("❌ RED FLAGS:")
            for flag in red_flags:
                print(f"   • {flag}")
        
        if warnings:
            print("⚠️  WARNINGS:")
            for warning in warnings:
                print(f"   • {warning}")
        
        if credibility_points > 0:
            print(f"✅ CREDIBILITY INDICATORS: {credibility_points}")
        
        # CALCULATE SCORE
        fake_score = len(red_flags) * 3 + len(warnings) * 1
        real_score = credibility_points * 2
        
        total_score = fake_score - real_score
        fake_probability = min(max(total_score * 10, 0), 100)
        
        print(f"\n📊 ANALYSIS SUMMARY:")
        print(f"   Red Flags: {len(red_flags)}")
        print(f"   Warnings: {len(warnings)}")
        print(f"   Fake Probability: {fake_probability}%")
        
        # FINAL VERDICT
        if fake_probability >= 70:
            print("🚨 VERDICT: HIGH RISK - LIKELY FAKE NEWS")
        elif fake_probability >= 40:
            print("⚠️  VERDICT: MEDIUM RISK - SUSPICIOUS CONTENT")
        else:
            print("✅ VERDICT: LOW RISK - LIKELY REAL NEWS")
        
        return fake_probability

# MAIN PROGRAM
if __name__ == "__main__":
    print("🤖 PROFESSIONAL FAKE NEWS DETECTOR")
    print("=" * 60)
    
    detector = ProfessionalFakeNewsDetector()
    
    # Test cases
    test_news = [
        ("Free iPhone for All Indians", "Government announces free iPhone for every citizen starting tomorrow. Historic move says senior official."),
        ("Car blast near Red Fort, Delhi", "A car explosion reported near Red Fort in Delhi. Security forces have cordoned off the area and investigation is underway.")
    ]
    
    for title, text in test_news:
        detector.analyze_news(title, text)
        print("─" * 60)