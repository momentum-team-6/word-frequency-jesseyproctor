opened_file = open("praise_song_for_the_day.txt", "r")
# print(opened_file.read()) 
read_file = opened_file.read().lower()
# print(read_file)

#variable.count() for counting words

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


data_text = remove_stop_words(STOP_WORDS, read_file)
print(data_text)
final_text = remove_punctuation(punctuation, data_text)
print(final_text)





def print_word_freq(file):
    # """Read in `file` and print out the frequency of words in that file."""
    pass

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


