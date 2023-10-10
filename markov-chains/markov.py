"""Generate Markov text from text files."""

from random import choice

def read_multi_files(file_path):
    text_string = ''
    for file in file_path:
        hold_text = open_and_read_file(file)
        text_string = text_string + hold_text
        # print(text_string)
    return text_string

def open_and_read_file(file_name):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    
    # your code goes here

    # open (file_path)
    # remove line breaks
    # save string in variable (text_string)



    # should be able to intake full file without iterating through lines

    with open(file_name) as the_file:
        text_string = the_file.read()

        # print(text)
        # print(type(text))
    
    return text_string

'Contents of your file as one long string'


def make_chains(text_string,ngram_length):

    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}

    text_string = text_string.replace('\n', ' ')
    text_string = text_string.split(' ') #str > ['txt','txt2','txt3, 'txt4', 'txt5']

    # for idx in text_string:


    # ngram_length=2)
    for idx in range(len(text_string)):
        try: 
            text_for_tuple = text_string[idx:idx+ngram_length]
            new_tuple = tuple(text_for_tuple)

            #dict_name['pssible_key'] = dict_name.get['pssible_key', default_vaule_if_new] + value_modicfication
            # chains  ['new_tuple']   = chains    .get('new_tuple',  text_string[idx+2])  + text_string[idx+2]
            
            chains[new_tuple] = chains.get(new_tuple, []) + [text_string[idx+ngram_length]]
            # try:
            #     chains[new_tuple] += [text_string[idx+2]]
            # except:
            #     chains[new_tuple] = [text_string[idx+2]]
            
        except:
            break

   


    
    # your code goes here
    # print(chains)
    return chains


def make_text(chains):
    """Return text from chains."""

    words = []



    # build words(list) using key/value pairs
        # add key1 to list
    starting_point = list(chains.keys()) #list of keys in chains
    # print(starting_point)
    # print(starting_point)
    first_key = starting_point[0] 
    # print(first_key)
    """pull value from first_key before converting to list"""
    first_word = choice(chains[first_key])
    first_key = list(first_key)
    #start with first key in list, NICE >> start with random key
    # print(first_key)
    # print(142)
    # first_key = ['Word", "word", "word"]
    # print(first_key)
    first_key[0]  = first_key[0].capitalize()
    # print(first_key)


    words.extend(first_key)
    words.append(first_word)
        # pick random value from key1=('Would', 'you')
        
        #     picks value1
        # add value1 to list
    
    # first_word = choice(chains[starting_point])
    # words.append(" " + first_word)

        # from list, list[-2], list[-1] >> key2
    while True:
        next_point = words[-ngram_length:]
        # print(next_point)
        # print(160)
        next_point = tuple(next_point)
        # print(next_point)
        if next_point in chains:
            
            next_word = choice(chains[next_point])
            words.append(next_word)
        else:
            break
        # pick random value from key2
        #     picks value2
        # add value2 to list

    


    

# return value converts list into a string, putting " " between each word in list
    return ' '.join(words) 




input_path = ['lyrics.txt', 'green-eggs.txt', 'shrek.txt']
ngram_length = 2

# Open the file and turn it into one long string
input_text = read_multi_files(input_path)

# Get a Markov chain
chains = make_chains(input_text,ngram_length)

# Produce random text
random_text = make_text(chains)

print(random_text)
