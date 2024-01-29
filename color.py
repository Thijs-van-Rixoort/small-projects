from random import randint

def convert_string_to_int(color):
    '''Takes the following parameter: color(Hexadecimal colorstring).
    returns the integer representation of the given hexadecimal colorstring.'''

    number_dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    color = color.upper()

    if len(color) == 7:
        color = color[1::]

    return [number_dict[color[0]] * 16 + number_dict[color[1]], number_dict[color[2]] * 16 + number_dict[color[3]], number_dict[color[4]] * 16 + number_dict[color[5]]]

def convert_int_to_string(color):
    '''Takes the following parameter: color(List consisting of 3 bytes, which represent a color value).
    returns the hexadecimal representation of the given color in integers.'''

    letter_dict = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    ret_string = '#'

    for value in color:
        ret_string += letter_dict[value // 16]
        ret_string += letter_dict[value % 16]

    return ret_string

def gradient(color_list, amount=25):
    '''Takes the following parameters: color_list(List of hexadecimal colorstrings), step(An int representing the step amount between two colorvalues that have the smallest difference).
    Returns a list of hexadecimal colorstrings which represent a gradient.'''

    color_list_int = []
    ret_list = []

    for color in color_list:
        color_list_int.append(convert_string_to_int(color))

    for i in range(len(color_list_int)):

        if i < len(color_list_int)-1:

            for j in range(amount):
                ret_list.append(convert_int_to_string([color_list_int[i][0] + (j * ((color_list_int[i+1][0] - color_list_int[i][0]))) // amount, color_list_int[i][1] + (j * ((color_list_int[i+1][1] - color_list_int[i][1]))) // amount, color_list_int[i][2] + (j * ((color_list_int[i+1][2] - color_list_int[i][2]))) // amount]))
            
        else:
            ret_list.append(convert_int_to_string(color_list_int[i]))

    return ret_list

def create_random_color():
    return convert_int_to_string([randint(0, 255), randint(0, 255), randint(0, 255)])

def get_color_negative(color):
    color_list_int = convert_string_to_int(color)
    for i in range(len(color_list_int)):
        if 255 - color_list_int[i] > 64 and 255 - color_list_int[i] < 192:
            if 255 - color_list_int[i] < 128:
                color_list_int[i] = 0
            else:
                color_list_int[i] = 255
        else:
            color_list_int[i] = 255 - color_list_int[i]

    return convert_int_to_string(color_list_int)