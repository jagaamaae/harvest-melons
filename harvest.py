############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, name, first_harvest, 
    color, is_seedless, is_bestseller, 
                 ):
        """Initialize a melon."""

        self.pairings = []

        self.code=code
        self.first_harvest=first_harvest
        self.color=color
        self.is_seedless=is_seedless
        self.is_bestseller=is_bestseller
        self.name=name


    def add_pairing(self, pairing):
        """Add 0a food pairing to the instance's pairings list."""

        self.pairings.append(pairing)
        print(self.pairings)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code=new_code
        print(self.code)


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    musk = MelonType("musk","Muskmelon",1998,"green",True,True)
    musk.add_pairing("mint") 
    all_melon_types.append(musk)
    
    cas = MelonType("cas", "Casaba", 2003, "orange", False, False)
    cas.add_pairing("strawberries")
    cas.add_pairing("mint")
    all_melon_types.append(cas)

    cren = MelonType ("cren", "Crenshaw", 1996, "green", False, False)
    cren.add_pairing("proscuitto")
    all_melon_types.append(cren)

    yw = MelonType ("yw", "Yellow wateremelon", 2013, "yellow", False, True)
    yw.add_pairing("ice cream")
    all_melon_types.append(yw)
    
    return all_melon_types

melon_types = make_melon_types()


def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    for melon in melon_types:       
        for pairing in melon.pairings:
            print (f"{melon.name} pairs with {pairing}")

print_pairing_info(melon_types)


def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""
    melon_dict = {}

    for melon in melon_types:
        # if melon.code not in melon_types:
        melon_dict[melon.code] = melon.name

    return melon_dict

melon_dict=make_melon_type_lookup(melon_types)




############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""

    def __init__(self, melon_type, shape_rating, color_rating, harvested_field, harvester):
        self.melon_type=melon_type
        self.shape_rating=shape_rating
        self.color_rating=color_rating
        self.harvested_field= harvested_field
        self.harvester=harvester
        
        
    
    def is_sellable(self):
        if self.shape_rating>5 and self.color_rating>5 and self.harvested_field != "Field 3":
            return True
    
    sellable = is_sellable(self)



def make_melons(melon_types):
    """Returns a list of Melon objects."""

    melon_list=[]
    melon1 = Melon("yw",  8,  7, "Field 2", "Sheila")
    melon_list.append(melon1)
    melon2 = Melon ("yw",  3,  4, "Field 2", "Sheila")
    melon_list.append(melon2)
    melon3 =  Melon ("yw",  9,  8, "Field 3", "Sheila")
    melon_list.append(melon3)
    melon4 = Melon ("cas",  10,  6, "Field 35", "Sheila")
    melon_list.append(melon4)
    melon5 = Melon  ("cren",  8,  9, "Field 35", "Micheal")
    melon_list.append(melon5)
    melon6 = Melon ("cren",  8,  2, "Field 35", "Micheal")
    melon_list.append(melon6)
    melon7 = Melon ("cren",  2,  3, "Field 4", "Micheal") 
    melon_list.append(melon7)
    melon8= Melon ("musk",  6,  7, "Field 4", "Micheal")   
    melon_list.append(melon8)
    melon9 = Melon ("yw",  7,  10, "Field 3", "Sheila")
    melon_list.append(melon9)

    return melon_list

melons = make_melons(melon_types)

def get_sellability_report(sellable, melons):
    """Given a list of melon object, prints whether each one is sellable."""
    for melon in melons:
        if sellable == True:
            print (melon)
    # Fill in the rest 



