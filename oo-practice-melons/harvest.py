############
# Part 1   #
############


class MelonType:
    """A species of melon at a melon farm."""

    def __init__(
        self, code, first_harvest, color, is_seedless, is_bestseller, name
    ):
        """Initialize a melon."""
        self.pairings = []
        self.name = name
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller


            # Reporting code: yw

            # First harvest in 2013

            # Color: yellow

            # Pairs well with ice cream

            # Has seeds

            # Bestseller

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        self.pairings.extend(pairing)
        # Fill in the rest



    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    # musk, cas, cren, yw
    # Fill in the rest
    # code, first_harvest, color, is_seedless, is_bestseller, name

    musk = MelonType("musk", 1998, "green", True, True, "Muskmelon")
    musk.add_pairing(["mint"])
    all_melon_types.append(musk)

    cas = MelonType("cas", 2003, "orange", False, False, "Casaba")
    cas.add_pairing(["strawberry", "mint"])
    all_melon_types.append(cas)
    
    cren = MelonType("cren", 1996, "green", False, False, "Crenshaw")
    cren.add_pairing(["prosciutto"])
    all_melon_types.append(cren)

    yw = MelonType("yw", 2013, "yellow", False, True, "Yellow Watermelon")
    yw.add_pairing(["ice cream"])
    all_melon_types.append(yw)
    
    return all_melon_types


def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""
    
    # Muskmelon pairs with
    # - mint

    # Casaba pairs with
    # - mint
    # - strawberries

    # Crenshaw pairs with
    # - prosciutto

    # Yellow Watermelon pairs with
    # - ice cream
    
    # melon_types = [ musk, cas, cren, yw]
    for melon in melon_types:
        pairing_list = melon.pairings
        pairing_list = ", ".join(pairing_list)
        print(f"{melon.name} pairs with {pairing_list}")   
        
    # __str__


    return None

def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    melon_dict = {}

    for melon in melon_types:
        melon_dict[melon.code] = [melon.name, melon.first_harvest, melon.color, melon.is_seedless, melon.is_bestseller, melon.pairings]

    return melon_dict
    # 
    # code, first_harvest, color, is_seedless, is_bestseller, name

    # musk = MelonType("musk", 1998, "green", True, True, "Muskmelon")
        # self.pairings = []
        # self.name = name
        # self.code = code
        # self.first_harvest = first_harvest
        # self.color = color
        # self.is_seedless = is_seedless
        # self.is_bestseller = is_bestseller

    # key = melon.code
    # value = [melon.name, melon.first_harvest, melon.color, melon.is_seedless, melon.is_bestseller, melon.pairings]

    #  keys are reporting codes (as strings) and 
    # whose values are the appropriate melon type instance for that reporting code.
    # Fill in the rest

############
# Part 2   #
############


class Melon:
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods
    def __init__(
        self, code, shape_rating, color_rating, field_source, harvesterered):
        """Initialize a melon."""

        self.sellable = []

        self.code = code
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.field_source = field_source
        self.harvesterered = harvesterered

    def is_sellable(self):
        if (self.shape_rating > 5) and (self.color_rating >5) and (self.field != 3):
            self.sellable = True
        else:
            self.sellable = False

def make_melons(melon_types):
    """Returns a list of Melon objects."""

    # melons_by_id = make_melon_type_lookup(melon_types)
#    self, code, shape_rating, color_rating, field_source, harvesterered, melon_number, melon_sellable):
    melons = []

    melon_1 = Melon(melon_types['yw'], 8, 7, 2, 'Sheila')
    melon_2 = Melon(melon_types['yw'], 3, 4, 2, 'Sheila')
    melon_3 = Melon(melon_types['yw'], 9, 8, 3, 'Sheila')
    melon_4 = Melon(melon_types['cas'], 10, 6, 35, 'Sheila')
    melon_5 = Melon(melon_types['cren'], 8, 9, 35, 'Michael')
    melon_6 = Melon(melon_types['cren'], 8, 2, 35, 'Michael')
    melon_7 = Melon(melon_types['cren'], 2, 3, 4, 'Michael')
    melon_8 = Melon(melon_types['musk'],6, 7, 4, 'Michael')
    melon_9 = Melon(melon_types['yw'], 7, 10, 3, 'Sheila')

    melons.extend([melon_1, melon_2, melon_3, melon_4, melon_5, melon_6, melon_7, melon_8, melon_9])

    return melons
    # self, code, shape_rating,  color_rating, field_source, harvesterered, melon_number
    # cren = MelonType("cren", 1996, "green", False, False, "Crenshaw")
    # cren.add_pairing(["prosciutto"])
    # all_melon_types.append(cren)

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""
    # '(CAN BE SOLD)' or '(NOT SELLABLE)'
    
    # Fill in the rest
    for melon in melons:
        if melon.sellable == False:
            sellable_melon = "MELON IS SELLABLE"
            print(f"Harvested by {melon.harvesterered} from field {melon.field_source} {sellable_melon}")
        else:
            sellable_melon = "MELON CANNOT BE SOLD"
            print(f"Harvested by {melon.harvesterered} from field {melon.field_source} {sellable_melon}")




melon_types = make_melon_types()
print(melon_types)
melon_types = make_melon_type_lookup(melon_types)
print(melon_types)
melons = make_melons(melon_types)
get_sellability_report(melons)