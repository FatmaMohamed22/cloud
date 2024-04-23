import re
from collections import Counter
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')

# to read file
def read_file(random_paragraphs):
    with open(random_paragraphs, 'r') as file:
        return file.read()

# to remove stopwords
def remove_stopwords(text, stopwords_set):
    words = re.findall(r'\b\w+\b', text.lower())
    return ' '.join(word for word in words if word not in stopwords_set)

# to count word frequencies
def count_word_frequencies(text):
    words = re.findall(r'\b\w+\b', text.lower())
    return Counter(words)

# Main function
def main():
    # Read the file
    filename = "random_paragraphs.txt"  
    paragraphs = read_file("random_paragraphs.txt")

    # Define stop words
    nltk_stopwords = set(stopwords.words('english'))

    # Remove stop words
    filtered_text = remove_stopwords(paragraphs, nltk_stopwords)

    # Count word frequencies
    word_frequencies = count_word_frequencies(filtered_text)

    # Display word frequency count
    for word, count in word_frequencies.items():
        print(f'{word}: {count}')

if __name__ == "__main__":
    main()