def abbrev_name(name):
    array = name.split()
    return array[0][0].upper() + "." + array[1][0].upper()
    
# Best practice version:
def abbrevName(name):
    first, last = name.upper().split(' ')
    return first[0] + '.' + last[0]