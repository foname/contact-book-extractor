import re

names = []
def capture_name(match):
    names.append(match)
    return

def split_name_and_address(capture_name, str_name_address):
    global names
    names = []
    address = re.sub('<(.*)>', capture_name, str_name_address)
    address = re.sub('[^0-9a-zA-Z-.]+'," ", address)
    name = names[0].group(1)
    return name, address.strip()

def phone(str_input, phone_num):
    '''
    Returns a string that consist of phone number, name, and address.

    Parameters:
        str_input (str):The string contains un-organized contact information.
        phone_num (str):The string phone number ex."48-421-674-8974".

    Returns:
        (str):String of "Phone => {phone_number}, Name => {name}, Address => {address}")  
    '''

    result = re.findall("\+{}".format(phone_num), str_input)
    if not result:
        return "Error => Not found: {}".format(phone_num)
    elif len(result) > 1:
        return "Error => Too many people: {}".format(phone_num)
    else:
        phone = re.search("\+{}".format(phone_num), str_input)
        first_index = max(0,str_input.rfind('\n', 0, phone.start()))
        last_index = str_input.find('\n', phone.end())
        if last_index < 0:
            last_index = len(str_input)
        str_subject = str_input[first_index:last_index]
        name_and_address = re.sub("\+{}".format(phone_num), "", str_subject)
        name, address = split_name_and_address(capture_name, name_and_address)
        return "Phone => {}, Name => {}, Address => {}".format(phone_num, name, address)
    return
