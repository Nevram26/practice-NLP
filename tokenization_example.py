#!/usr/bin/env python3
"""
Tokenization Examples using NLTK
This script demonstrates various tokenization techniques using the Natural Language Toolkit (NLTK).
"""

import nltk
from nltk.tokenize import word_tokenize, sent_tokenize, regexp_tokenize, wordpunct_tokenize

# Download required NLTK data (run this once)
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

def word_tokenization_example():
    """Demonstrate word tokenization."""
    print("=" * 60)
    print("WORD TOKENIZATION EXAMPLE")
    print("=" * 60)
    
    text = "Hello! Welcome to NLP practice. Let's learn tokenization."
    tokens = word_tokenize(text)
    
    print(f"Original Text: {text}")
    print(f"\nWord Tokens: {tokens}")
    print(f"Number of tokens: {len(tokens)}")
    print()

def sentence_tokenization_example():
    """Demonstrate sentence tokenization."""
    print("=" * 60)
    print("SENTENCE TOKENIZATION EXAMPLE")
    print("=" * 60)
    
    text = "Natural Language Processing is fascinating. It helps computers understand human language. We can do many things with NLP!"
    sentences = sent_tokenize(text)
    
    print(f"Original Text: {text}")
    print(f"\nSentence Tokens:")
    for i, sentence in enumerate(sentences, 1):
        print(f"  {i}. {sentence}")
    print(f"\nNumber of sentences: {len(sentences)}")
    print()

def regex_tokenization_example():
    """Demonstrate regular expression tokenization."""
    print("=" * 60)
    print("REGEX TOKENIZATION EXAMPLE")
    print("=" * 60)
    
    text = "Email me at user@example.com or call 123-456-7890"
    
    # Extract words only (alphabetic)
    word_pattern = r'\w+'
    word_tokens = regexp_tokenize(text, word_pattern)
    
    # Extract email and phone patterns
    email_pattern = r'\S+@\S+'
    email_tokens = regexp_tokenize(text, email_pattern)
    
    print(f"Original Text: {text}")
    print(f"\nWord Tokens (using regex): {word_tokens}")
    print(f"Email Tokens: {email_tokens}")
    print()

def wordpunct_tokenization_example():
    """Demonstrate word and punctuation tokenization."""
    print("=" * 60)
    print("WORD AND PUNCTUATION TOKENIZATION EXAMPLE")
    print("=" * 60)
    
    text = "Don't worry! We'll learn NLP step-by-step."
    tokens = wordpunct_tokenize(text)
    
    print(f"Original Text: {text}")
    print(f"\nWordPunct Tokens: {tokens}")
    print(f"Number of tokens: {len(tokens)}")
    print()

def main():
    """Run all tokenization examples."""
    print("\n" + "=" * 60)
    print("NLTK TOKENIZATION EXAMPLES")
    print("=" * 60 + "\n")
    
    word_tokenization_example()
    sentence_tokenization_example()
    regex_tokenization_example()
    wordpunct_tokenization_example()
    
    print("=" * 60)
    print("Tokenization examples completed!")
    print("=" * 60)

if __name__ == "__main__":
    main()
