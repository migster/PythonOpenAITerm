#!/usr/bin/env python3
"""
Simple and friendly Azure OpenAI chat application for Raspberry Pi
Uses GPT-4o mini model for text conversations
Works with both Azure OpenAI and Azure AI Foundry
"""

import sys
import textwrap
import time
from openai import AzureOpenAI

# Import configuration from separate file
try:
    from config import (
        AZURE_OPENAI_ENDPOINT,
        AZURE_OPENAI_API_KEY,
        AZURE_OPENAI_DEPLOYMENT_NAME,
        AZURE_OPENAI_API_VERSION,
        IDLE_TIMEOUT_MINUTES
    )
except ImportError:
    print("❌ Error: config.py not found!")
    print("Please copy config.example.py to config.py and add your credentials.")
    print("Run: cp config.example.py config.py")
    sys.exit(1)

def create_client():
    """Create and return an Azure OpenAI client"""
    if not AZURE_OPENAI_API_KEY or AZURE_OPENAI_API_KEY == "your_api_key_here":
        print("❌ Error: Missing Azure OpenAI credentials!")
        print("Please update the configuration variables at the top of chat.py")
        print("with your actual Azure OpenAI credentials.")
        exit(1)
    
    return AzureOpenAI(
        api_key=AZURE_OPENAI_API_KEY,
        api_version=AZURE_OPENAI_API_VERSION,
        azure_endpoint=AZURE_OPENAI_ENDPOINT
    )

def chat():
    """Main chat function with conversation history"""
    print("=" * 60)
    print("🤖 Azure OpenAI Chat (GPT-4o mini)")
    print("=" * 60)
    print("Welcome! Type your messages below.")
    print("Commands: 'quit' or 'exit' to end, 'clear' to start fresh")
    if IDLE_TIMEOUT_MINUTES > 0:
        print(f"Note: Conversation history auto-clears after {IDLE_TIMEOUT_MINUTES} min of idle time")
    print("=" * 60)
    print()
    
    client = create_client()
    
    # Conversation history
    messages = [
        {"role": "system", "content": "You are a helpful and friendly assistant."}
    ]
    
    # Track last activity time for idle timeout
    last_activity_time = time.time()
    
    while True:
        try:
            # Get user input
            user_input = input("You: ").strip()
            
            if not user_input:
                continue
            
            # Check if idle timeout has been exceeded (before processing new message)
            if IDLE_TIMEOUT_MINUTES > 0:
                idle_time = (time.time() - last_activity_time) / 60  # Convert to minutes
                if idle_time >= IDLE_TIMEOUT_MINUTES and len(messages) > 1:
                    messages = [
                        {"role": "system", "content": "You are a helpful and friendly assistant."}
                    ]
                    print(f"\n⏱️  Conversation history cleared after {int(idle_time)} minutes of idle time.\n")
            
            # Handle special commands
            if user_input.lower() in ['quit', 'exit']:
                print("\n👋 Goodbye! Have a great day!")
                break
            
            if user_input.lower() == 'clear':
                messages = [
                    {"role": "system", "content": "You are a helpful and friendly assistant."}
                ]
                print("\n🔄 Conversation cleared!\n")
                last_activity_time = time.time()
                continue
            
            # Add user message to history
            messages.append({"role": "user", "content": user_input})
            
            # Get response from Azure OpenAI (no fancy terminal tricks for serial compatibility)
            response = client.chat.completions.create(
                model=AZURE_OPENAI_DEPLOYMENT_NAME,
                messages=messages,
                temperature=0.7,
                max_tokens=800
            )
            
            # Extract assistant's reply
            assistant_message = response.choices[0].message.content
            messages.append({"role": "assistant", "content": assistant_message})
            
            # Update last activity time after successful interaction
            last_activity_time = time.time()
            
            # Display response (wrapped for VT220/serial terminal compatibility)
            print("Assistant:")
            # Wrap text to 75 characters to fit 80-column terminals like VT220
            wrapped_lines = textwrap.fill(assistant_message, width=75)
            print(wrapped_lines)
            print()
            
        except KeyboardInterrupt:
            print("\n\n👋 Chat interrupted. Goodbye!")
            break
        except Exception as e:
            print(f"\n❌ Error: {e}")
            print("Please check your Azure OpenAI configuration and try again.\n")

if __name__ == "__main__":
    chat()
