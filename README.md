# Hangman Assistant

Welcome to the Hangman Assistant project! This repository contains Python code designed to assist in solving hangman puzzles. Whether you're playing a game of hangman online, with friends, or just looking for a tool to help you crack word puzzles, the Hangman Assistant is here to suggest the next best letter or even guess the word for you. The repositoty is also an inspiration as how to make code with large language models, such as ChatGPT, based on a research meetup at CAMES (Copenhagen Academy for Medical Education and Simulation). The whole process of generation of code using GPT is shared [GPT session](https://chat.openai.com/share/4c1e17fa-449c-4b71-8603-2f897f875191)

## Features

- **Automatic Letter Suggestion**: Given the current state of the hangman puzzle, the Hangman Assistant suggests the most likely letter to guess next.
- **Word Guessing**: Based on the letters already guessed and the current state of the puzzle, the assistant can also suggest what the whole word might be.
- **Tkinter GUI**: A simple and intuitive graphical user interface to input the current puzzle state and view suggestions.

## Getting Started

To get started with Hangman Assistant, clone this repository and ensure you have Python installed on your system.

### Prerequisites

- Python 3.x

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/hangmanassistant.git
   ```
2. Navigate to the cloned directory:
   ```bash
   cd hangmanassistant
   ```
3. Run the application:
   ```bash
   python hangmanassistant.py
   ```

## Usage

After starting the Hangman Assistant, simply enter the current state of your hangman puzzle (e.g., `--a--n`) and any letters you've already guessed. The assistant will update its suggestions in real-time.

## Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

To contribute:
1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a pull request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- A special thanks to OpenAI and the ChatGPT platform for providing the foundational code and assistance in developing the Hangman Assistant. The guidance and code contributions from ChatGPT were instrumental in bringing this project to life. [GPT session](https://chat.openai.com/share/4c1e17fa-449c-4b71-8603-2f897f875191)
- Gratitude to the Python and Tkinter communities for the wealth of resources and documentation that made building a graphical user interface straightforward and accessible.
- Thank you to all hangman enthusiasts and puzzle solvers for the inspiration behind creating a tool that makes solving hangman puzzles not just easier, but also more fun.
- Lastly, I'd like to express my appreciation to anyone who uses, contributes to, or learns from this project. Your engagement and feedback are what drive open-source projects forward.


## Word List Requirement

The Hangman Assistant requires a list of words to function correctly. This list serves as the dictionary from which the assistant suggests letters and guesses words based on the current state of the puzzle.

### Finding a Word List

You can find suitable word lists for the Hangman Assistant in various places:

- **[SCOWL (Spell Checker Oriented Word Lists)](http://wordlist.aspell.net/)**: SCOWL offers customizable word lists that can be tailored to different levels of difficulty or language variations.
- **[The English Open Word List (EOWL)](https://diginoodles.com/projects/eowl)**: EOWL is a free and publicly available word list that contains thousands of English words, suitable for a variety of applications including word games.
- **GitHub Repositories**: There are numerous GitHub repositories that provide comprehensive word lists for English and other languages. A quick search for "word list" or "dictionary list" on GitHub can yield useful results.

### Using a Word List

After obtaining a word list, you'll need to load it into the Hangman Assistant. The application expects the word list to be in the form of a Python list, where each word is a string. For larger word lists, consider loading the list from a file to avoid hard-coding it directly into your scripts.

For example, to load a word list from a file named `wordlist.txt` where each line contains a word:

```python
def load_word_list(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]

# Example usage
dictionary = load_word_list('path/to/wordlist.txt')
```

Remember to replace `'path/to/wordlist.txt'` with the actual path to your word list file.
