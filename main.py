import tkinter as tk
from tkinter import messagebox
import random

class GuessTheNumberGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Guess the Number Game")

        self.secret_number = random.randint(1, 20)
        self.attempts = 0
        self.max_attempts = 3

        self.label = tk.Label(self.master, text="Guess between number 1 to 20")
        self.label.pack()

        self.entry = tk.Entry(self.master)
        self.entry.pack()

        self.guess_button = tk.Button(self.master, text="Guess", command=self.check_guess)
        self.guess_button.pack()

    def check_guess(self):
        try:
            guess = int(self.entry.get())
            self.attempts += 1

            if guess == self.secret_number:
                messagebox.showinfo("Congratulations!", f"Correct! You guessed the number in {self.attempts} attempts.")
                self.reset_game()
            elif guess < self.secret_number:
                messagebox.showinfo("Too Low", "Try a higher number.")
            else:
                messagebox.showinfo("Too High", "Try a lower number.")

            self.entry.delete(0, tk.END)  # Clear the entry field

            if self.attempts == self.max_attempts:
                messagebox.showinfo("You Lose", f"Sorry, you didn't guess the number in {self.max_attempts} attempts.")
                self.reset_game()

        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")

    def reset_game(self):
        self.secret_number = random.randint(1, 20)
        self.attempts = 0

if __name__ == "__main__":
    root = tk.Tk()
    game = GuessTheNumberGame(root)
    root.mainloop()
