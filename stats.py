def count_words(book_text):
    
    words = book_text.split()
    return len(words)

def count_characters(book_text):
    
    book_text = book_text.lower()  
    char_counts = {}

    
    for char in book_text:
        if char.isalpha():  
            char_counts[char] = char_counts.get(char, 0) + 1

    
    sorted_counts = sorted(char_counts.items(), key=lambda x: x[1], reverse=True)

    return sorted_counts 
