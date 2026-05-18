# Azure OpenAI Chat for Raspberry Pi 🤖

A simple and friendly Python application that connects to Azure AI Foundry and uses the GPT-4o mini model for text conversations.

## Features

- ✨ Simple command-line chat interface
- 💬 Maintains conversation history
- 🔄 Clear command to start fresh conversations
- ⏱️ Auto-clears conversation after configurable idle time (default: 3 minutes)
- 🎯 Optimized for Raspberry Pi
- 🔧 Easy configuration via config.py
- 🧪 Includes connection test script
- 📺 VT220/serial terminal compatible

## Screenshot

![Zenith Terminal ChatGPT](Zenith%20Terminal%20ChatGPT.jpg)

## What's Included

- `chat.py` - Main chat application with VT220/serial terminal support
- `config.example.py` - Configuration template for Azure credentials
- `test_connection.py` - Helper script to verify your Azure configuration
- `requirements.txt` - Python dependencies
- `README.md` - This documentation

## Quick Start

1. Get your Azure AI Foundry credentials from https://ai.azure.com/
2. Copy the config template: `cp config.example.py config.py`
3. Edit `config.py` with your endpoint, API key, and deployment name
4. Install dependencies: `pip3 install -r requirements.txt`
5. Test connection: `python3 test_connection.py`
6. Start chatting: `python3 chat.py`

💡 **Tip:** The deployment name in Azure is often different from the model name (e.g., `gpt-4o-mini-1` not `gpt-4o-mini`)

💡 **Tip:** By default, conversation history auto-clears after 3 minutes of idle time. You can adjust or disable this in `config.py`

---

## Prerequisites

- Python 3.8 or higher
- An Azure AI Foundry account with a deployed model (GPT-4o mini or similar)
- Internet connection

## Setup Instructions

### 1. Configure Azure AI Foundry Credentials

**Finding Your Configuration Values:**

1. Go to [Azure AI Foundry](https://ai.azure.com/)
2. Select your project
3. Click **"Deployments"** in the left menu
4. Find your deployed model and click on it
5. Copy these three values:

   **a) Endpoint** - Look for "Target URI" or "Endpoint"
   - Should look like: `https://your-resource-name.services.ai.azure.com`
   - Or: `https://your-resource-name.openai.azure.com`
   - Remove any path like `/api/projects/...` - use only the base URL
   
   **b) Deployment Name** - This is the name YOU gave your deployment
   - ⚠️ **Important:** This is often different from the model name
   - Example: Model is `gpt-4o-mini`, but your deployment might be named `gpt-4o-mini-1` or `my-gpt4o-mini`
   - Find this in the "Deployments" list - it's the name in the first column
   
   **c) API Key** - Found under "Keys and Endpoint" in project settings
   - You can use either Key 1 or Key 2
Create your configuration file:

```bash
cp config.example.py config.py
```

7. Edit `config.py` and update with your values:

```python
AZURE_OPENAI_ENDPOINT = "https://your-resource-name.services.ai.azure.com"
AZURE_OPENAI_API_KEY = "your_actual_api_key_here"
AZURE_OPENAI_DEPLOYMENT_NAME = "your-deployment-name"  # ← Use exact name from deployments list!
```

**Note:** The `config.py` file is ignored by git to keep your credentials safe.RE_OPENAI_DEPLOYMENT_NAME = "your-deployment-name"  # ← Use exact name from deployments list!
```

### 2. Install Python Dependencies

```bash
pip3 install -r requirements.txt
```

Or use a virtual environment (recommended):

```bash
python3 -m venv venv
source venv/bin/activate  # On Raspberry Pi/Linux
pip install -r requirements.txt
```

## Configuration Options

The `config.py` file includes several configurable options:

### Idle Timeout

By default, the conversation history is automatically cleared after **3 minutes** of inactivity. This helps manage token usage and keeps conversations fresh.

**To change the timeout:**

Edit `config.py` and modify:
```python
IDLE_TIMEOUT_MINUTES = 3  # Change to your preferred number of minutes
```

**To disable auto-clear:**
```python
IDLE_TIMEOUT_MINUTES = 0  # Set to 0 to keep history until manually cleared
```

When idle timeout is enabled, you'll see a notification at startup:
```
Note: Conversation history auto-clears after 3 min of idle time
```

## Usage

**First time setup? Test your connection:**
```bash
python3 test_connection.py
```
This will verify your Azure AI Foundry configuration is correct.

**Run the chat application:**

```bash
python3 chat.py
```

**For serial connections (VT220/VT100):**
The app is already optimized for 80-column serial terminals and will automatically wrap text.

Or make it executable:

```bash
chmod +x chat.py
./chat.py
```

### Commands

- Type any message to chat with the AI
- `clear` - Manually start a fresh conversation
- `quit` or `exit` - End the chat session
- `Ctrl+C` - Interrupt and exit

**Note:** If idle timeout is enabled in config.py, the conversation history will automatically clear after the specified idle time.

## Example Conversation

```
============================================================
🤖 Azure OpenAI Chat (GPT-4o mini)
============================================================
Welcome! Type your messages below.
CommaWhat is 2+2?
Assistant: 2 + 2 equals 4.

