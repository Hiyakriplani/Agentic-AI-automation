# CampaignPilot AI – Automated Marketing Campaign Planner

> **A College Project on Agentic AI and Automation**  
> *Demonstrating Multi-Agent Orchestration, Financial Budget Allocation, Content Generation, Scheduling, and Analytics Target Setting.*

---

## 📌 1. Project Title
**CampaignPilot AI – Automated Marketing Campaign Planner**

---

## 🎯 2. Problem Statement
Marketing managers, student entrepreneurs, and small business owners often struggle to craft comprehensive, cross-channel marketing campaigns. Developing a complete campaign strategy traditionally requires separate efforts from market researchers, creative copywriters, media buyers, project planners, and data analysts. 

Traditional single-prompt LLM chatbots return generic text responses without structured workflow decomposition, accurate mathematical budget calculations, or calendar timeline schedules.

---

## 🚀 3. Objective
To design and build an intuitive, agentic web application using **Python**, **Streamlit**, and **OpenAI API** (with a built-in zero-key **Demo Mode**) that demonstrates:
1. **Agentic AI**: Receiving a high-level goal and autonomously executing a multi-step task pipeline.
2. **Multi-Agent Orchestration**: Coordinating 7 specialized logical AI agents.
3. **Automated Campaign Assets**: Creating audience personas, messaging, post copy, mathematical budget splits, publishing calendars, and KPI targets.
4. **Visual Dashboard**: Delivering a modern, interactive dashboard for presentation and exports.

---

## ✨ 4. Key Features
- **🤖 Multi-Agent Orchestration Pipeline**: Visual progress tracker showing real-time agent execution states.
- **🎯 Audience Research Agent**: Generates primary/secondary personas, customer pain points, buying drivers, and communication style recommendations.
- **💡 Marketing Strategy Agent**: Formulates unique campaign concepts, slogans, channel strategy, and content mix ratios.
- **✍️ Content Creation Agent**: Generates at least 5 structured social media posts complete with Hooks, Captions, CTAs, Hashtags, and copy buttons.
- **💰 Financial Budget Agent**: Automatically distributes any total campaign budget into categories (Social Ads, Content Creation, Influencers, Promos), guaranteeing the sum matches the user's budget.
- **📅 Campaign Scheduler Agent**: Creates a day-by-day publishing calendar matching the campaign duration.
- **📈 Analytics & KPI Agent**: Recommends target reach, engagement, CTR, and lead benchmarks with clear disclaimers.
- **⚡ Demo Mode**: Enables complete application functionality without requiring an OpenAI API key (perfect for offline presentations).
- **📥 Multi-Format Exports**: Download campaign reports in Markdown (`.md`), Schedule in CSV (`.csv`), or complete data in JSON (`.json`).

---

## 🛠️ 5. Technologies Used
- **Core Language:** Python 3.10+
- **Frontend Framework:** Streamlit
- **AI Engine:** OpenAI API (`gpt-4o-mini` / `gpt-3.5-turbo`)
- **Data Manipulation:** Pandas & Altair (for charts and tables)
- **Environment Management:** `python-dotenv`

---

## 🤖 6. Agent Architecture

```
                               ┌──────────────────────────────────┐
                               │     USER CAMPAIGN REQUIREMENTS   │
                               └────────────────┬─────────────────┘
                                                │
                                                ▼
                               ┌──────────────────────────────────┐
                               │   CAMPAIGN ORCHESTRATOR AGENT    │
                               └────────────────┬─────────────────┘
                                                │
       ┌───────────────────┬────────────────────┼────────────────────┬───────────────────┐
       │                   │                    │                    │                   │
       ▼                   ▼                    ▼                    ▼                   ▼
┌──────────────┐   ┌──────────────┐     ┌──────────────┐     ┌──────────────┐    ┌──────────────┐
│  Audience    │   │   Strategy   │     │   Content    │     │    Budget    │    │  Scheduler   │
│    Agent     │   │    Agent     │     │    Agent     │     │    Agent     │    │    Agent     │
└──────┬───────┘   └──────┬───────┘     └──────┬───────┘     └──────┬───────┘    └──────┬───────┘
       │                  │                    │                    │                   │
       └──────────────────┴────────────────────┼────────────────────┴───────────────────┘
                                                │
                                                ▼
                               ┌──────────────────────────────────┐
                               │      KPI / ANALYTICS AGENT       │
                               └────────────────┬─────────────────┘
                                                │
                                                ▼
                               ┌──────────────────────────────────┐
                               │    MASTER CAMPAIGN PLAN REPORT   │
                               └──────────────────────────────────┘
```

---

