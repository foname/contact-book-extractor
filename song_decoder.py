import re

def songDecoder(str_input):
	return re.sub("(WUB)+", " ", str_input).strip()
