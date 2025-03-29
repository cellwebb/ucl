# How UCL Works

This document explains the internal architecture of UCL and how it generates changelog entries using various AI providers.

## Overview

UCL (Update Changelog) streamlines the changelog generation process by:

1. Analyzing your recent commits
2. Generating changelog entries using an AI provider
3. Formatting changelog entries in a standardized format
4. Optionally editing entries in your default editor

## Component Architecture

### Core Components

1. **Command Line Interface (core.py)**

   - Handles command-line arguments and orchestrates the workflow
   - Interacts with Git to get commit history
   - Handles user interaction

2. **AI Integration (utils.py)**

   - Manages communication with AI providers via aisuite
   - Formats prompts and parses responses
   - Counts tokens to optimize requests

3. **Configuration (config.py)**

   - Manages default settings and environment variables
   - Supports different AI providers and models

## The Workflow

### 1. Initialization

When you run `ucl`, the tool:

- Loads configuration from environment variables and .env file
- Processes command-line arguments
- Checks for recent commits

### 2. Generating Changelog Entries

The tool:

- Gets the commit history using `git log`
- Creates a prompt for the AI model
- Sends the prompt to the configured AI provider
- Receives structured changelog entries

### 3. Multi-Provider Support

UCL uses the aisuite library to abstract away provider-specific details:

1. **Provider Selection**

   - Set by `UCL_PROVIDER` environment variable or `--model` flag
   - Each provider needs its own API key

2. **Model Selection**

   - Each provider offers different models
   - Models are referenced using the format `provider:model_name`
   - Default models are defined in `PROVIDER_MODELS` in config.py

3. **Entry Generation**
   - The actual AI request is handled by aisuite
   - The prompt template is standardized across providers
   - Token counting ensures requests stay within limits

### 4. Changelog Management

After generating entries:

- The tool displays the suggested changelog entries
- The user can accept or reject the entries
- If accepted, the tool updates the changelog file
- Optionally opens the entries in your default editor for manual editing

## Provider Selection Logic

The logic for selecting a provider and model follows this precedence:

1. Command-line argument (`--model` or `-m`)
2. Environment variable `UCL_MODEL` (fully qualified model)
3. Environment variables `UCL_PROVIDER` and `UCL_MODEL_NAME`
4. Default configuration (Anthropic Claude)

This allows for flexible usage patterns, from project-wide configuration to one-off overrides.

## Provider-Specific Details

### Anthropic Claude (Default)

- Good at understanding code context
- Produces well-structured changelog entries
- API charges per token
- Default model: claude-3-haiku

### OpenAI GPT Models

- Fast response times
- Strong code understanding
- Subscription or per-token pricing
- Default model: gpt-4o

### Groq

- Low-latency responses
- Offers LLaMA-based models
- Free tier available
- Default model: llama3-70b-8192

### Mistral

- Range of model sizes
- Good balance of speed and quality
- Competitive pricing
- Default model: mistral-large-latest

### AWS Bedrock

- Access to multiple model families
- AWS infrastructure integration
- Pay-as-you-go pricing
- Default model: meta.llama3-1-70b-instruct-v1:0

### Azure OpenAI

- Enterprise-grade deployment
- Security and compliance features
- Microsoft infrastructure
- Default model: gpt-4

## Prompt Engineering

UCL uses a specific prompt format to guide the AI:

```text
Analyze this git log and write ONLY a changelog entry in the following format. Do not include any other text, explanation, or commentary.

Format:
[type]: Short summary of changes (50 chars or less)
 - Bullet point details about the changes
 - Another bullet point if needed

[feat/fix/docs/refactor/test/chore/other]: <description>

Git Log:
...
```

This prompt:

- Provides clear instructions on the desired output format
- Includes the Git log for context
- Encourages structured, conventional changelog entries

## Behind the Scenes: Token Management

UCL includes token counting functionality to:

1. Estimate prompt size before sending
2. Log token usage for monitoring
3. Optimize large diffs to stay within context windows

The token counting is provider-agnostic thanks to aisuite's abstraction layer.

## Environment Variables

UCL uses the following environment variables:

| Variable             | Description       | Example                    |
| -------------------- | ----------------- | -------------------------- |
| `ANTHROPIC_API_KEY`  | Anthropic API key | `sk-ant-api03-...`         |
| `OPENAI_API_KEY`     | OpenAI API key    | `sk-...`                   |
| `GROQ_API_KEY`       | Groq API key      | `gsk_...`                  |
| `MISTRAL_API_KEY`    | Mistral API key   | `...`                      |
| `UCL_PROVIDER`       | Provider to use   | `anthropic`                |
| `UCL_MODEL_NAME`     | Model name        | `claude-3-haiku`           |
| `UCL_MODEL`          | Full model ID     | `anthropic:claude-3-haiku` |
| `UCL_USE_FORMATTING` | Enable formatting | `true`                     |
| `UCL_MAX_TOKENS`     | Max output tokens | `8192`                     |

## Extending UCL

UCL can be extended to support additional providers by:

1. Adding the provider to `PROVIDER_MODELS` in config.py
2. Ensuring aisuite supports the provider
3. Documenting the API key environment variable

No changes to the core logic are needed as long as aisuite supports the provider.
