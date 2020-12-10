opened_file = open("praise_song_for_the_day.txt", "r")
# print(opened_file.read()) 
read_file = opened_file.read().lower()
# print(read_file)

STOP_WORDS = [
    ' a ', ' an ', ' and ', ' are ', ' as ', ' at ', ' be ', ' by ', ' for ', ' from ', ' has ', ' he ',
    ' i ', ' in ', ' is ', ' it ', ' its ', ' of ', ' on ', ' that ', ' the ', ' to ', ' were ',
    ' will ', ' with '
]

punctuation = '''!()-[]{};:'"\, <>./?@#$%^&*_~'''

def remove_stop_words(stop_words_ls, file):
    for word in stop_words_ls:
        if word in file:
            file = file.replace(word, " ")
    return file

def remove_punctuation(punctuation, file):
    for item in punctuation:
        if item in file:
            file = file.replace(item, " ")
    return file

word_text = remove_stop_words(STOP_WORDS, read_file)
# print(word_text)
ready_text = remove_punctuation(punctuation, word_text)
# print(ready_text)


def create_sorted_dictionary(file):
    word_list = ready_text.split()
    # print(word_list)
    word_counter = {}
    for item in word_list:
        if item in word_counter:
            word_counter[item] +=1
        else:
            word_counter[item] = 1
        #if I wanted to use .get method it would look like:
        #for item in word_list:
        #   word_counter[item] = word_counter.get(item, 0) + 1
    # print(word_counter)
    return sorted(word_counter.items(), key = lambda x:x[1], reverse=True)
    
    # print(sorted_dict)
    # print(sorted_dict )
    # print(sorted_dict.keys, sorted_dict.values)

def stringify(list):
    # print(list)
    for item in list:
        print(item[0], item[1], '|', '*'*(item[1]))

def align_items(items):
    for item in items:
        print(len(item[0]))
    #above function prints length of string as int
    #now find the longest string 
    #then add that white space to beggining of each string...
    #...of letters until you reach a max length (set by longest string)
    pass

sorted_dictionary = create_sorted_dictionary(ready_text)
stringify(sorted_dictionary)
# align_items(sorted_dictionary)

    


# if __name__ == "__main__":
#     import argparse
#     from pathlib import Path

#     parser = argparse.ArgumentParser(
#         description='Get the word frequency in a text file.')
#     parser.add_argument('file', help='file to read')
#     args = parser.parse_args()

#     file = Path(args.file)
#     if file.is_file():
#         print_word_freq(file)
#     else:
#         print(f"{file} does not exist!")
#         exit(1)


