class Item:
    '''
    Purpose:
        An object of this class represents a single item available for purchase.
    Instance variables:
        name: A string describing what the item is called.
        price: A float numnber describing the item’s price in USD.
        category: A string that describes where the item is worn.
            It must be one of four values: 'Head', 'Torso', 'Legs', or 'Feet'.
        store: a string that describes the name of the store where the item can
        be found.
    Methods:
        __str__ Method: To return a string in the format "<name>, <category>, <store>: $<price>"
        __lt__ Method: To return the Boolean value "True" if the item in the
        left has a lower price than the item on the right.

    '''
    def __init__(self,name,price,category,store):
        self.name = name
        self.price = price
        self.category = category
        self.store = store
    def __str__(self):
        return str(self.name) + ", " + str(self.category) + ', ' + str(self.store) + ': $' + str(self.price)
    def __lt__(self,other):
        if self.price < other.price:
            return True
        else:
            return False

class Store:
    '''
    Purpose:
        An object of this class represents the inventory of a given Store.
    Instance variables:
        name: A string representing the name of the store
        items: A list of Item objects, representing every item in the store’s
        inventory.
    Methods:
        __str__ Method: This method will return a string containing the name of
        the store followed by the string representation of each item the store
        has.
    '''
    def __init__(self,name,items):
        self.name = name
        self.items = []
        fp = open(items)
        fp1 = fp.readlines()
        for i in fp1[1:]:
            b=i.split(',')
            newlist = []
            for i in b:
                x = i.replace('\n','')
                newlist.append(x)
            self.items.append(Item(newlist[0],float(newlist[1]),newlist[2],self.name))
    def __str__(self):
        string = ''
        string += str(self.name) + '\n'
        for i in self.items:
            string += str(i) + '\n'
        return string

def cheap_outfit(store_list):
    head = []
    torso = []
    legs = []
    feet = []
    for i in store_list:
        store = i.items
        for item in store:
            if item.category == 'Head':
                head.append(item)
            if item.category == 'Torso':
                torso.append(item)
            if item.category == 'Legs':
                legs.append(item)
            if item.category == 'Feet':
                feet.append(item)
    d = {'Head':min(head), 'Torso':min(torso), 'Legs':min(legs), 'Feet':min(feet)}
    return d
