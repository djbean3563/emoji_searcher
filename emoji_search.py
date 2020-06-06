"""
This program allows the user to search for emojis
by keyword or to generate a random emoji.
"""
import random
import tkinter.filedialog

#creates the emoji dictionary 
#keys are emoji descriptions
#values are emojis
def create_dict(file):
    emoji_dict = {}
    count =0
    for line in file:
        try:
            key=line[1:len(line)-1]
            key=key.strip()
            value=line[0:1]
            emoji_dict[key]= value
        except:
            count+=1
    return emoji_dict

# Creates a list of emojis (no descriptions)
# that can be accessed by index.
# This is necessary to access a random emoji.
def create_list(file):
    emoji_list = []
    for line in file:
        emoji_list.append(line[0:1])
    return emoji_list
    
 #Searches for a emoji by keyword, or generates
#random emoji if user enters *   
def search(emoji_list, emoji_dict):
    keep_going = True
    while (keep_going):
        search = input("search or *: ")
        if search == "":
            keep_going = False
        elif "*" in search:
            wild= random.randint(0,len(emoji_dict)-1)
            print(emoji_list[wild])
        else:
            for key in emoji_dict:
                if search in key:
                    print(emoji_dict[key])
                
def main():
    try:
        root = tkinter.Tk()
        root.withdraw()
        file_name = tkinter.filedialog.askopenfilename()
        file = open(file_name)
        emoji_dict = create_dict(file)
        file.close()
        file = open(file_name)
        emoji_list = create_list(file)
        file.close()
        
    except IOError:
        print("no file")
    else:
        search(emoji_list, emoji_dict)

main()
