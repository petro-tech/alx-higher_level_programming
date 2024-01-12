#!/usr/bin/python3

""" prints a text with 2 new lines after each of these characters: ., ? and : """
def text_indentation(text):
    # Check if text is a string
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Define the set of characters that trigger a new line
    trigger_characters = {'.', '?', ':'}

    # Initialize an empty line
    current_line = ""

    # Iterate through each character in the text
    for char in text:
        current_line += char

        # Check if the character is a trigger character
        if char in trigger_characters:
            # Print the current line without spaces at the beginning or end
            print(current_line.strip())
            # Start a new line
            current_line = ""

    # Print the last line if there is any text remaining
    if current_line:
        print(current_line.strip())
