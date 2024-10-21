'''
    String formmatter for making notes from PDFs and creating
    flashcards from the notes.
'''

import pyperclip as pyclip
import tkinter as tk

def on_hello_click():
    print("Hello button clicked!")

def on_test_click():
    print("Test button clicked!")

def main():
    '''
        Main function. Runs on start.
    '''

    # menu_value = menu_logic()
    # while menu_value:
    #     menu_value = menu_logic()


    # Create the main window
    root = tk.Tk()
    root.title("Study Formatter")

    # Configure the root window's grid to expand
    root.grid_columnconfigure(0, weight=1)  # First column in the root
    root.grid_columnconfigure(1, weight=1)  # Second column in the root
    root.grid_rowconfigure(0, weight=1)     # Make the row stretch to fit the window

    # Create the buttons and place them in grid
    hello_button = tk.Button(root, text="Enter Remover", command=cleaner)
    hello_button.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

    test_button = tk.Button(root, text="Flashcard Formatter", command=fc_formatter)
    test_button.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

    # Set the window size
    root.geometry("400x200")

    # Start the tkinter loop
    root.mainloop()


# def menu_logic() -> int:

#     '''
#         Displays the cmdline UI to operate program.
#     '''

#     menu_items = ['Exit', 'Enter Remover', 'Flashcard Formatter']

#     print('Select the formatting action to perform:')

#     menu_last_index = len(menu_items) - 1
#     for i, x in enumerate(menu_items):
#         print(f'{i}: {x}', end='')
#         if i != menu_last_index:
#             print(' | ', end='')
#         else:
#             print(' ')

#     user_input = input()
#     if user_input.isdigit:
#         int_input = int(user_input)
#         if int_input == 1:
#             cleaner()
#         elif int_input == 2:
#             fc_formatter()
#         return int_input
#     else:
#         print('Please enter a valid menu number.')
#         return 1


def cleaner():
    '''
        Cleans the user input of any unnecessary enters and words spliced with a dash
    '''

    try:
        dirty_str = pyclip.paste()
    except ValueError:
        print('Entered non-valid string')

    # Split the text by lines to handle line-by-line processing
    lines = dirty_str.splitlines()

    # List to hold cleaned lines
    clean_lines = []

    # Process each line and handle hyphenation
    i = 0
    while i < len(lines):
        line = lines[i]

        # If the line ends with a hyphen, remove the hyphen and join with the next line
        if line.endswith('-') and i + 1 < len(lines):
            # Merge with the next line, removing the hyphen and newline
            line = line[:-1] + lines[i + 1].strip()
            clean_lines.append(line)
            # Skip the next line since we've already merged it
            i += 1
        else:
            clean_lines.append(line)

        i += 1

    # Join the cleaned lines together with spaces between them
    clean_buffer = ' '.join(clean_lines)

    # Replace any multiple spaces with a single space
    clean_buffer = ' '.join(clean_buffer.split())

    pyclip.copy(clean_buffer)


def fc_formatter():
    '''
        Formats text in notes.txt (within same folder) to a format
        usable for Quizlet's "AI Note Creator"
    '''
    # Read/Open notes text file
    all_notes = None

    with open("notes.txt", "r", encoding="utf8") as notes:
        all_notes = notes.read()

    # Split notes by enters
    indiv_notes = all_notes.split("\n")

    # Remove blank items from the individual notes
    indiv_notes = list(filter(lambda x: x != "", indiv_notes))

    # Remove "Answer: ", seperate Def/Term by tab, seperate each 'flashcard' by newline
    for i, x in enumerate(indiv_notes):
        if "answer:" in x.lower():
            ### Old Version ###
            # Add "Term:" to terms and change "Answer:" to "Definitiion:"
            # indiv_notes[i - 1] = "Term: " + indiv_notes[i - 1]
            # indiv_notes[i] = indiv_notes[i].replace("answer:", "Definition:")
            # indiv_notes[i] = indiv_notes[i].replace("Answer:", "Definition:")
            # indiv_notes[i] = indiv_notes[i] + '\n'

            indiv_notes[i] = indiv_notes[i].replace("answer: ", "")
            indiv_notes[i] = indiv_notes[i].replace("Answer: ", "")
            indiv_notes[i] = indiv_notes[i] + '\n'
        else:
            indiv_notes[i] = indiv_notes[i] + '\t'

    # Join list into hrd (human-readable data) and copy to clipboard
    formatted_notes = ''.join(map(str, indiv_notes))
    pyclip.copy(formatted_notes)

main()
