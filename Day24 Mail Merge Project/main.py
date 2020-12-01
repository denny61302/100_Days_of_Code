#TODO: Create a letter using starting_letter.docx 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
import docx2txt
with open("./Input/Names/invited_names.txt", "r") as file:
    names = file.readlines()
text = docx2txt.process("./Input/Letters/starting_letter.docx")

for name in names:
    strip_name = name.strip()
    new_content = text.replace("Dear ", f"Dear {strip_name}, ")
    with open(f"./Output/ReadyToSend/{strip_name}.txt", mode="w") as letter:
        letter.write(new_content)
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp