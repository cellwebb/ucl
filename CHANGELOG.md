<!-- markdownlint-disable MD024-->

# Changelog

All notable changes to the Universal Changelog Language (UCL) project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0] - 2025-03-29

### Added

- Initial release of ucl CLI tool
- Core functionality to generate changelog entries using AI
- Multi-provider support via aisuite integration
- Support for multiple AI providers:
  - Anthropic Claude
  - OpenAI GPT models
  - Groq LLaMA models
  - Mistral AI
  - AWS Bedrock
  - Azure OpenAI
  - Google Vertex AI
- Command-line model selection with `--model` or `-m` flag
- Environment variables loading from .env file
- GitHub Actions CI workflow with multiple Python versions
- Codecov integration for test coverage reporting

### Changed

- Migrated from `hatch` to `uv` for package management
- Updated development workflow to use `Makefile` for common tasks
- Improved development environment setup
- Switched from `bumpversion` to `bump-my-version` for version management

### Fixed

- Enhanced error handling and import configurations
- Updated `.env.example` with UCL configuration details
- Improved token counting across different providers
- Enhanced error handling in configuration and AI interaction

### Security

- Added environment variable support for securely managing API keys
- Enhanced configuration validation

[0.1.0]: https://github.com/cellwebb/ucl/releases/tag/v0.1.0