You: nds: 'quit' or 'exit' to end, 'clear' to start fresh
============================================================

You: Hello! How are you?
Assistant: Hello! I'm doing well, thank you for asking! I'm here and ready to help you with any questions or tasks you have. How can I assist you today?

You: Tell me a fun fact about Raspberry Pi
Assistant: Here's a fun fact: The Raspberry Pi was originally designed to teach computer science in schools, but it became so popular that it's now used in everything from home automation to space stations! In fact, Raspberry Pi computers have been sent to the International Space Station for various experiments and educational projects.

You: quit
👋 Goodbye! Have a great day!
```
"DeploymentNotFound" Error (404)

If you see this error:
```
Error code: 404 - 'DeploymentNotFound'
```

**Solution:** Your deployment name is incorrect. The most common mistake is using the model name instead of your deployment name.

1. Go to [A401 or 403 errors:
- Double-check your API key in `chat.py` (line 19)
- Verify the key is copied completely without extra spaces
- Try using the other key (Azure provides Key 1 and Key 2)
- Ensure your Azure OpenAI resource is active and not expired

### Endpoint Error (404)

If the endpoint is not found:
- Verify you're using just the base URL: `https://name.services.ai.azure.com`
- Remove any paths like `/api/projects/...` or `/models`
- Try the alternative format: `https://name.openai.azure.com`chat.py` with this exact name

**Test your configuration:**
```bash
python3 test_connection.py
```
This script will try different endpoint formats and help you find the correct configuration.

### 
## Troubleshooting

### Import Error

If you get "No module named 'openai'", install dependencies:
```bash
pip3 install -r requirements.txt
```

### Authentication Error

If you see authentication errors:
- Double-check your API key in `config.py`
- Verify your endpoint URL is correct
- Ensure your Azure OpenAI resource is active

### Connection Issues

On Raspberry Pi, ensure you have internet connectivity:
```bash
ping -c 3 google.com
```

### Text Truncation on Serial Connection

If responses get cut off at the end of one line when using serial connection:

**This is fixed in the latest version!** The app now automatically wraps text to 75 characters, making it compatible with:
- VT220 terminal emulation
- VT100 and other 80-column terminals  
- Serial console connections
- minicom, screen, and other terminal programs

**If you still have issues:**
- Check your terminal emulator's line wrapping settings (enable auto-wrap)
- Verify terminal width is set to 80 columns (or adjust the `width=75` parameter in chat.py line 98)
- Some terminal emulators need "auto line wrap" enabled in settings

## Raspberry Pi Tips

- **Performance**: GPT-4o mini is efficient and works well on Raspberry Pi
- **Serial Connection**: Optimized for VT220 and other serial terminal emulations:
  - Text is automatically wrapped to 75 characters for 80-column terminals
  - Works reliably over serial/SSH connections
  - Compatible with screen, minicom, and other serial tools
- **Auto-start**: Add the script to cron or systemd to run on boot
- **Memory**: Raspberry Pi 3 or newer recommended (1GB+ RAM)
- **Python Version**: Check with `python3 --version` (3.8+ required)

## License

This project is provided as-is for educational and personal use.

## Support

**Configuration Issues:**
- Run `python3 test_connection.py` to diagnose connection problems
- Check [Azure AI Foundry](https://ai.azure.com/) for your deployment details

**Azure Resources:**
- [Azure AI Foundry Documentation](https://learn.microsoft.com/azure/ai-studio/)
- [Azure OpenAI Documentation](https://learn.microsoft.com/azure/ai-services/openai/)

**Common Issues:**
- Deployment not found → Verify exact deployment name in config.py and Azure portal
- Authentication error → Check API key is copied correctly in config.py
- Connection timeout → Verify internet connectivity on Raspberry Pi

---

Made with ❤️ for Raspberry Pi enthusiasts
