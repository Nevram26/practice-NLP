#!/usr/bin/env python3
"""
Sentiment Analysis Examples using TextBlob
This script demonstrates sentiment analysis using the TextBlob library.
"""

from textblob import TextBlob

def analyze_sentiment(text):
    """Analyze sentiment of given text and return polarity and subjectivity."""
    blob = TextBlob(text)
    sentiment = blob.sentiment
    
    return {
        'text': text,
        'polarity': sentiment.polarity,
        'subjectivity': sentiment.subjectivity
    }

def interpret_sentiment(polarity):
    """Interpret polarity score into sentiment category."""
    if polarity > 0.1:
        return "Positive"
    elif polarity < -0.1:
        return "Negative"
    else:
        return "Neutral"

def basic_sentiment_analysis():
    """Demonstrate basic sentiment analysis."""
    print("=" * 60)
    print("BASIC SENTIMENT ANALYSIS")
    print("=" * 60)
    
    texts = [
        "I love this product! It's amazing and works perfectly.",
        "This is the worst experience I've ever had. Terrible service!",
        "The weather is okay today.",
        "I am very happy with the results. Excellent work!",
        "I hate waiting in long queues. It's so frustrating."
    ]
    
    for text in texts:
        result = analyze_sentiment(text)
        sentiment_category = interpret_sentiment(result['polarity'])
        
        print(f"\nText: {result['text']}")
        print(f"Polarity: {result['polarity']:.3f} ({sentiment_category})")
        print(f"Subjectivity: {result['subjectivity']:.3f}")
        print("-" * 60)

def detailed_sentiment_explanation():
    """Explain sentiment scores in detail."""
    print("\n" + "=" * 60)
    print("UNDERSTANDING SENTIMENT SCORES")
    print("=" * 60)
    
    print("\nPolarity:")
    print("  - Range: -1.0 (most negative) to +1.0 (most positive)")
    print("  - 0.0 indicates neutral sentiment")
    
    print("\nSubjectivity:")
    print("  - Range: 0.0 (objective) to 1.0 (subjective)")
    print("  - High subjectivity = more personal opinion")
    print("  - Low subjectivity = more factual")
    print()

def compare_sentiments():
    """Compare sentiments of different texts."""
    print("=" * 60)
    print("COMPARING SENTIMENTS")
    print("=" * 60)
    
    text1 = "The movie was fantastic! I really enjoyed every moment."
    text2 = "The movie was okay. Nothing special."
    text3 = "The movie was boring and disappointing."
    
    texts = [text1, text2, text3]
    results = []
    
    for text in texts:
        result = analyze_sentiment(text)
        results.append(result)
        sentiment_category = interpret_sentiment(result['polarity'])
        print(f"\nText: {result['text']}")
        print(f"Sentiment: {sentiment_category} (Polarity: {result['polarity']:.3f})")
    
    # Find most positive and most negative
    most_positive = max(results, key=lambda x: x['polarity'])
    most_negative = min(results, key=lambda x: x['polarity'])
    
    print("\n" + "-" * 60)
    print(f"Most Positive: {most_positive['text'][:50]}...")
    print(f"Most Negative: {most_negative['text'][:50]}...")
    print()

def analyze_custom_text():
    """Analyze custom text input."""
    print("=" * 60)
    print("ANALYZE YOUR OWN TEXT")
    print("=" * 60)
    
    sample_text = "Natural Language Processing is incredibly powerful and useful for many applications."
    
    print(f"\nSample Text: {sample_text}")
    result = analyze_sentiment(sample_text)
    sentiment_category = interpret_sentiment(result['polarity'])
    
    print(f"\nSentiment Analysis Results:")
    print(f"  Polarity: {result['polarity']:.3f} ({sentiment_category})")
    print(f"  Subjectivity: {result['subjectivity']:.3f}")
    
    if result['subjectivity'] > 0.5:
        print("  Note: This text is quite subjective (opinion-based)")
    else:
        print("  Note: This text is relatively objective (fact-based)")
    print()

def main():
    """Run all sentiment analysis examples."""
    print("\n" + "=" * 60)
    print("TEXTBLOB SENTIMENT ANALYSIS EXAMPLES")
    print("=" * 60 + "\n")
    
    detailed_sentiment_explanation()
    basic_sentiment_analysis()
    compare_sentiments()
    analyze_custom_text()
    
    print("=" * 60)
    print("Sentiment analysis examples completed!")
    print("=" * 60)

if __name__ == "__main__":
    main()
