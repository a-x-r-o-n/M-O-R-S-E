
# Morse Code Generator

This project is a simple Morse Code generator built using Python. It takes a string input and converts it into Morse Code.

## Features

- Converts any alphabetic string input to its corresponding Morse Code.
- Supports lowercase alphabets.
- Spaces between words in the message are replaced with Morse Code representation (`.....`).

## How It Works

The project consists of two files:
1. **module.py**: Contains a function `isAlphabet` that maps each letter to its corresponding Morse Code.
2. **main.py**: Handles the user input, processes each character, and generates the final Morse Code output.

### Morse Code Mapping
The mapping of alphabets to Morse Code is as follows:
- A: `._`
- B: `_...`
- C: `_._.`
- ...
- Z: `__..`

## Getting Started

### Prerequisites
- Python 3.x installed on your machine.

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/morse-code-generator.git
   ```
2. Navigate to the project directory:
   ```bash
   cd morse-code-generator
   ```

### Usage

1. Run the `main.py` script:
   ```bash
   python main.py
   ```
2. Enter your message when prompted. The program will output the corresponding Morse Code.

### Example

```bash
Enter your message: hello world
Morse code for the message hello world: .... . ._.. ._.. ___ ..... .__ ___ ._. ._.. _..
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

- **Your Name** - [GitHub Profile](https://github.com/a-x-r-o-n)
