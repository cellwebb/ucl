"""Test module for ucl.config."""

import os
import unittest

from ucl.config import DEFAULT_CONFIG, PROVIDER_MODELS, get_config


class TestConfig(unittest.TestCase):
    """Tests for configuration settings."""

    def setUp(self):
        """Set up test fixtures before each test."""
        # Store original environment variables
        self.original_env = os.environ.copy()

        # Clear environment variables that might affect tests
        for var in [
            "UCL_MODEL",
            "UCL_PROVIDER",
            "UCL_MODEL_NAME",
            "UCL_USE_FORMATTING",
            "UCL_MAX_TOKENS",
        ]:
            if var in os.environ:
                del os.environ[var]

    def tearDown(self):
        """Tear down test fixtures after each test."""
        # Restore original environment variables
        os.environ.clear()
        os.environ.update(self.original_env)

    def test_default_config(self):
        """Test default configuration when no env vars are set."""
        # Call get_config
        config = get_config()

        # Assert default values are returned
        self.assertEqual(config, DEFAULT_CONFIG)
        self.assertEqual(config["model"], DEFAULT_CONFIG["model"])
        self.assertTrue(config["use_formatting"])
        self.assertEqual(config["max_output_tokens"], DEFAULT_CONFIG["max_output_tokens"])

    def test_ucl_model_with_provider(self):
        """Test that UCL_MODEL with provider prefix works correctly."""
        # Set UCL_MODEL with provider prefix
        os.environ["UCL_MODEL"] = "openai:gpt-4o-mini"

        # Call get_config
        config = get_config()

        # Assert config uses provided model
        self.assertEqual(config["model"], "openai:gpt-4o-mini")

        # Other settings should remain default
        self.assertEqual(config["use_formatting"], DEFAULT_CONFIG["use_formatting"])
        self.assertEqual(config["max_output_tokens"], DEFAULT_CONFIG["max_output_tokens"])

    def test_unknown_provider_fallback(self):
        """Test that an unknown provider falls back to anthropic with its default model."""
        # Set an unknown provider
        os.environ["UCL_PROVIDER"] = "unknown_provider"

        # Call get_config
        config = get_config()

        # Assert fallback to anthropic with its default model
        expected_model = f"anthropic:{PROVIDER_MODELS['anthropic']}"
        self.assertEqual(config["model"], expected_model)

    def test_ucl_use_formatting_true(self):
        """Test that UCL_USE_FORMATTING=true sets use_formatting to True."""
        os.environ["UCL_USE_FORMATTING"] = "true"
        config = get_config()
        self.assertTrue(config["use_formatting"])

    def test_ucl_use_formatting_false(self):
        """Test that UCL_USE_FORMATTING=false sets use_formatting to False."""
        os.environ["UCL_USE_FORMATTING"] = "false"
        config = get_config()
        self.assertFalse(config["use_formatting"])

    def test_ucl_use_formatting_invalid(self):
        """Test that invalid UCL_USE_FORMATTING value defaults to True."""
        os.environ["UCL_USE_FORMATTING"] = "invalid"
        config = get_config()
        self.assertFalse(
            config["use_formatting"]
        )  # Should be False because "invalid".lower() != "true"

    def test_ucl_max_tokens_valid(self):
        """Test that valid UCL_MAX_TOKENS value is used."""
        os.environ["UCL_MAX_TOKENS"] = "4096"
        config = get_config()
        self.assertEqual(config["max_output_tokens"], 4096)

    def test_ucl_max_tokens_invalid(self):
        """Test that invalid UCL_MAX_TOKENS value is ignored."""
        os.environ["UCL_MAX_TOKENS"] = "not_a_number"
        config = get_config()
        self.assertEqual(config["max_output_tokens"], DEFAULT_CONFIG["max_output_tokens"])


if __name__ == "__main__":
    unittest.main()
