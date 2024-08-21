def new_list():
    newlist = {
        "elements" : [],
        "size" : 0,
    }
    return newlist

def get_element(mylist, pos):
    return mylist['elements'][pos-1]

def is_present(mylist, element, cmp_function):
    size = my_list["size"]
    if size>0:
        keyexist == false
        for keypos in range (0,size):
            info = mylist["elements"][keypos]
            if (cmp_function(element, info) == 0):
                keyexist == True
                break
        if keyexist:
            return keypos
    return -1

def add_first():
    pass

def add_last():
    pass

def size():
    pass

def first_element():
    pass