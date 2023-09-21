"""Functions to parse a file containing villager data."""

# def tokenize_data():
#     file_name = "villagers.csv"
#         # f string
#     the_file = open(file_name)
#     for line in the_file:
#         line = line.rstrip()
#         items = line.split('|')

#         name = items[0]
#         species = items[1]
#         personality = items[2]
#         hobby = items[3]
#         motto = items[4]
#     return items
#Todo: decide what data you want returned from this, how it should be structured etc
# name|species|personality|hobby|motto

def all_species(filename):
    """Return a set of unique species in the given file.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - set[str]: a set of strings
    """
    # all_species("villagers.csv") --> filename = "villagers.csv" # functionions lecture (arguments and parameters)
        # f string
    
    find_animals = set()


    the_file = open(filename)

    for line in the_file:
        line = line.rstrip()
        items = line.split('|') #list of lists

        species = items[1] #species is at index 1 for each list
        find_animals.add(species)
 

    the_file.close()
    

    # TODO: replace this with your code
    return find_animals


def get_villagers_by_species(filename, search_string="All"):
    """Return a list of villagers' names by species.

    Arguments:
        - filename (str): the path to a data file
        - search_string (str): optional, the name of a species
    

    Return:
        - list[str]: a list of names
    """
    #tokenize data
    # token list> dictionary. list[1] (species) >key; list[0]>items (villager names)
    villagers = {}

    the_file = open(filename)
    

    for line in the_file:
        line = line.rstrip()
        items = line.split('|') # name|species|personality|hobby|motto

    # dictionary_name["new/old key name"] = value
    name = items[0]
    species = items[1]
    # try:
    villagers[species] += [name]
    # except:
        # villagers[species] = [name] 

    the_file.close()

    # TODO: replace this with your code
# for species in items:
    # if species == input("Enter animal here: ")
    # villagers.append(items[0])


    return print(villagers) #sorted(villagers)


def all_names_by_hobby(filename):
    """Return a list of lists containing villagers' names, grouped by hobby.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[list[str]]: a list of lists containing names
    """

    # TODO: replace this with your code

    return []


def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (name, species, personality, hobby,
    saying).

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[tuple[str]]: a list of tuples containing strings
    """

    the_file = open(filename)

    for line in the_file:
        line = line.rstrip()
        items = line.split('|') #list of lists


 

    the_file.close()


    all_data = items

    # TODO: replace this with your code

    return all_data


def find_motto(filename, villager_name):
    """Return the villager's motto.

    Return None if you're not able to find a villager with the
    given name.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name

    Return:
        - str: the villager's motto or None
    """

    # TODO: replace this with your code
    villagers = []
    the_file = open(filename)

    while True:
        for line in the_file:
            line = line.rstrip()
            items = line.split('|') # name|species|personality|hobby|motto
            villagers.append(items)
        if villagers[:][0] == villager_name:
            return villagers[:][-1]
        else:
            villager_name = input("Please enter a villager name: ")
        
    #     return None:
     


def find_likeminded_villagers(filename, villager_name):
    """Return a set of villagers with the same personality as the given villager.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name
    
    Return:
        - set[str]: a set of names

    For example:
        >>> find_likeminded_villagers('villagers.csv', 'Wendy')
        {'Bella', ..., 'Carmen'}
    """

    # TODO: replace this with your code
