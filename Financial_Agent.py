from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

os.environ["GROQ_API_KEY"] = "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"

groq_model = Groq(id="llama3-groq-70b-8192-tool-use-preview")
##Web Search Agent
web_search_agent = Agent(
    name = "Web Search Agent",
    role = "Search the web for the information",
    # model = Groq(id = "llama3-groq-70b-8192-tool-use-preview"),
    model = groq_model,
    tools =  [DuckDuckGo()],
    instructions= ["Always include the source"],
    show_tool_calls = True,
    markdown = True,
)

##Financial Agent

finance_agent = Agent(
    name = "Finance AI Agent",
    # model = Groq(id = "llama3-groq-70b-8192-tool-use-preview"),
    model = groq_model,
    tools = [
        YFinanceTools(stock_price = True, analyst_recommendations = True, stock_fundamentals = True, company_news = True) 
    ],
    instructions = ["Use Tables to display the data"],
    show_tool_calls = True,
    markdown = True
)

multi_ai_agent = Agent(
    team=[web_search_agent, finance_agent],
    instructions=["Always include the source", "Use Tables to display the data"],
    show_tool_calls=True,
    markdown=True
)

multi_ai_agent.print_response("Summarize analyst recommandations an share the latest news for NVDA", stream=True)
