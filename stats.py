def get_book_text(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def count_character_frequency(text):
    char_count = {}
    for char in text.lower():
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def sort_character_frequency(char_count):
    # Filter for alphabetic characters only and create list of dictionaries
    alphabetic_chars = [{'character': char, 'count': count} 
                       for char, count in char_count.items() 
                       if char.isalpha()]
    
    # Sort by count in descending order
    sorted_chars = sorted(alphabetic_chars, key=lambda x: x['count'], reverse=True)
    
    return sorted_chars
    
