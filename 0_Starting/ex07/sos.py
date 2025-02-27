import sys

def morse_translate(string) -> str:
	""" takes a string and translates it into morse code """

	NESTED_MORSE = {
		'A':'.-', 'B':'-...','C':'-.-.', 'D':'-..',
		'E':'.','F':'..-.', 'G':'--.', 'H':'....',
		'I':'..', 'J':'.---', 'K':'-.-','L':'.-..',
		'M':'--', 'N':'-.','O':'---', 'P':'.--.',
		'Q':'--.-','R':'.-.', 'S':'...', 'T':'-',
		'U':'..-', 'V':'...-', 'W':'.--','X':'-..-',
		'Y':'-.--', 'Z':'--..','1':'.----', '2':'..---',
		'3':'...--','4':'....-', '5':'.....', '6':'-....',
		'7':'--...', '8':'---..', '9':'----.','0':'-----',
		' ':'/', '\n':'\n'}
	morse_code = []
	for c in string.upper():
		if c in NESTED_MORSE:
			morse_code.append(NESTED_MORSE[c])
		else:
			raise AssertionError(f"can't convert char '{c}'.")
	return ' '.join(morse_code)

def main():
	""" take a string as an arg, turn to morse code, ???, profit! """
	try:
		ac = len(sys.argv)
		if (ac != 2):
			raise AssertionError("the arguments are bad")
		
		res = morse_translate(sys.argv[1])
		print(res)

	except AssertionError as e:
		print(f"Assertion Error: {str(e)}") 

if __name__ == "__main__":
	main()