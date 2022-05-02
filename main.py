from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_index = 0

with open(file="data/french_words.csv") as word_list_data:
    data = pandas.read_csv(word_list_data)
    french_list = data["French"].tolist()
    english_list = data["English"].tolist()

words_to_learn = [[], []]
for word in french_list:
    words_to_learn[0].append(word)
for word in english_list:
    words_to_learn[1].append(word)


# Word/Language Fetcher


def get_fr_word(index):
    french_word = words_to_learn[0][index]

    canvas.itemconfig(card_img, image=card_front_img)
    canvas.itemconfig(language_txt, text="French", fill="black")
    canvas.itemconfig(word_txt, text=french_word, fill="black")


def get_en_word(index):
    english_word = words_to_learn[1][index]

    canvas.itemconfig(card_img, image=card_back_img)
    canvas.itemconfig(language_txt, text="English", fill="black")
    canvas.itemconfig(word_txt, text=english_word, fill="black")


def get_words():
    global current_index
    current_index = random.randint(0, len(words_to_learn[0]) - 1)
    get_fr_word(current_index)

    window.update()

    window.after(3000)

    get_en_word(current_index)

# Next Word

def next_correct():
    fr_words = words_to_learn[0]
    fr_word = fr_words[current_index]
    words_to_learn[0].remove(fr_word)
    en_words = words_to_learn[1]
    en_word = en_words[current_index]
    words_to_learn[1].remove(en_word)
    print(words_to_learn)

    get_words()


def next_incorrect():
    get_words()


# User Interface

window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(window, width=800, height=550, highlightthickness=0)
canvas.config(bg=BACKGROUND_COLOR)
canvas.grid(column=0, row=0, columnspan=2)


# Images
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
right_img = PhotoImage(file="images/right.png")
wrong_img = PhotoImage(file="images/wrong.png")

card_img = canvas.create_image(400, 270, image=card_front_img)

# Buttons

right_btn = Button(image=right_img, highlightthickness=0, command=next_correct)
wrong_btn = Button(image=wrong_img, highlightthickness=0, command=next_incorrect)
right_btn.grid(column=0, row=1)
wrong_btn.grid(column=1, row=1)

# Canvas Text

language_txt = canvas.create_text(
    400, 150,
    # fill="black",
    font=("Ariel", 30, "italic"),
    text="Language")

word_txt = canvas.create_text(
    400, 250,
    # fill="black",
    font=("Ariel", 50, "bold"),
    text="Word")


get_words()


window.mainloop()


# canvas.itemconfig(language_txt, text="Text changed", fill="Blue")