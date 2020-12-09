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


def print_word_freq(file):
    word_list = ready_text.split()
    # print(word_list)
    word_counter = {

}
    for item in word_list:
        if item in word_counter:
            word_counter[item] +=1
        else:
            word_counter[item] = 1
        #if I wanted to use .get method it would look like:
        #for item in word_list:
        #   word_counter[item] = word_counter.get(item, 0) + 1
    print(word_counter)


print_word_freq(ready_text)


# .count method counts whatever argument you pass through () so pass each key in dict 
# take list of words, take a word, ask if its a key in dict. 
# if yes add one += 1
# if no create key in dict and set value to 1




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


