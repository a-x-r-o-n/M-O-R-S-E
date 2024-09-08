# M-O-R-S-E

M-O-R-S-E is a simple Python project that converts between plain text and Morse code. It provides functionality to translate messages from plain text to Morse code and vice versa, supporting all lowercase letters of the alphabet.

## Features

- Convert plain text to Morse code.
- Convert Morse code to plain text.

## Project Structure

The project consists of the following files:

- **main.py**: This is the entry point of the application. It provides a simple menu for the user to select whether they want to convert plain text to Morse or Morse to plain text.
- **module.py**: This file contains the conversion logic for transforming plain text to Morse code and vice versa.

## How It Works

### Plain to Morse

The `plainToMorse()` function takes a plain text message as input and converts each letter into the corresponding Morse code. Each letter is separated by a space, and the spaces between words are represented by `.....` (5 dots).

### Morse to Plain

The `morseToPlain()` function takes a Morse code sequence as input and converts it back to plain text. It assumes each letter is separated by a space, and word boundaries are marked by `.....`.

### Morse Code Mapping

The Morse code for each letter is predefined and hardcoded in the **module.py** file. For example:

- `a`: `._`
- `b`: `_...`
- `c`: `_._.`

And so on for all letters of the alphabet.

## Getting Started

### Prerequisites

Make sure you have Python 3 installed on your machine.

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/M-O-R-S-E.git
   ```
2. Navigate to the project directory:
   ```bash
   cd M-O-R-S-E
   ```

### Running the Program

To run the program, simply execute `main.py`:

```bash
python main.py
```

### Usage

Once you run the program, you'll be presented with a menu to choose between two options:

1. Convert a plain text message to Morse code.
2. Convert a Morse code message to plain text.

- If you choose option 1, enter your plain text message, and the program will output the corresponding Morse code.
- If you choose option 2, enter a Morse code sequence (with letters separated by spaces and words by `.....`), and the program will convert it to plain text.

### Example

**Plain to Morse:**
```
Input: hello
Output: .... . ._.. ._.. ___
```

**Morse to Plain:**
```
Input: .... . ._.. ._.. ___
Output: hello
```


## Contributing

If you'd like to contribute to the project, feel free to fork the repository and submit a pull request. Please ensure your changes are well-tested.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
```

This `README.md` gives a detailed overview of the project's functionality, structure, and usage instructions, making it easy for users to understand and contribute.