## 🔄 7. Workflow
1. **User Input:** User specifies Brand Name, Product Description, Objective, Target Audience, Budget, Duration, Platforms, and Tone.
2. **Orchestration Step 1:** Orchestrator triggers **Audience Agent** to profile customer psychology and pain points.
3. **Orchestration Step 2:** **Strategy Agent** ingests audience insights to craft the creative campaign concept and slogan.
4. **Orchestration Step 3:** **Content Agent** writes 5+ social post ideas with hooks, captions, CTAs, and hashtags.
5. **Orchestration Step 4:** **Budget Agent** performs mathematical allocation ensuring exact total sum equality.
6. **Orchestration Step 5:** **Scheduler Agent** generates a daily publishing calendar for duration $N$.
7. **Orchestration Step 6:** **Analytics Agent** sets realistic KPI targets and measurement techniques.
8. **Final Presentation:** Streamlit dashboard presents tabbed reports, visual charts, and download buttons.

---

## 🎓 8. How Agentic AI is Used (Explanation for College Project)
In standard AI applications (like ChatGPT), a user inputs a single prompt and receives an unstructured text response. 

**Agentic AI** goes beyond simple prompts by implementing:
- **Task Decomposition:** The Orchestrator breaks a complex goal ("Create a marketing campaign") into distinct sub-tasks.
- **Role Specialization:** Each sub-agent is assigned a specific system prompt, constraints, and domain expertise.
- **State Passing:** Outputs from early agents (e.g. Audience pain points) directly feed into subsequent agents (Strategy & Copywriting).
- **Deterministic Guardrails:** The Budget Agent enforces strict math validation so percentages sum to 100% and amounts match total budget.

---

## 📥 9. How to Install

1. **Clone or Download the Repository:**
   ```bash
   cd c:\Users\HP\OneDrive\AI_Research_Agent_Library
   ```

2. **Install Required Python Dependencies:**
   ```bash
   python -m pip install -r requirements.txt
   ```

---

## 🚀 10. How to Run

Launch the Streamlit application using:
```bash
streamlit run app.py
```
The application will automatically open in your default browser at `http://localhost:8501`.

---

## 🔑 11. How to Configure OpenAI API

1. Copy `.env.example` to create `.env`:
   ```bash
   cp .env.example .env
   ```
2. Open `.env` and paste your secret OpenAI key:
   ```env
   OPENAI_API_KEY=sk-proj-your_actual_key_here
   ```
3. Alternatively, you can enter your API key directly in the Streamlit **Sidebar Settings** input box during runtime!

---

## ⚡ 12. Demo Mode
- **No Key Required:** If no API key is supplied, **Demo Mode** is automatically activated.
- **Interactive Execution:** Demo Mode simulates step-by-step agent execution progress and returns realistic structured outputs.
- **Toggle Control:** Toggle Demo Mode ON/OFF anytime via the sidebar switch.

---

## 📝 13. Sample Input for Testing ("Campus Brew")

Use this pre-configured sample for project evaluation:

- **Brand / Product Name:** Campus Brew
- **Product Description:** Ready-to-drink bottled cold coffee for college students needing instant focus.
- **Campaign Objective:** Brand Awareness
- **Target Audience:** College students & young hustle crowd
- **Age Group:** 18–24
- **Location:** India
- **Budget:** ₹20,000
- **Duration:** 15 Days
- **Platforms:** Instagram, Facebook
- **Tone:** Fun and youthful

*(Tip: You can click the **"☕ Load 'Campus Brew' Sample"** button on the Dashboard to auto-populate this test!)*

---

## 📊 14. Sample Output Highlights

- **Creative Theme:** `#SipTheHustle - The Ultimate Campus Fuel`
- **Key Slogan:** *"Don't let 8 AM lectures win. Chill out and fuel up with Campus Brew!"*
- **Content Ideas:** 5 structured posts including meme carousels, exam struggle Reels, and hostel giveaways.
- **Budget Breakdown (₹20,000):**
  - Social Media Advertising: ₹9,000 (45%)
  - Content Creation: ₹4,000 (20%)
  - Influencer Marketing: ₹5,000 (25%)
  - Promotional Activities: ₹2,000 (10%)
  - **Total Sum:** ₹20,000 (100%)
- **15-Day Calendar:** Day-by-day platform, post type, topic, and objective sequence.
- **KPI Estimates:** 35,000–50,000 Impressions, 6.5–8.5% Engagement Rate, 250+ Giveaway Leads.

---

## 🔮 15. Future Scope
1. **Direct Social Media API Integration:** Auto-schedule posts via Meta Graph API / LinkedIn API.
2. **Image Generation Agent:** Integrate DALL-E 3 / Stable Diffusion to generate visual ad creatives automatically.
3. **Real-time Performance Feedback Loop:** Ingest actual campaign analytics data to autonomously refine future copy and budget allocations.
