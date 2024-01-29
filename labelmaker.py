def create_label(text, whitespace_width=3, side_symbol="|", top_symbol="_", top_text="", top_text_left_side_symbol="{", top_text_right_side_symbol="}", bottom_symbol="‾"):
    '''Takes the following parameters: text(list of strings), whitespace_width(int), side_symbol(string), top_symbol(string), bottom_symbol(string).
    Returns the text as a string, centered on a label, customized to your specifications.'''

    ret_list = []
    ret_string = ""
    longest_string = 0

    for element in text:
        if len(element) > longest_string:
            longest_string = len(element)

    if top_text == "":
        ret_list.append(" " + top_symbol * ((len(side_symbol) * 2 - 2) + whitespace_width * 2 + longest_string) + " ")
    else:
        if longest_string % 2 == 0:
            if len(top_text) % 2 == 0:
                ret_list.append(" " + ((longest_string//2 - len(top_text)//2 + whitespace_width - (len(top_text_left_side_symbol) + 1)) * top_symbol) + top_text_left_side_symbol + " " + top_text + " " + top_text_right_side_symbol + ((longest_string//2 - len(top_text)//2 + whitespace_width - (len(top_text_right_side_symbol) + 1)) * top_symbol) + " ")
            else:
                ret_list.append(" " + ((longest_string//2 - len(top_text)//2 + whitespace_width - (len(top_text_left_side_symbol) + 1)) * top_symbol) + top_text_left_side_symbol + " " + top_text + " " + top_text_right_side_symbol + ((longest_string//2 - len(top_text)//2-1 + whitespace_width - (len(top_text_right_side_symbol) + 1)) * top_symbol) + " ")
        else:
            if len(top_text) % 2 == 0:
                ret_list.append(" " + ((longest_string//2 - len(top_text)//2 + whitespace_width - (len(top_text_left_side_symbol) + 1)) * top_symbol) + top_text_left_side_symbol + " " + top_text + " " + top_text_right_side_symbol + ((longest_string//2 - len(top_text)//2+1 + whitespace_width - (len(top_text_right_side_symbol) + 1)) * top_symbol) + " ")
            else:
                ret_list.append(" " + ((longest_string//2 - len(top_text)//2 + whitespace_width - (len(top_text_left_side_symbol) + 1)) * top_symbol) + top_text_left_side_symbol + " " + top_text + " " + top_text_right_side_symbol + ((longest_string//2 - len(top_text)//2 + whitespace_width - (len(top_text_right_side_symbol) + 1)) * top_symbol) + " ")

    for i in range(whitespace_width//3):
        ret_list.append(side_symbol + (whitespace_width * 2 + longest_string) * " " + side_symbol)

    for index in range(len(text)):
        if longest_string % 2 == 0:
            if len(text[index]) % 2 == 0:
                ret_list.append(side_symbol + ((longest_string//2 - len(text[index])//2 + whitespace_width) * " ") + text[index] + ((longest_string//2 - len(text[index])//2 + whitespace_width) * " ") + side_symbol)
            else:
                ret_list.append(side_symbol + ((longest_string//2 - len(text[index])//2 + whitespace_width) * " ") + text[index] + ((longest_string//2 - len(text[index])//2-1 + whitespace_width) * " ") + side_symbol)
        else:
            if len(text[index]) % 2 == 0:
                ret_list.append(side_symbol + ((longest_string//2 - len(text[index])//2 + whitespace_width) * " ") + text[index] + ((longest_string//2 - len(text[index])//2+1 + whitespace_width) * " ") + side_symbol)
            else:
                ret_list.append(side_symbol + ((longest_string//2 - len(text[index])//2 + whitespace_width) * " ") + text[index] + ((longest_string//2 - len(text[index])//2 + whitespace_width) * " ") + side_symbol)

    for i in range(whitespace_width//3):
        ret_list.append(side_symbol + (whitespace_width * 2 + longest_string) * " " + side_symbol)

    ret_list.append(" " + bottom_symbol * ((len(side_symbol) * 2 - 2) + whitespace_width * 2 + longest_string) + " ")

    for index in range(len(ret_list)):
        ret_string += ret_list[index]
        if index < len(ret_list) - 1:
            ret_string += "\n"

    return ret_string