import re
from collections import Counter

stopwords = {
    "the", "is", "in", "at", "a", "an", "and", "or", "on", "of", "to", "with", 
    "for", "by", "this", "that", "it", "as", "are", "was", "were", "be", "been", 
    "but", "not", "from", "have", "has", "had", "you", "we", "they", "he", "she"
}

def most_frequent_word(text):
   
    words = re.findall(r'\b\w+\b', text.lower())
    
    filtered_words = [word for word in words if word not in stopwords]
    
    
    freq = Counter(filtered_words)
    
    if freq:
        word, count = freq.most_common(1)[0]
        return word, count
    else:
        return None, 0


blog_content = """
Machine learning is the science of getting computers to act without being explicitly programmed.
It has given us self-driving cars, practical speech recognition, effective web search, and a vastly improved understanding of the human genome.
"""

word, count = most_frequent_word(blog_content)
print(f"Most frequent word: '{word}' occurred {count} times.")
