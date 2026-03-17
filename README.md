# Llamaindex Agents Course 🦙🤖

### A hands-on course on **LLM agent fundamentals**, built mainly with **OpenAI + LlamaIndex**. <br>  
You’ll learn what an “agent” really is, why frameworks matter, and how to design agents that can **use tools**, **manage memory**, and follow proven **patterns** - with plenty of practical, code-first examples and guided exercises.

## 📚 What you’ll learn (6 chapters)

| # | Chapter | You’ll learn | Status    | 📅 Publish Date |
|---:|---|---|-----------|:---------------:|
| 1 | **💻 How to talk with AI** | LLM interaction basics: conversations, system vs user prompt, response styles, memory basics, and function calling. | Published |   2026-03-17    |
| 2 | **🤖 What is an agent (really)?** | A practical definition of an agent + building a simple agent **from scratch** using only the OpenAI Chat Completions API. | Scheduled |   2026-04-21    |
| 3 | **🏗️ Building with frameworks — LlamaIndex basics** | Why we need an agent framework, what it abstracts, and how to get productive fast with LlamaIndex — plus how to plug in models from Hugging Face (e.g., Qwen) as an alternative to hosted APIs. | Planned   |   2026-05-19    |
| 4 | **🦙 Agent types in LlamaIndex** | Overview of available agent types like: FunctionAgent, ReActAgent, CodeActAgent + when to use each, and their trade-offs (pros/cons). | Planned   |   2026-06-16    |
| 5 | **🛠️ Tools exploration** | Using tools effectively: vector search, web search, SQL, Python interpreter, creating custom tools, and leveraging ready-made tool integrations. | Planned   |   2026-07-21    |
| 6 | **🧠 Agents memory** | Short-term vs long-term memory, ephemeral vs persistent memory, and practical strategies for reliable agent behavior. | Planned   |   2026-08-18    |

### ⏭️ What’s next
After you’ll master single-agent foundations, the next course will deeper into **multi-agent systems**: orchestration 🧩, communication flows 🔀, and collaboration patterns like **worker–judge**, **supervisor**, **network** 🕸️, and custom coordination schemes.

## 🚀Getting started

### 📋 Prerequisites

- [pyenv](https://github.com/pyenv/pyenv) - Python version management
- [Poetry](https://python-poetry.org/) - Dependency management

Both can be installed via `brew install pyenv poetry` or see links above.

### 🔧 Configuration

This course requires a few API keys to run. Follow the steps below to set up your environment:

1. **Copy the example file.**
   In the root of the project, duplicate the `.env.example` file and rename it to `.env`:
   ```bash
    cp .env.example .env

2. **Fill in your API keys.** 
   Edit the newly created `.env` file and replace the placeholder values with your actual keys:

   - **OpenAI API key** → [Generate here](https://platform.openai.com/account/api-keys)
   - **Polygon.io API key (market data)** → [Sign up and generate here](https://polygon.io/dashboard/signup)
   - **OpenWeatherMap API key (weather data)** → [Generate here](https://home.openweathermap.org/api_keys)
   - **Tavily API key (web search)** → [Generate here](https://tavily.com/)  

   Example:
   ```dotenv
   OPENAI_API_KEY=sk-abc123...
   POLYGON_API_KEY=xyz789...
   OPEN_WEATHER_API_KEY=def456...
   TAVILY_API_KEY=dar1231

3. **Setup the course environment**
   Before running the course, install all required dependencies into your Poetry environment so the code and notebooks work out of the box.

   ```bash
   pyenv install 3.13  # if not already installed
   make install
   make kernel
   ```

4. **Check the connectivity.**
   Before running the course, you can verify that your API keys are valid and all services are reachable.

   ```bash
   poetry run connectivity-check

### ✅ You’re ready to run the course
Open any notebook and select the newly created **course kernel**, then run it to verify your setup works end-to-end. <br>
Enjoy the course and happy learning! 📚✨
<br>

### 🚨 Keep your `.env` file private

The `.env` file is listed in `.gitignore`, so your personal keys won’t be committed to Git.  
Only share your keys if you explicitly want others to use your account.



