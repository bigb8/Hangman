class HangmanSolver:
    """
    A class to assist in solving Hangman puzzles by suggesting the next best letter to guess
    and the best guess for the whole word based on the current state of the game and previous guesses.
    """

    def __init__(self, initial_state, dictionary):
        """
        Initializes the HangmanSolver with an initial state and a dictionary of possible words.
        
        :param initial_state: A string representing the initial state of the word to be guessed, e.g., "-------"
        :param dictionary: A list of strings representing the dictionary of possible words.
        """
        self.current_state = initial_state.upper()
        self.dictionary = [word.upper() for word in dictionary if len(word) == len(initial_state)]
        self.guessed_letters = set()
        self.possible_words = self.dictionary.copy()

    def update(self, guess, new_state, success):
        """
        Updates the solver's state based on the latest guess, the new state of the word, and whether the guess was successful.
        
        :param guess: The letter that was guessed.
        :param new_state: The new state of the word after the guess.
        :param success: 1 if the guess was successful (the letter is in the word), 0 otherwise.
        """
        self.current_state = new_state.upper()
        guess = guess.upper()
        if success:
            self.guessed_letters.add(guess)
            for i, char in enumerate(new_state):
                if char != '-':
                    self.possible_words = [word for word in self.possible_words if word[i] == char]
        else:
            self.guessed_letters.add(guess)
            self.possible_words = [word for word in self.possible_words if guess not in word]
        self.filter_possible_words()

    def filter_possible_words(self):
        """Filters the list of possible words based on the current state and guessed letters."""
        filtered_words = []
        for word in self.possible_words:
            match = True
            for i, char in enumerate(self.current_state):
                if char != '-' and word[i] != char:
                    match = False
                    break
            if match:
                filtered_words.append(word)
        self.possible_words = filtered_words

    def suggest_letter(self):
        """
        Suggests the next best letter to guess based on the current list of possible words and already guessed letters.
        
        :return: The suggested letter or None if no suggestions can be made.
        """
        letter_frequency = {}
        for word in self.possible_words:
            for letter in set(word):
                if letter not in self.guessed_letters:
                    letter_frequency[letter] = letter_frequency.get(letter, 0) + 1
        return max(letter_frequency, key=letter_frequency.get) if letter_frequency else None

    def suggest_word(self):
        """
        Suggests the best guess for the whole word if the list of possible words has been narrowed down sufficiently.
        
        :return: The suggested word or None if no single word can be determined.
        """
        if len(self.possible_words) == 1:
            return self.possible_words[0]
        return None
