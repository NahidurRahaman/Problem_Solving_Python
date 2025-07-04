def find_duplicates(tags):
    find = set()
    duplicates = set()
    for tag in tags:
        if tag in find:
            duplicates.add(tag)
        else:
            find.add(tag)
    return duplicates

# Example usage
tags_list = ["ai", "ml", "python", "ml", "dl", "ai"]
print(find_duplicates(tags_list))  
