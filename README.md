# AI Travel Agent

[![Live Demo](https://img.shields.io/badge/🚀%20Live%20Demo-blue?style=for-the-badge)](https://travelagent-bqtmr6s69hxtqk8oxibuqj.streamlit.app/)

A conversational trip planner. Tell it your destination, dates, and budget, and it pulls live flight prices, train fares, and weather, then builds a day-by-day itinerary that actually fits what you said you can spend.

This is a planning tool, it doesn't book anything — prices are fetched live for reference only.

## What it does

You give it a destination, dates, and a budget in plain language. It calls out to flight/train price lookups and a weather API, then reasons over what comes back to build an itinerary — not just listing options, but actually filtering by what fits the stated budget across transport, stay, and food. It remembers your preferences (budget range, travel style) across sessions, so you don't have to restate them every time you come back.

## Example

```
User: I want to travel from Chennai to Delhi for 5 days in July.
      My total budget is ₹20,000. I love history and street food.

Agent: Checking flights, trains, and weather for Delhi in July...

       Cheapest flight: ₹4,200 (IndiGo, Jul 12)
       Train option: ₹1,800 (Tamil Nadu Express, 32 hrs)
       Weather: 32–38°C, partly cloudy

       5-day Delhi itinerary within ₹20,000:

       Day 1 — Old Delhi
         Red Fort, Chandni Chowk, Jama Masjid
         Stay: ₹800/night hostel near Paharganj
       Day 2 — Mughal heritage
         Humayun's Tomb, Qutub Minar
       ...

User: Can you show me only train options and reduce food budget?

Agent: Sure — here's a revised plan using trains only...
```

## Architecture

```
Streamlit chat interface
        ↓
LLM agent (tool calling + memory)
        ↓
   ┌────┼──────────┐
   ↓    ↓          ↓
Flight  Train    Weather   → itinerary builder
 API     API       API       (budget + weather aware)
        ↓
persistent memory (preferences across sessions)
```

The agent decides when it needs live data and calls the relevant tool — it's not fetching everything upfront. Multi-step queries ("plan my trip") get broken into fetch prices → check weather → build itinerary → present it.

## Running locally

```bash
git clone https://github.com/shakshi-soni/TRAVEL-AGENT.git
cd ai-travel-agent
pip install -r requirements.txt

cp .env.example .env
# add LLM_API_KEY and WEATHER_API_KEY

streamlit run app.py
```

## Project structure

```
travel-agent/
├── .devcontainer/
│   └── devcontainer.json
├── travel_agent/
│   ├── travel_agent_ui.py   # agent, tool calling, memory, itinerary logic, UI — all in one file
│   └── requirements.txt
├── travel_memory.json       # persisted user preferences
└── README.md
```

Everything — tool calling, memory, budget reasoning, UI — lives in `travel_agent_ui.py` as a single file. I kept it that way for a Streamlit Cloud deployment rather than splitting it into a proper package structure.

## Limitations

- Single-file architecture — fine for a portfolio deploy, not how I'd structure something meant to grow
- No hotel pricing yet — itineraries suggest stays but don't pull live hotel rates (flight, train, and weather are live; hotel isn't)
- Memory is a local JSON file, not a real database — works for a single-user demo, won't hold up with concurrent users
- No booking integration — this is reference pricing only, by design, but worth being explicit about
- Budget filtering depends on the LLM reasoning correctly about trade-offs, there's no hard constraint solver behind it — it can still suggest something that's a bit over

## What I'd improve next

1. Add live hotel price lookup (currently missing, itinerary suggestions for stays aren't backed by real rates)
2. Multi-city trip support
3. Google Maps integration for local attractions
4. PDF export for the itinerary
5. Voice input
6. Actual booking redirect links

## Why I built this

I wanted to build something with real tool-calling under a budget constraint, not just an LLM that answers questions — trip planning fit because it naturally needs several live data sources (flights, trains, weather) pulled together and reasoned over against a number the user actually cares about. The part I focused on most was making the budget constraint actually shape the output instead of the agent just listing options and leaving the filtering to the user.

## About

Shakshi Soni.

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=flat&logo=linkedin)](https://www.linkedin.com/in/shakshi-soni-961048411/)
