from tkinter import*
import tkinter.font as font
import random

game_window = Tk()
game_window.title("Rock Paper Scissors Game")

app_font = font.Font(size=12)

#displaying game title
game_title = Label(text= "Rock Paper Scissors", font=font.Font(size=20), fg="grey")
game_title.pack()

#label to display who wins each time
winner_label = Label(text = "Let's Start the Game...", fg="green", font = font.Font(size = 13), pady = 8)
winner_label.pack()

input_frame = Frame(game_window)
input_frame.pack()

#Displaying player options
player_options = Label(input_frame, text = "Your Options : ", font = app_font, fg="grey")
player_options.grid(row = 0, column = 0, pady = 8)

rock_btn = Button(input_frame, text = "Rock", width=15, bd = 0, bg = "pink", pady=5, command=lambda: player_choice(options[0]))
rock_btn.grid(row = 1, column= 1, padx = 8, pady=5)

paper_btn = Button(input_frame, text = "Paper", width=15, bd = 0, bg = "orange", pady=5, command=lambda: player_choice(options[0]))
paper_btn.grid(row = 1, column= 2, padx = 8, pady=5)

scissors_btn = Button(input_frame, text = "Scissors", width=15, bd = 0, bg = "green", pady=5, command=lambda: player_choice(options[0]))
scissors_btn.grid(row = 1, column= 3, padx = 8, pady=5)



game_window.geometry('700x300')
game_window.mainloop