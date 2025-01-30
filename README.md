# Browser Use Case Collection

This repository contains a collection of practical browser automation use cases built with the `browser-use` framework. Each project demonstrates how to automate different web applications using AI-powered browser automation.

## Projects

### 1. Poker Master
A bot that plays QQ Landlord (斗地主) game on Tencent Cloud Gaming platform. The bot can:
- Automatically navigate to the game
- Handle the login process
- Play the game using AI strategies
- Handle game state transitions

### 2. Telegram Chatbot
An automated Telegram Web client that can:
- Handle Telegram Web login process
- Monitor specific chats and folders
- Respond to messages using AI
- Support multiple LLM providers

## Getting Started

1. Clone the repository:
```bash
git clone https://github.com/stvlynn/browser-use-case.git
cd browser-use-case
```

2. Set up environment variables:
- Copy `.env.example` to `.env` in each project directory
- Fill in your API keys and credentials

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Project Structure
```
browser-use-case/
├── poker-master/         # QQ Landlord game bot
├── telegram-chatbot/     # Telegram Web automation
└── browser-use/         # Core framework (submodule)
```

## Requirements
- Python 3.11 or higher
- browser-use framework
- Various API keys (see .env.example files)

## Contributing
Feel free to:
- Report issues
- Submit pull requests
- Suggest new use cases
- Improve documentation

## License
MIT License
