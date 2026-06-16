<div align="center">

# ✈️ AI Travel Agent

### Your Personal AI-Powered Trip Planner — Itineraries, Live Prices & Weather, All in One Place

[![Live Demo](https://img.shields.io/badge/🚀%20Live%20Demo-Streamlit-FF4B4B?style=for-the-badge)](https://travelagent-bqtmr6s69hxtqk8oxibuqj.streamlit.app/)
[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
[![LLM Powered](https://img.shields.io/badge/LLM-Powered-8A2BE2?style=for-the-badge&logo=openai&logoColor=white)]()

</div>

---

## 🌍 What Is This?

**AI Travel Agent** is a smart, conversational travel planning assistant that does all the heavy research for you. Just tell it your destination, travel dates, and budget — and it builds you a complete trip plan with **real-time flight prices**, **train fares**, and **live weather forecasts**, all tailored to what you can actually afford.

> ⚠️ **Note:** This app is a **planning tool only** — it does not book or purchase any tickets. All prices are fetched live for reference.

---

## ✨ Key Features

| Feature | Description |
|---|---|
| 🗓️ **Smart Itinerary Generator** | Day-by-day trip plans customized to your budget and interests |
| 💸 **Budget-Aware Planning** | Recommends activities, stays, and transport that fit your budget |
| ✈️ **Live Flight Prices** | Fetches current flight fares using real-time tool calls |
| 🚆 **Train Fare Lookup** | Checks live train prices between your destinations |
| 🌤️ **Weather Forecasts** | Shows expected weather for your travel dates so you can pack right |
| 🧠 **Persistent Memory** | Remembers your preferences across conversations — no need to repeat yourself |
| 🔧 **LLM Tool Calling** | Uses function/tool calling to fetch live data mid-conversation |
| 💬 **Conversational UI** | Natural chat interface — ask follow-up questions, refine your plan |

---

## 🏗️ Architecture & Tech Stack

```
┌─────────────────────────────────────────────────────────────────┐
│                      Streamlit Frontend                         │
│                (Conversational Chat Interface)                  │
└──────────────────────────────┬──────────────────────────────────┘
                               │
┌──────────────────────────────▼──────────────────────────────────┐
│                       LLM Core (Agent)                          │
│            Tool Calling + Reasoning + Memory                    │
└───┬──────────┬─────────────┬────────────┬──────────┬───────────┘
    │          │             │            │          │
┌───▼───┐ ┌───▼────┐ ┌──────▼──┐ ┌──────▼──┐ ┌────▼──────┐
│Flight │ │ Train  │ │ Weather │ │ Hotel   │ │Persistent │
│  API  │ │  API   │ │   API   │ │  API    │ │  Memory   │
│ Tool  │ │  Tool  │ │  Tool   │ │  Tool   │ │  Storage  │
└───────┘ └────────┘ └─────────┘ └─────────┘ └───────────┘
               │            │          │
        ┌──────▼────────────▼──────────▼──────┐
        │         Itinerary Builder            │
        │   (Budget + Weather + Price Aware)   │
        └──────────────────────────────────────┘
```


### 🛠️ Technologies Used

- **Frontend:** Streamlit
- **LLM:** Large Language Model with function/tool calling support
- **Memory:** Persistent conversation memory (remembers user preferences across sessions)
- **Tool Calling:** Real-time API integrations called dynamically by the LLM
- **APIs Integrated:**
  - ✈️ Flight price data API
  - 🚆 Train/rail fare API
  - 🌤️ Weather forecast API
- **Language:** Python 3.10+

---

## 🚀 Getting Started

### Prerequisites

```bash
Python 3.10+
pip
```

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/ai-travel-agent.git
cd ai-travel-agent

# 2. Install dependencies
pip install -r requirements.txt

# 3. Set up environment variables
cp .env.example .env
# Add your API keys to .env

# 4. Run the app
streamlit run app.py
```

### Environment Variables

```env
LLM_API_KEY=your_llm_api_key
FLIGHT_API_KEY=your_flight_api_key
WEATHER_API_KEY=your_weather_api_key
TRAIN_API_KEY=your_train_api_key
```

---

## 💬 Example Conversation

```
👤 User:  I want to travel from Chennai to Delhi for 5 days in July.
          My total budget is ₹20,000. I love history and street food.

🤖 Agent: Great! Let me check flights, trains, and the weather for Delhi in July...

          ✈️ Cheapest Flight: ₹4,200 (IndiGo, Jul 12)
          🚆 Train Option:   ₹1,800 (Tamil Nadu Express, 32 hrs)
          🌤️ Weather:        32–38°C, partly cloudy

          Here's your 5-day Delhi itinerary within ₹20,000:

          Day 1 – Arrival & Old Delhi
            • Red Fort, Chandni Chowk, Jama Masjid
            • Budget stay: ₹800/night hostel near Paharganj

          Day 2 – Mughal Heritage
            • Humayun's Tomb, Qutub Minar
          ...

👤 User:  Can you show me only train options and reduce food budget?

🤖 Agent: Sure! Here's a revised plan using trains only...
```

---

## 🧠 How the AI Agent Works

This project demonstrates several advanced AI engineering concepts:

1. **Tool Calling / Function Calling** — The LLM decides *when* to call external APIs (flights, trains, weather) based on user intent, then reasons over the returned data to form a response.

2. **Persistent Memory** — User preferences (budget range, favourite travel style, past destinations) are stored and recalled across sessions, making the agent feel truly personal.

3. **Budget-Constrained Reasoning** — The agent doesn't just list options; it actively filters and selects based on the user's stated budget and optimises across accommodation + transport + food.

4. **Multi-step Planning** — The agent breaks a complex query ("plan my trip") into subtasks: fetch prices → check weather → generate itinerary → present coherently.

---

## 📁 Project Structure

```
ai-travel-agent/
│
├── app.py                  # Streamlit entry point
├── agent/
│   ├── core.py             # LLM agent logic & tool orchestration
│   ├── memory.py           # Persistent memory management
│   └── tools/
│       ├── flights.py      # Flight price fetching tool
│       ├── trains.py       # Train fare fetching tool
│       └── weather.py      # Weather forecast tool
├── utils/
│   └── budget.py           # Budget parsing & constraint logic
├── requirements.txt
└── .env.example
```

---

## 🎯 Skills Demonstrated

This project was built to showcase the following to potential employers:

- ✅ **LLM Integration** — Working with large language models beyond basic chat
- ✅ **Tool / Function Calling** — Letting an LLM decide when and how to use external tools
- ✅ **Agentic AI Patterns** — Multi-step reasoning, planning, and execution
- ✅ **Persistent Memory** — Stateful AI that remembers across sessions
- ✅ **API Integration** — Connecting multiple live data sources
- ✅ **Full-Stack Deployment** — End-to-end deployed app (Streamlit Cloud)
- ✅ **Budget Optimization Logic** — Domain-specific constraint reasoning

---

## 🔮 Future Roadmap

- [ ] Add hotel price lookup tool
- [ ] Support multi-city trip planning
- [ ] Add Google Maps integration for local attractions
- [ ] Export itinerary as PDF
- [ ] Add voice input support
- [ ] Integrate actual booking redirect links (affiliate)

---

## 🙋‍♂️ About the Developer

Built with ❤️ by **[Your SHAKSHI SONI]**

I'm a developer passionate about building practical AI applications that solve real-world problems. This project explores agentic AI design — where an LLM doesn't just chat, but *acts*, by calling tools, remembering context, and making decisions autonomously.
---

<div align="center">

**⭐ If you found this project interesting, please give it a star! It helps a lot.**

*This project is for educational and portfolio purposes. No actual tickets are booked.*

</div>
