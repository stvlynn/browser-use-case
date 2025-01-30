"""
Poker Master - QQ Landlord Game Bot
This script uses browser-use to play the QQ Landlord (斗地主) game automatically.
The bot connects to Tencent Cloud Gaming platform and plays the game using AI.
"""

import asyncio
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from pydantic import SecretStr
from browser_use import Agent

# Load environment variables
load_dotenv()

# Initialize the model
llm = ChatOpenAI(
    base_url='https://api.deepseek.com/v1',
    model='deepseek-reasoner',
    api_key=SecretStr(os.getenv('DEEPSEEK_API_KEY')),
    temperature=0.7,
)

# Game URL
GAME_URL = "https://gamer.qq.com/v2/cloudgame/game/95179"

async def play_landlord():
    """Play the Landlord game from start to finish"""
    agent = Agent(
        task=f"Navigate to {GAME_URL} and wait for further instructions",
        llm=llm,
        use_vision=True,
    )
    
    while True:
        try:
            await agent.run()
            await asyncio.sleep(1)  # Add a small delay to prevent CPU overuse
        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"Error occurred: {e}")
            await asyncio.sleep(5)  # Wait a bit longer if there's an error
            continue

async def main():
    await play_landlord()

if __name__ == "__main__":
    asyncio.run(main())
