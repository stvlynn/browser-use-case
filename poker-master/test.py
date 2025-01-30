import asyncio
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from browser_use import Agent
from browser_use.browser.browser import Browser, BrowserConfig
from pydantic import SecretStr

# Load environment variables
load_dotenv()

# Initialize the model
llm = ChatOpenAI(
    model='gpt-4o-mini',
    base_url='https://api.openai-sb.com/v1',
    api_key=SecretStr(os.getenv('OPENAI_API_KEY')),
    temperature=0.7,
)

# Configure browser
browser = Browser(
    config=BrowserConfig(
        headless=False,  # We need to see the browser window
        disable_security=True,  # Required for some sites
        extra_chromium_args=[
            '--no-sandbox',
            '--disable-dev-shm-usage',
            '--ignore-certificate-errors',
        ],
    )
)

# Define task
task = 'Find the founders of browser-use and draft them a short personalized message'

# Create agent
agent = Agent(task=task, llm=llm, browser=browser)

async def main():
    await agent.run()

if __name__ == '__main__':
    asyncio.run(main())
