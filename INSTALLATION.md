# Installation Guide

This guide provides instructions for installing and configuring UCL (Update Changelog) with support for multiple AI providers.

## Quick Start

1. Install UCL:

   ```bash
   pipx install ucl
   ```

2. Set up at least one AI provider (Anthropic Claude is the default):

   ```bash
   export ANTHROPIC_API_KEY=your_api_key_here
   ```

3. Start using UCL:

   ```bash
   # Generate changelog entries from recent commits
   ucl
   ```

## Installation Methods

### Recommended: Install with pipx

[pipx](https://pypa.github.io/pipx/) installs the package in an isolated environment while making the CLI commands globally available.

1. Install pipx if you don't have it:

   ```bash
   # On macOS
   brew install pipx
   pipx ensurepath

   # On Ubuntu/Debian
   sudo apt update
   sudo apt install python3-pip python3-venv
   python3 -m pip install --user pipx
   python3 -m pipx ensurepath

   # On Windows
   pip install pipx
   pipx ensurepath
   ```

2. Install UCL:

   ```bash
   pipx install ucl
   ```

3. Verify installation:

   ```bash
   ucl --help
   ```

### Alternative: Install with pip

```bash
# Standard installation
pip install ucl

# Or user installation
pip install --user ucl
```

### Install from Source

For developers or to get the latest changes:

```bash
# Clone the repository
git clone https://github.com/cellwebb/ucl.git
cd ucl

# Install in development mode
pip install -e .
```

## AI Provider Setup

UCL supports multiple AI providers. You need to set up at least one:

### Anthropic Claude (Default)

1. Register at [console.anthropic.com](https://console.anthropic.com/)
2. Create an API key and set it:

   ```bash
   export ANTHROPIC_API_KEY=your_key_here
   ```

### OpenAI (GPT-4, GPT-3.5)

1. Register at [platform.openai.com](https://platform.openai.com/)
2. Create an API key and set it:

   ```bash
   export OPENAI_API_KEY=your_key_here
   ```

### Groq

1. Register at [console.groq.com](https://console.groq.com/)
2. Create an API key and set it:

   ```bash
   export GROQ_API_KEY=your_key_here
   ```

### Mistral

1. Register at [console.mistral.ai](https://console.mistral.ai/)
2. Create an API key and set it:

   ```bash
   export MISTRAL_API_KEY=your_key_here
   ```

### Other Providers

For other providers like AWS Bedrock, Azure, or Google, see the documentation for each provider in the `.env.example` file.

## Configuration

### Using Environment Variables

Add your configuration to your shell profile (e.g., `~/.bashrc` or `~/.zshrc`):

```bash
# AI Provider Keys
export ANTHROPIC_API_KEY=your_api_key_here
# export OPENAI_API_KEY=your_api_key_here
# export GROQ_API_KEY=your_api_key_here
# export MISTRAL_API_KEY=your_api_key_here

# UCL Configuration
export UCL_PROVIDER=anthropic  # Choose: anthropic, openai, groq, mistral, aws
# export UCL_MODEL_NAME=claude-3-haiku  # Model name for the selected provider
# export UCL_MODEL=openai:gpt-4o  # Or set a fully qualified model (overrides provider and model name)
# export UCL_MAX_TOKENS=8192  # Maximum output tokens
```

### Using .env Files

Alternatively, create a `.env` file in your project directory with the same variables. This is useful for project-specific configurations.

### Using Command-Line Options

Override the model for a single run:

```bash
ucl -m openai:gpt-4o
```

## Basic Usage

1. Generate changelog entries:

   ```bash
   ucl
   ```

2. Additional options:

   ```bash
   # Generate entries without prompts
   ucl -f

   # Format existing changelog entries
   ucl -F

   # Use a specific model
   ucl -m groq:llama3-70b-8192
   ```

## Troubleshooting

### Common Issues

1. **API Key Not Recognized**

   If you get errors about missing API keys, ensure you've:

   - Exported the correct environment variable
   - Restarted your terminal session after adding to your profile
   - Checked for typos in your API key

2. **Command Not Found**

   If the `ucl` command isn't found:

   - Ensure the Python bin directory is in your PATH
   - Try installing with `pipx` instead of `pip`
   - For pip installations, you might need to add `~/.local/bin` to your PATH:

     ```bash
     export PATH="$HOME/.local/bin:$PATH"
     ```

3. **Dependency Errors**

   If you encounter dependency errors:

   ```bash
   pip install --upgrade 'ucl[all]'
   ```

4. **Model Not Found**

   If you get errors about models not being found:

   - Check that you've specified the correct model ID
   - Verify that your API key has access to the requested model
   - Try using a different model from the same provider

### Getting Help

If you continue to experience issues:

1. Run UCL in verbose mode for more information:

   ```bash
   ucl -v
   ```

2. Check the [GitHub issues](https://github.com/cellwebb/ucl/issues) for similar problems and solutions

3. Open a new issue with the error details and steps to reproduce
