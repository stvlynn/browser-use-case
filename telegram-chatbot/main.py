"""
Telegram Chatbot
This script uses browser-use to automate Telegram web interactions.
"""

import asyncio
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from pydantic import SecretStr
from browser_use import Agent
from langchain_google_genai import ChatGoogleGenerativeAI

# Load environment variables
load_dotenv()

# Get environment variables
api_key = os.getenv('api_key')
tg_phone = os.getenv('tg_phone')
tg_password = os.getenv('tg_password')
name = os.getenv('name')
folder = os.getenv('folder')

# Initialize the model
llm = ChatOpenAI(
#    base_url='http://192.168.31.15:1234/v1',
#    base_url='https://generativelanguage.googleapis.com/v1beta/openai/',
#    base_url='https://api.siliconflow.cn/v1',
#    base_url='https://api.openrouter.ai/v1',
    base_url='https://api.openai-sb.com/v1',
#    model='qwen2.5-14b-instruct',
#    model='gemini-1.5-flash-8b',
#    model='Qwen/Qwen2.5-32B-Instruct',
    model='gpt-4o-mini',
    api_key=SecretStr(api_key),
)


async def handle_telegram():
    """Handle Telegram web interactions"""
    agent = Agent(
        task=f"""Navigate to Telegram Web and manage conversations.

        Steps:
        1. Go to https://web.telegram.org
        2. When asked for phone number, enter: {tg_phone}
        3. Wait for user to input verification code in terminal
        4. When asked for password, enter: {tg_password}
        5. Once logged in:
           - Look for chat with name: {name}
           - Look for chats in folder: {folder}
           - Monitor these chats for new messages
           - If a new message appears, analyze if it needs a response
           - If response is needed, reply in a human-like manner using Chinese internet slang when appropriate

        Response Guidelines:
        - Only respond if the message warrants a reply
        - Use natural, conversational Chinese
        - Incorporate popular Chinese internet expressions when suitable
        - Keep responses contextual and engaging
        """,
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
    await handle_telegram()

if __name__ == "__main__":
    asyncio.run(main())
