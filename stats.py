def get_num_words(file_path): 
    with open(file_path) as f: 
        content = f.read()
        words = content.split()
        count = len(words)
        return(count)
    
def count_characters(file_path): 
    with open(file_path) as f: 
        content = f.read().lower()
        words = content.split()
        characters = [char for word in words for char in word]
        char_counts = {}
        for char in characters:
            if char in char_counts:
                char_counts[char] += 1
            else:
                char_counts[char] = 1
        return char_counts
    
def sort_on(dict):
    return dict["count"]

def create_sort_list_from_dict(dict): 
    list = []
    for key, value in dict.items():
        dict_item = {"character": key, "count": value}
        list.append(dict_item)
        list.sort(reverse=True, key=sort_on)
    return list