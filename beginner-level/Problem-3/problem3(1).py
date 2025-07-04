def find_duplicates_with_dict(tags):
    count_dict = {}
    duplicates = []

    for tag in tags:
        if tag in count_dict:
            count_dict[tag] += 1
        else:
            count_dict[tag] = 1

    for tag, count in count_dict.items():
        if count > 1:
            duplicates.append(tag)

    return duplicates

tags_list = ["ai", "ml", "python", "ml", "dl", "ai"]
print(find_duplicates_with_dict(tags_list))  
