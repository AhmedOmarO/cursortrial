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

## Development

- Use `black` for code formatting
- Use `flake8` for linting
- Use `pytest` for testing

## Running Tests

```bash
pytest tests/
``` 