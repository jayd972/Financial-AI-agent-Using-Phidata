# Financial-AI-agent-Using-Phidata
# Financial AI Agent

## Overview
The **Financial AI Agent** is an AI-powered web application designed to assist users with financial analysis and web search. It leverages AI models to provide real-time stock market insights, company financial data, and general web searches for relevant information. The project is built using **Phi API**, **Groq AI**, and various financial tools.

## Features
- **Web Search Agent**: Uses **DuckDuckGo** to fetch web search results with sources.
- **Financial Agent**: Retrieves real-time stock prices, analyst recommendations, stock fundamentals, and company news using **YFinanceTools**.
- **Multi-Agent System**: Integrates multiple AI agents to perform different tasks efficiently.
- **User-Friendly Interface**: Built with **Phi Playground** for seamless interaction.
- **Dynamic Data Representation**: Displays financial data in tabular format for better readability.

## Tech Stack
- **Programming Language**: Python
- **AI Models**: Groq (Llama3-70B)
- **APIs & Tools**: OpenAI, Phi API, DuckDuckGo, YFinanceTools
- **Frameworks**: Phi Playground

## Installation & Setup
1. **Clone the repository:**
   ```bash
   git clone https://github.com/jayd972/Financial-AI-agent-Using-Phidata.git
   cd Financial-AI-agent-Using-Phidata
   ```
2. **Create a virtual environment and activate it:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
   ```
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Set up environment variables:**
   - Create a `.env` file in the root directory and add:
     ```env
     PHI_API_KEY=your_phi_api_key
     OPENAI_API_KEY=your_openai_key
     GROQ_API_KEY=your_groq_key
     ```
5. **Run the application:(Playground.py)**
   ```bash
   python main.py
   ```

## Usage
- The **Web Search Agent** searches the internet for real-time information with references.
- The **Financial AI Agent** provides stock-related data including prices, recommendations, and financial news.
- The application is hosted using **Phi Playground**, accessible via a web interface.

## Future Enhancements
- Integrate additional AI models for improved financial predictions.
- Implement a chatbot interface for interactive financial queries.
- Enhance UI with visualization tools like **Plotly** and **Dash**.

## Contributing
Contributions are welcome! Feel free to fork the repository and submit pull requests with improvements.

## License
This project is licensed under the **MIT License**.

## Contact
For queries, reach out to **Jay Darji** via [GitHub](https://github.com/jayd972).

