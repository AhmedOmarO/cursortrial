# Python Test Project

This is a sample Python project to test Cursor capabilities. The project includes a basic structure and common development tools.

## Project Structure

```
.
├── src/           # Source code
├── tests/         # Test files
├── docs/          # Documentation
├── requirements.txt   # Project dependencies
```

## Setup

1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Unix/macOS
   ```

2. Install dependencies:
   ```bash
   pip install --index-url https://pypi.org/simple -r requirements.txt
   ```

## Usage

### Command Line Interface

Run the calculator from the command line:
```bash
python src/cli.py
```

The CLI provides a menu-driven interface with the following operations:
1. Add - Add two numbers
2. Subtract - Subtract second number from first
3. Multiply - Multiply two numbers
4. Divide - Divide first number by second
5. Exit - Exit the calculator

## Development

- Use `black` for code formatting
- Use `flake8` for linting
- Use `pytest` for testing

## Running Tests

```bash
pytest tests/
``` 