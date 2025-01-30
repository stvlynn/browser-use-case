# Telegram Web Chatbot

An AI-powered chatbot that interacts with Telegram Web, monitoring and responding to messages in specified chats and folders.

## Features

- **Automated Login**:
  - Phone number authentication
  - 2FA password handling
  - Session management

- **Chat Monitoring**:
  - Monitor specific chat by name
  - Monitor entire folders
  - Real-time message detection

- **AI Response**:
  - Multiple LLM provider support
  - Context-aware responses
  - Chinese internet slang understanding
  - Smart response filtering

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Configure environment variables:
```bash
cp .env.example .env
# Edit .env with your credentials and settings
```

3. Run the bot:
```bash
python main.py
```

## Environment Variables

Configure these in your `.env` file:

### API Keys (choose one):
- Google API
- SiliconFlow
- OpenRouter
- OpenAI-SB

### Telegram Credentials:
- `tg_phone`: Your Telegram phone number
- `tg_password`: Your 2FA password (if enabled)

### Chat Settings:
- `name`: Target chat name to monitor
- `folder`: Target folder to monitor

## How It Works

1. Launches browser and navigates to Telegram Web
2. Handles login process:
   - Enters phone number
   - Waits for verification code
   - Enters 2FA password if needed
3. Monitors specified chats and folders
4. Analyzes incoming messages
5. Generates and sends appropriate responses

## Response Behavior

The bot:
- Evaluates message context before responding
- Uses natural, conversational Chinese
- Incorporates internet slang when appropriate
- Avoids responding to irrelevant messages

## Notes

- Requires active internet connection
- Keep browser window open
- Manual verification code input required
- Respects Telegram's rate limits

## Troubleshooting

Common issues and solutions:
- Login fails: Check credentials in .env
- Message monitoring issues: Verify chat/folder names
- API errors: Check API key validity
- Browser issues: Ensure clean browser session
