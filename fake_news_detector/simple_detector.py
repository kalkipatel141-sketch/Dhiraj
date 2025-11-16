# SIMPLE FAKE NEWS DETECTOR
print("🤖 WELCOME TO FAKE NEWS DETECTOR")
print("=" * 50)

def check_news(title, text):
    # Fake news ke signs
    fake_signs = [
        'free', 'miracle', 'breakthrough', 'historic move',
        'experts warn', 'senior official', 'world first',
        'cures cancer', 'moon land', '5-day weekend', 'tesla rickshaw'
    ]
    
    # Sab text ko chota letters mein karo
    content = (title + " " + text).lower()
    
    # Check karo kitne fake signs hai
    found_signs = []
    for sign in fake_signs:
        if sign in content:
            found_signs.append(sign)
    
    # Decision lo
    if len(found_signs) >= 2:
        return "🚨 FAKE NEWS!", found_signs
    elif len(found_signs) == 1:
        return "⚠️ SUSPICIOUS!", found_signs
    else:
        return "✅ REAL NEWS!", found_signs

# TEST KARO
test_cases = [
    {
        "title": "India Declares 5-Day Weekend Every Week Starting 2026",
        "text": "NEW DELHI: In a historic move, the Indian government has announced that all offices and schools will observe a 5-day weekend starting January 1, 2026. Employees will now work only Monday and Tuesday. Experts warn of economic collapse."
    },
    {
        "title": "India Successfully Launches Chandrayaan-4 Mission",
        "text": "SRIHARIKOTA: ISRO successfully launched Chandrayaan-4 mission carrying advanced lunar rover and orbital module for detailed moon exploration."
    }
]

print("📊 TESTING NEWS EXAMPLES:")
print("=" * 50)

# Har news check karo
for i, news in enumerate(test_cases, 1):
    print(f"\n📰 News {i}: {news['title']}")
    result, signs = check_news(news['title'], news['text'])
    print(f"Result: {result}")
    if signs:
        print(f"🚩 Signs found: {', '.join(signs)}")
    print("-" * 60)

print("\n🎉 DEMO COMPLETE!")