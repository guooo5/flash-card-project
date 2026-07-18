import pandas 
from tkinter import *
from collections import defaultdict
import random 

BACKGROUND_COLOR = "#B1DDC6"

#----data
data = pandas.read_csv("data/common_chinese_words.csv")
data_dict = defaultdict(list)
for row in data.itertuples():
    data_dict[row.Chinese] = row.English 

word = random.choice(list(data_dict.keys())) 
def change_text():
    global word, flip_timer 
    screen.after_cancel(flip_timer)
    
    word = random.choice(list(data_dict.keys()))     
    flash_card.itemconfig(card_title, text="Chinese", fill="black")
    flash_card.itemconfig(flash_card_word, text=word, fill="black")
    flash_card.itemconfig(flash_card_image, image=card_front)
    
    flip_timer = screen.after(3000, func=flip_card)

def flip_card():
    flash_card.itemconfig(card_title, text="English", fill="white")
    flash_card.itemconfig(flash_card_word, text=data_dict[word], fill="white")
    flash_card.itemconfig(flash_card_image, image=card_back)

def known_card():
    del data_dict[word]
    change_text()
    print(len(data_dict))
        
    
# def flip_card():
#     flash_card.itemconfig(flash_card_image, image=card_back)
#     flash_card.itemconfig(flash_card_word,text=data_dict[word])
#---gui 
#screen 
screen = Tk()
screen.title("Chinese Words Flash Card")
screen.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = screen.after(3000, func=flip_card) #timer after 3 secs flip

#card body
flash_card = Canvas(width=800, height=526)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
flash_card_image = flash_card.create_image(400, 263, image=card_front)

#text
card_title = flash_card.create_text(400, 150, text="Chinese", font=("Ariel", 40, "italic"), fill="black")

flash_card_word = flash_card.create_text(400, 263, text="word", font=("Ariel", 60, "bold"), fill="black")

flash_card.config(bg=BACKGROUND_COLOR, highlightthickness=0)
flash_card.grid(row=0, column=0, columnspan=2)


#buttons 
x_image = PhotoImage(file="images/wrong.png")
x_button = Button(image=x_image, highlightthickness=0, command=change_text)
x_button.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png")
check_button = Button(image=check_image, highlightthickness=0, command=known_card)
check_button.grid(row=1, column=1)



screen.mainloop()