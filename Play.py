password = 	raw_input("What is the password?: ")
available_chars = raw_input("What characters could be in the password? ")
length = int(raw_input("How long is the password? From: "))       # The minimum and starting length of the password
max_length = int(raw_input("To: "))            # User defined input on how long the password can be
char_list = list(available_chars)              # Makes the available characters into a list
last_char = char_list[len(char_list) - 1]      # The last character available
guess = list(char_list[0] * length)            # The current password being tried
changing_char_pos = len(guess) - 1             # The character that is currently being cycled through
first_chars = guess[0:changing_char_pos]       # The characters in front of the character being cycled through
rest_of_chars = guess[changing_char_pos + 1:len(char_list) - 1]   # The characters after the character being cycled through

while length < max_length + 1:           # Keeps going until the length of the passwords attempted is longer than the user defined max length
	changing_char_pos = length - 1       # Sets the position of the changing character to the last one
	for char in available_chars:         # Cycles through each character available
		guess = guess[0:changing_char_pos] + list(char) + guess[changing_char_pos + 1:len(char_list) - 1]     # Keeps the password currently being tried the same except for one character
		if "".join(guess) == password:   # If the password being tried is correct
			print "The password is: " + "".join(guess)   # prints the password
			length += max_length              #break the loop by increasing the length of the password
			break
		print	"".join(guess)           # Prints the password being tried each time. Greatly slows down the process. Comment out for faster speed
	guess[changing_char_pos] = char_list[0] # returns the letter that was being tried back to the first character.
	changing_char_pos -= 1               # Moves the place of the character being changed to the left one, second to last position.
	while guess[changing_char_pos] == last_char:  # If the character being changed is the last character available. Repeat until the character is not the last characer
		guess[changing_char_pos] = char_list[0] # reset it to the first character
		changing_char_pos -= 1     # go left one position
		if changing_char_pos < 0:        # For when trying one letter attempts, changing_char_pos will go to -2 and give an error
			break
	if changing_char_pos >= 0:           # If the position of the character being changed is still a valid position
		guess[changing_char_pos] = char_list[char_list.index(guess[changing_char_pos]) + 1]         # The character at the position being changed is changed to ---> Find the index of it, add one, then get the next character
	if changing_char_pos < 0:            # Once the position of the character being changed has reached past the first character, add one to the length of the password
		length += 1
