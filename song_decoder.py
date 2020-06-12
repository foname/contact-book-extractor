import re

def songDecoder(str_input):
    '''
    Returns a proper string without WUB.

    Parameters:
        str_input (str):The string contains information that need to be decoded.

    Returns:
        (str): Readable string 
    '''
    return re.sub("(WUB)+", " ", str_input).strip()
