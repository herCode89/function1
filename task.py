conv_dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
             '8': 8, '9': 9, 'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15}  # A map


def conv_num(arg: str = None):  # arg returns a string
    arg = arg.strip().lower()  # .lower returns a string in lowercase everything before a '.' gets modified
    if not len(arg):  # to handle empty cases
        return None  # return none lol
    neg: bool = arg[0] == '-'  # evaluate first before right side neg. given type bool to run through id to check
    if neg:  # negative bool is a variable type equal result after arg 0, if negative arg without all
        arg = arg[1:]  # characters from first pos to last (how every many there are then hex is bool test)
    hex_num: bool = arg[0:2] == '0x'  # hex bool is 0-1 exclusive. if first two characters is 0x then strip off
    if hex_num:
        arg = arg[2:]
    if not len(arg) or arg.count('.') > 1:
        return None
    result = 0
    # find the dec minus len +1 when you find dec go into string 0 relative and find where dec is
    power = (arg.find('.') - len(arg) + 1) if '.' in arg else 0
    # pos in arg start at very right is len -1 string is 0 relative go to len 0 and to 01
    for pos in range(len(arg) - 1, -1, -1):
        if arg[pos] != '.':  # if pos not equal to dec
            if not arg[pos] in conv_dict.keys(): 
                return None
            if not hex_num and conv_dict[arg[pos]] > 9:
                return None
            # bool set above if hex digit do base 16 (if True) and power if not then do base 10 (if False) and power
            result = result + (conv_dict[arg[pos]] * 16 ** power if hex_num else conv_dict[arg[pos]] * 10 ** power)
            power += 1  # after loop increase power by 1
    return -result if neg else result  # if negative get back negative result, otherwise get back positive result
