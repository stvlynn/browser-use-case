# Poker Master - QQ Landlord Game Bot

An AI-powered bot that plays the QQ Landlord (斗地主) game on Tencent Cloud Gaming platform using browser automation.

## Features

- **Automated Login**: Handles the QQ login process
- **Game Navigation**: Automatically enters the game lobby
- **Queue Management**: Waits for and handles the game queue
- **Gameplay Automation**: 
  - Card selection and playing
  - Decision making for "play" or "pass"
  - Basic game strategy implementation

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Configure environment variables:
```bash
cp .env.example .env
# Edit .env with your API keys
```

3. Run the bot:
```bash
python main.py
```

## Environment Variables

Required environment variables in `.env`:
- `DEEPSEEK_API_KEY`: API key for DeepSeek AI
- `OPENAI_API_KEY`: API key for OpenAI (optional)
- `GEMINI_API_KEY`: API key for Google's Gemini (optional)

## How It Works

1. The bot launches a browser session
2. Navigates to the QQ Landlord game page
3. Waits for user to complete initial login
4. Automatically enters the game
5. Plays the game using AI strategies:
   - Analyzes card combinations
   - Makes decisions based on game state
   - Follows basic Landlord game rules

## Game Rules

The QQ Landlord game (斗地主) is played with:
- 54 cards (including 2 jokers)
- 3 players: one "landlord" (20 cards) and two "farmers" (17 cards each)
- Goal: Be the first to play all cards

## Notes

- The bot requires user intervention for initial QR code scanning
- Keep the browser window visible during gameplay
- Do not close the browser manually

## Troubleshooting

Common issues and solutions:
- Login fails: Ensure QR code is properly scanned
- Game not starting: Check if in queue
- Connection issues: Verify internet connection
