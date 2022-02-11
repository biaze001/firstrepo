import math
import random
def skein_counts(stitch_counts):
    '''
    Purpose:
        To take a dictionary in which the key is a string representing the
    color of the thread and the value is an integer representing the number of
    stitches of that color in the project. The function will return a new
    dictionary where the keys are the colors of the thread and the values are
    the number of skeins needed to have enough thread to complete the project.
    Parameter(s):
        stitch_counts:A dictionary in which the key is a string representing the
        color of the thread and the value is an integer representing the number
        of stitches of that color in the project.
    Return Value:
        d: A dictionary where the keys are the colors of the thread and the values
        are the number of skeins needed to have enough thread to complete the
        project.
    '''
    d = {}
    for i in stitch_counts:
        d[i]=int(math.ceil(stitch_counts[i]/1800))
    return d

def follows(words_list):
    '''
    Purpose:
        To take a list of words ans return a dictionary of lists where each key
        in the dictionary will be a word in the words_list, and each value will
        be a list of all of the words that appear immediately after that one,
        each time it appears in words_list.
    Parameter(s):
        words_list: a list of words
    Return Value:
        d: A dictionary where each key in the dictionary will be a word in the
        words_list, and each value will be a list of all of the words that
        appear immediately after that one, each time it appears in words_list.

    '''
    d = {}
    for words in range(len(words_list)):
        if words == len(words_list)-1:
            break
        if words_list[words] in d:
            d[words_list[words]].append(words_list[words+1])
        if words_list[words] not in d:
            d[words_list[words]] = []
            d[words_list[words]].append(words_list[words+1])
    return d

def autofill(follows_dict, current):
    '''
    Purpose:
        To take  two parameters in the following order: a dictionary where each
        key is a word, and each value is a list of words and a  single word
        called current. The function will create a list of words to potentially
        follow current in a randomly generated sentence using the following
        rules:
        1. If the current word appears as a key in the dictionary passed in, the
        function will return the list of words that is the value corresponding
        to that key.
        2. If the word does not appear as a key, return a list of all the keys
        in the dictionary.
    Parameter(s):
        follows_dict: A dictionary where each key is a word, and each value is
        a list of words
        current: single word
    Return Value:
        ls : A list of all the keys in the dictionary.
        or
        follows_dict[current]: A list of words that is the value corresponding
        to that key current.
    '''
    ls=[]
    if current in follows_dict:
        return follows_dict[current]
    else:
        for keys in follows_dict:
            ls.append(keys)
    return ls

def random_sentence(fname, length):
    '''
    Purpose:
        The function will read in the fname file and then use the other
    functions in this assignment to create a random sentence of the given length
    (in terms of number of words), whose data is drawn from the given text file.
    Parameter(s):
        fname: A text file
        length: The number of words in the final sentence
    Return Value:
        sentencestr: A sentence of the given length (in terms of number of words)
    '''
    sentence = []
    sentencestr = ' '
    fp = open(fname)
    fp1 = fp.read()
    fp2 = fp1.split()
    dic = follows(fp2)
    word = random.choice(fp2)
    sentence.append(word)
    for i in range(length-1):
        word = autofill(dic, sentence[i])
        sentence.append(random.choice(word))
    for words in sentence:
        sentencestr += ' '+ words

    return sentencestr

print("hello")
x = 3 + 3
print(x)
