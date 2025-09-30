# practice-NLP
Repository for practicing NLP related activities such as tokenization, sentiment analysis or sentence translation

## Overview
This repository contains Python examples demonstrating common Natural Language Processing (NLP) tasks:
- **Tokenization** using NLTK
- **Sentiment Analysis** using TextBlob
- **Translation** using TextBlob

## Prerequisites
- Python 3.7 or higher
- Internet connection (required for translation examples)

## Installation

### 1. Clone the repository
```bash
git clone https://github.com/Nevram26/practice-NLP.git
cd practice-NLP
```

### 2. Install required packages
```bash
pip install -r requirements.txt
```

### 3. Download NLTK data (for tokenization)
The tokenization script will automatically download required NLTK data on first run.

## Examples

### 1. Tokenization Example (tokenization_example.py)
Demonstrates various tokenization techniques using NLTK:
- Word tokenization
- Sentence tokenization
- Regular expression tokenization
- Word and punctuation tokenization

**Run the example:**
```bash
python tokenization_example.py
```

**Sample Output:**
```
WORD TOKENIZATION EXAMPLE
Original Text: Hello! Welcome to NLP practice. Let's learn tokenization.
Word Tokens: ['Hello', '!', 'Welcome', 'to', 'NLP', 'practice', '.', 'Let', "'s", 'learn', 'tokenization', '.']
Number of tokens: 12
```

### 2. Sentiment Analysis Example (sentiment_analysis_example.py)
Demonstrates sentiment analysis using TextBlob:
- Basic sentiment analysis (polarity and subjectivity)
- Sentiment comparison
- Interpretation of sentiment scores

**Run the example:**
```bash
python sentiment_analysis_example.py
```

**Sample Output:**
```
BASIC SENTIMENT ANALYSIS
Text: I love this product! It's amazing and works perfectly.
Polarity: 0.625 (Positive)
Subjectivity: 0.650
```

**Understanding Sentiment Scores:**
- **Polarity**: Range from -1.0 (most negative) to +1.0 (most positive)
- **Subjectivity**: Range from 0.0 (objective) to 1.0 (subjective)

### 3. Translation Example (translation_example.py)
Demonstrates simple translation using TextBlob:
- English to multiple languages
- Bidirectional translation
- Language detection
- Common phrases translation

**Run the example:**
```bash
python translation_example.py
```

**Note:** Translation examples require an internet connection. The actual translation functions are commented out by default. Uncomment them in the `main()` function to run actual translations.

**Sample Usage:**
```python
from textblob import TextBlob

text = "Hello! Welcome to Natural Language Processing."
blob = TextBlob(text)
spanish = blob.translate(to='es')
print(spanish)  # "¡Hola! Bienvenido al procesamiento del lenguaje natural."
```

## File Structure
```
practice-NLP/
├── README.md                        # This file
├── requirements.txt                 # Python dependencies
├── tokenization_example.py          # NLTK tokenization examples
├── sentiment_analysis_example.py    # TextBlob sentiment analysis examples
└── translation_example.py           # TextBlob translation examples
```

## Dependencies
- **nltk** (3.8.1): Natural Language Toolkit for tokenization
- **textblob** (0.17.1): Library for processing textual data, sentiment analysis, and translation

## Usage Tips

### Tokenization
- Use `word_tokenize()` for basic word-level tokenization
- Use `sent_tokenize()` to split text into sentences
- Use `regexp_tokenize()` for custom pattern-based tokenization

### Sentiment Analysis
- Polarity > 0.1: Positive sentiment
- Polarity < -0.1: Negative sentiment
- Polarity between -0.1 and 0.1: Neutral sentiment
- Higher subjectivity means more opinion-based content

### Translation
- Requires internet connection
- Uses Google Translate API
- Common language codes: en (English), es (Spanish), fr (French), de (German), it (Italian), pt (Portuguese)

## Contributing
Feel free to add more NLP examples or improve existing ones!

## License
This project is for educational purposes.
