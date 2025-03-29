# ucl (Update Changelog)

[![Tests](https://github.com/cellwebb/ucl/actions/workflows/ci.yml/badge.svg)](https://github.com/cellwebb/ucl/actions/workflows/ci.yml)
[![Code Coverage](https://codecov.io/gh/cellwebb/ucl/graph/badge.svg?token=WXOSX7R2JH)](https://codecov.io/gh/cellwebb/ucl)
[![PyPI - Version](https://img.shields.io/pypi/v/ucl.svg)](https://pypi.org/project/ucl)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/ucl.svg)](https://pypi.org/project/ucl)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A CLI tool (pronounced like "you see ell") that uses large language models to generate and update changelog entries based on your git commits.

## Features

- Automatically generates meaningful changelog entries using various LLM providers
- Supports multiple AI providers (Anthropic Claude, OpenAI, Groq, Mistral, and more)
- Formats changelog entries in a standardized format
- Interactive prompts for changelog generation and editing
- Supports various flags for different workflows

## Installation

```console
pipx install ucl
```

## Configuration

### API Keys

Set up your API keys for the provider you want to use:

```console
# For Anthropic Claude (default)
export ANTHROPIC_API_KEY=your_api_key_here

# For OpenAI
export OPENAI_API_KEY=your_api_key_here

# For Groq
export GROQ_API_KEY=your_api_key_here

# For Mistral
export MISTRAL_API_KEY=your_api_key_here
```

For permanent configuration, add this to your shell profile (~/.zshrc, ~/.bashrc, etc.)

### Provider Configuration

You can specify which LLM provider and model to use:

```console
# Set provider (anthropic, openai, groq, mistral, aws, etc.)
export UCL_PROVIDER=anthropic

# Optionally, set a specific model name for the provider
export UCL_MODEL_NAME=claude-3-5-sonnet-20240620

# Or set a fully qualified model
export UCL_MODEL=openai:gpt-4o
```

## Usage

### Basic Usage

Run ucl to generate changelog entries based on your recent commits:

```console
ucl
```

### Command Line Options

- `--test`: Run in test mode with example changelog entries
- `--force, -f`: Skip all prompts (auto-yes)
- `--edit, -e`: Open generated changelog entries in your default editor
- `--format, -F`: Format existing changelog entries

Example:

```console
# Generate changelog entries without prompts
ucl -f
```

## Project Structure

```plaintext
ucl/
├── src/
│   └── ucl/
│       ├── __init__.py
│       ├── core.py
│       └── utils.py
├── tests/
├── .gitignore
├── LICENSE.txt
├── README.md
└── pyproject.toml
```

## Contributing

For development instructions, see [DEVELOPMENT.md](DEVELOPMENT.md).

1. Fork the repository
2. Create a new branch for your feature
3. Make your changes
4. Run tests and linting
5. Submit a pull request

## License

MIT
