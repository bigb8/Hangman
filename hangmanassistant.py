import tkinter as tk
from tkinter import simpledialog, messagebox

from hangmansolver import HangmanSolver

import tkinter as tk
from tkinter import Label, Entry, Button, StringVar

class HangmanSolverGUI:
    def __init__(self, master, dictionary):
        self.master = master
        master.title("Hangman Solver")
        
        self.dictionary = dictionary
        self.solver = HangmanSolver("------", self.dictionary)  # Initial state with 6 unknowns as an example

        # Word State
        Label(master, text="Current Word State:").pack()
        self.word_state_entry = Entry(master)
        self.word_state_entry.pack()

        # Guess History
        Label(master, text="Guess History (a,b,c):").pack()
        self.guess_history_entry = Entry(master)
        self.guess_history_entry.pack()

        # Update Button
        Button(master, text="Update", command=self.update_solver).pack()

        # Best Guess for Letter
        Label(master, text="Best Guess for Letter:").pack()
        self.best_guess_letter_var = StringVar()
        Label(master, textvariable=self.best_guess_letter_var).pack()

        # Best Guess for Word
        Label(master, text="Best Guess for Word:").pack()
        self.best_guess_word_var = StringVar()
        Label(master, textvariable=self.best_guess_word_var).pack()

    def update_solver(self):
        word_state = self.word_state_entry.get().upper()
        guess_history = self.guess_history_entry.get().replace(" ", "").upper().split(',')
        
        # Reset solver with new word state
        self.solver = HangmanSolver(word_state, self.dictionary)
        
        # Update solver based on guess history
        for guess in guess_history:
            if guess:
                # Mock update call (adapt based on how your actual solver handles updates)
                success = 1 if guess in word_state else 0
                self.solver.update(guess, word_state, success)
        
        # Update UI with best guesses
        self.best_guess_letter_var.set(self.solver.suggest_letter())
        self.best_guess_word_var.set(self.solver.suggest_word() or "Keep guessing!")

# Example usage
example_dictionary = ['python', 'hangman', 'computer', 'keyboard', 'mouse', 'monitor', 'laptop', 'speaker', 'camera']
root = tk.Tk()
gui = HangmanSolverGUI(root, example_dictionary)
root.mainloop()
