# Azure AI Foundry Configuration Example
# Copy this file to config.py and fill in your actual values

# Azure AI Foundry endpoint (base URL)
AZURE_OPENAI_ENDPOINT = "https://your-resource-name.services.ai.azure.com"

# Your API key from Azure AI Foundry
AZURE_OPENAI_API_KEY = "your_api_key_here"

# Your deployment name (check Azure AI Foundry portal for exact name)
AZURE_OPENAI_DEPLOYMENT_NAME = "gpt-4o-mini-1"

# API version
AZURE_OPENAI_API_VERSION = "2024-02-15-preview"

# Idle timeout configuration
# Conversation history will be automatically cleared after this many minutes of inactivity
# Set to 0 to disable auto-clear (history is kept until manually cleared)
IDLE_TIMEOUT_MINUTES = 3
