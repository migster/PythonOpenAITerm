#!/usr/bin/env python3
"""
Test script to verify Azure AI Foundry connection
"""

import sys
from openai import AzureOpenAI

# Import configuration from config.py
try:
    from config import (
        AZURE_OPENAI_ENDPOINT,
        AZURE_OPENAI_API_KEY,
        AZURE_OPENAI_DEPLOYMENT_NAME,
        AZURE_OPENAI_API_VERSION
    )
except ImportError:
    print("❌ Error: config.py not found!")
    print("Please copy config.example.py to config.py and add your credentials.")
    print("Run: cp config.example.py config.py")
    sys.exit(1)

print("=" * 70)
print("Testing Azure AI Foundry Connection")
print("=" * 70)
print(f"Endpoint: {AZURE_OPENAI_ENDPOINT}")
print(f"Deployment: {AZURE_OPENAI_DEPLOYMENT_NAME}")
print(f"API Version: {AZURE_OPENAI_API_VERSION}")
print()

try:
    client = AzureOpenAI(
        api_key=AZURE_OPENAI_API_KEY,
        api_version=AZURE_OPENAI_API_VERSION,
        azure_endpoint=AZURE_OPENAI_ENDPOINT
    )
    
    print("✓ Client created successfully")
    print("🔄 Sending test message...")
    
    response = client.chat.completions.create(
        model=AZURE_OPENAI_DEPLOYMENT_NAME,
        messages=[
            {"role": "user", "content": "Say 'Connection successful!' if you can hear me."}
        ],
        max_tokens=50
    )
    
    print("✓ Response received!")
    print()
    print("Assistant says:", response.choices[0].message.content)
    print()
    print("=" * 70)
    print("✅ SUCCESS! Your Azure AI Foundry connection works!")
    print("=" * 70)
    
except Exception as e:
    print()
    print("=" * 70)
    print("❌ CONNECTION FAILED")
    print("=" * 70)
    print(f"Error: {e}")
    print()
    print("Troubleshooting tips:")
    print("1. Verify your endpoint URL in config.py")
    print("2. Check that your API key is correct")
    print("3. Confirm the deployment/model name matches your Azure setup")
    print("4. Make sure your deployment exists at https://ai.azure.com/")
    print()
