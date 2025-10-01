def count_words(text):
    return len(text.split())

def count_characters(text):
    chars = {}
    for char in text:
        if char.lower() in chars:
            chars[char.lower()] += 1
        else:
            chars[char.lower()] = 1
    return chars

def sort_on(items):
    return items["num"]

def list_characters(dictionary):
    new_list = []
    for key, value in dictionary.items():
        new_list.append({"char": key, "num": value})
    new_list.sort(reverse=True, key=sort_on)
    return new_list