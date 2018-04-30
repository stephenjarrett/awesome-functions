import random

def remove_duplicates():
    #De-dup
    print('De-dup')
    print('Duplicates list:')
    duplicates_list = []
    for i in range(0, 25):
        x = random.randint(1, 15)
        duplicates_list.append(x)
    print(duplicates_list)
    print()
    no_duplicates_list = []
    print('Same list with duplicates removed:')
    for i in range(len(duplicates_list)):
        if duplicates_list[i] not in no_duplicates_list:
            no_duplicates_list.append(duplicates_list[i])
    print(no_duplicates_list)
    print()
    return no_duplicates_list