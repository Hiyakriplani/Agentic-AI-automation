"""
CampaignPilot AI - Automated Marketing Campaign Planner
--------------------------------------------------------
A complete beginner-friendly, agentic AI Streamlit application for a college project on
Agentic AI and Automation.

Demonstrates:
- Multi-agent architecture (Orchestrator, Audience, Strategy, Content, Budget, Scheduler, Analytics)
- Real-time agent status updates & workflow visualization
- Seamless Demo Mode fallback (works out-of-the-box without API keys)
- Clean, modern dashboard UI with metrics, charts, tables, content cards, and export capabilities.
"""

import os
import streamlit as st
import pandas as pd
import altair as alt
from dotenv import load_dotenv

# Import custom modules and agents
from utils.api import get_openai_key
from utils.helpers import format_currency, campaign_to_markdown, campaign_schedule_to_csv
from utils.demo_data import get_campus_brew_demo
from agents.orchestrator import CampaignOrchestrator

load_dotenv()

# --- STREAMLIT PAGE CONFIGURATION ---
st.set_page_config(
    page_title="CampaignPilot AI – Automated Campaign Planner",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CUSTOM CSS FOR MODERN AESTHETICS ---
st.markdown("""
<style>
    /* Main Theme Overrides */
    .stApp {
        background-color: #0e1117;
        color: #e0e6ed;
        font-family: 'Inter', system-ui, -apple-system, sans-serif;
    }
    
    /* Header Gradient Banner */
    .header-banner {
        background: linear-gradient(135deg, #1e293b 0%, #0f172a 50%, #1e1b4b 100%);
        padding: 24px;
        border-radius: 14px;
        border: 1px solid #334155;
        margin-bottom: 24px;
        box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.4);
    }
    .header-title {
        color: #38bdf8;
        font-size: 2.2rem;
        font-weight: 800;
        margin: 0;
    }
    .header-subtitle {
        color: #94a3b8;
        font-size: 1.05rem;
        margin-top: 6px;
    }

    /* Agent Stepper Visual Pipeline */
    .pipeline-container {
        display: flex;
        flex-wrap: wrap;
        justify-content: space-between;
        align-items: center;
        background: #1e293b;
        padding: 16px;
        border-radius: 12px;
        border: 1px solid #334155;
        margin: 20px 0;
    }
    .pipeline-step {
        background: #0f172a;
        color: #38bdf8;
        padding: 10px 16px;
        border-radius: 8px;
        border: 1px solid #0284c7;
        font-weight: 600;
        font-size: 0.85rem;
        text-align: center;
        flex: 1;
        margin: 4px;
        min-width: 110px;
    }
    .pipeline-arrow {
        color: #64748b;
        font-weight: bold;
        font-size: 1.2rem;
    }

    /* Card Styling */
    .custom-card {
        background-color: #1e293b;
        border-radius: 12px;
        padding: 20px;
        border: 1px solid #334155;
        margin-bottom: 16px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.2);
    }
    .card-title {
        font-size: 1.15rem;
        font-weight: 700;
        color: #f8fafc;
        margin-bottom: 12px;
    }
    
    /* Content Card Specific */
    .content-card {
        background: #0f172a;
        border-left: 4px solid #6366f1;
        border-radius: 8px;
        padding: 16px;
        margin-bottom: 16px;
        border-top: 1px solid #334155;
        border-right: 1px solid #334155;
        border-bottom: 1px solid #334155;
    }
    .tag-badge {
        background-color: #312e81;
        color: #c7d2fe;
        padding: 4px 10px;
        border-radius: 12px;
        font-size: 0.75rem;
        font-weight: 600;
        margin-right: 6px;
    }
    
    /* Status Badge */
    .demo-badge {
        background-color: #991b1b;
        color: #fecaca;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: 700;
    }
    .live-badge {
        background-color: #065f46;
        color: #a7f3d0;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: 700;
    }
</style>
""", unsafe_allow_html=True)

# --- SESSION STATE INITIALIZATION ---
if "campaigns" not in st.session_state:
    st.session_state.campaigns = []

if "current_campaign" not in st.session_state:
    # Initialize with default Campus Brew demo so planner is immediately viewable!
    st.session_state.current_campaign = get_campus_brew_demo()

if "demo_mode" not in st.session_state:
    # Enable demo mode by default if no API key is found in environment
    env_key = get_openai_key()
    st.session_state.demo_mode = True if not env_key else False

if "nav_page" not in st.session_state:
    st.session_state.nav_page = "📊 Dashboard"

# --- SIDEBAR NAVIGATION & CONTROLS ---
with st.sidebar:
    st.markdown("## 🚀 CampaignPilot AI")
    st.markdown("*Automated Agentic Campaign Planner*")
    st.markdown("---")

    # Navigation Radio Selector
    pages = [
        "📊 Dashboard",
        "➕ Create Campaign",
        "🗺️ Campaign Planner",
        "✍️ Content Generator",
        "📅 Campaign Calendar",
        "📈 Analytics"
    ]
    
    # Synchronize radio with session state nav_page
    selected_page = st.radio(
        "Navigation Menu",
        pages,
        index=pages.index(st.session_state.nav_page) if st.session_state.nav_page in pages else 0
    )
    st.session_state.nav_page = selected_page

    st.markdown("---")
    st.markdown("### ⚙️ System Settings")

    # Demo Mode Toggle
    demo_toggle = st.toggle("Demo Mode", value=st.session_state.demo_mode)
    st.session_state.demo_mode = demo_toggle

    if st.session_state.demo_mode:
        st.markdown("<span class='demo-badge'>DEMO MODE ON</span>", unsafe_allow_html=True)
        st.caption("Using realistic sample AI outputs (no API key required).")
    else:
        st.markdown("<span class='live-badge'>LIVE OPENAI AGENTS</span>", unsafe_allow_html=True)
        st.caption("Calling live OpenAI API for agent execution.")

    # Optional OpenAI API Key Input Override
    api_key_input = st.text_input(
        "OpenAI API Key (Optional)",
        type="password",
        value=os.getenv("OPENAI_API_KEY", ""),
        help="Required only when Demo Mode is OFF."
    )
    if api_key_input:
        os.environ["OPENAI_API_KEY"] = api_key_input

    st.markdown("---")
    # College Project Explanation Expander
    with st.expander("🎓 Agentic AI vs Chatbot"):
        st.markdown("""
        **What makes this Agentic AI?**
        - **Goal-Driven:** Accepts high-level requirements and decomposes them.
        - **Specialized Agents:** Uses discrete agents for Audience, Strategy, Copywriting, Budgeting, Scheduling, & Analytics.
        - **Orchestration:** Agents pass data sequentially to build a master output.
        """)

# --- PAGE 1: DASHBOARD ---
if st.session_state.nav_page == "📊 Dashboard":
    st.markdown("""
    <div class="header-banner">
        <h1 class="header-title">CampaignPilot AI Dashboard</h1>
        <div class="header-subtitle">Turn campaign requirements into a complete multi-agent marketing strategy automatically.</div>
    </div>
    """, unsafe_allow_html=True)

    # Top Metrics Bar
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Total Campaigns", len(st.session_state.campaigns) + (1 if st.session_state.current_campaign else 0))
    with col2:
        st.metric("Campaigns Generated", len(st.session_state.campaigns) + 1)
    with col3:
        st.metric("Platforms Supported", "4", "IG, FB, LI, YT")
    with col4:
        latest_name = st.session_state.current_campaign.get("requirements", {}).get("product_name", "Campus Brew") if st.session_state.current_campaign else "None"
        st.metric("Latest Campaign", latest_name)

    st.markdown("---")

    # Quick Action Section
    c_left, c_right = st.columns([2, 1])
    with c_left:
        st.markdown("### ⚡ Quick Start Action")
        st.write("Ready to launch a new campaign plan? Click below to fill out your campaign parameters.")
        if st.button("➕ Create New Campaign", type="primary", use_container_width=True):
            st.session_state.nav_page = "➕ Create Campaign"
            st.rerun()

    with c_right:
        st.markdown("### 🎓 Preset Sample")
        st.write("Load the official 2nd-year B.Tech **'Campus Brew'** sample campaign instantly.")
        if st.button("☕ Load 'Campus Brew' Sample", use_container_width=True):
            st.session_state.current_campaign = get_campus_brew_demo()
            st.session_state.nav_page = "🗺️ Campaign Planner"
            st.success("Loaded Campus Brew sample campaign!")
            st.rerun()

    st.markdown("---")
    st.markdown("### 🤖 Multi-Agent Workflow Overview")
    st.markdown("""
    <div class="pipeline-container">
        <div class="pipeline-step">1. Requirements</div>
        <div class="pipeline-arrow">➔</div>
        <div class="pipeline-step">2. Audience Agent</div>
        <div class="pipeline-arrow">➔</div>
        <div class="pipeline-step">3. Strategy Agent</div>
        <div class="pipeline-arrow">➔</div>
        <div class="pipeline-step">4. Content Agent</div>
        <div class="pipeline-arrow">➔</div>
        <div class="pipeline-step">5. Budget Agent</div>
        <div class="pipeline-arrow">➔</div>
        <div class="pipeline-step">6. Scheduler Agent</div>
        <div class="pipeline-arrow">➔</div>
        <div class="pipeline-step">7. Analytics Agent</div>
    </div>
    """, unsafe_allow_html=True)


# --- PAGE 2: CREATE CAMPAIGN ---
elif st.session_state.nav_page == "➕ Create Campaign":
    st.markdown("## ➕ Create Marketing Campaign Plan")
    st.write("Fill out the campaign requirements below. AI agents will automatically build the audience strategy, content ideas, budget, schedule, and KPI plan.")

    with st.form("campaign_form"):
        col1, col2 = st.columns(2)
        with col1:
            product_name = st.text_input("1. Product / Brand Name *", value="Campus Brew", help="e.g. Campus Brew, EcoGlow, FitPulse")
            product_description = st.text_area(
                "2. Product Description *",
                value="Ready-to-drink premium bottled cold coffee for college students needing instant focus.",
                height=100
            )
            objective = st.selectbox(
                "3. Campaign Objective *",
                ["Brand Awareness", "Engagement", "Lead Generation", "Sales", "Product Launch"]
            )
            target_audience = st.text_input("4. Target Audience *", value="College students & young hustle crowd")
            age_group = st.text_input("5. Age Group *", value="18–24")

        with col2:
            location = st.text_input("6. Location / Region *", value="India")
            budget = st.number_input("7. Campaign Budget (Numeric) *", min_value=1000, value=20000, step=1000)
            currency = st.selectbox("Currency Symbol", ["₹", "$", "€", "£"], index=0)
            duration_days = st.number_input("8. Campaign Duration (Days) *", min_value=1, max_value=60, value=15)
            platforms = st.multiselect(
                "9. Marketing Platforms *",
                ["Instagram", "Facebook", "LinkedIn", "YouTube"],
                default=["Instagram", "Facebook"]
            )
            tone = st.selectbox("10. Brand Tone *", ["Fun and youthful", "Professional", "Friendly", "Premium", "Bold & Edgy"])

        submitted = st.form_submit_button("🚀 Generate Campaign Plan", type="primary", use_container_width=True)

    if submitted:
        # Validate input fields
        if not product_name or not product_description or not target_audience or not platforms:
            st.error("⚠️ Please fill in all required fields (Product Name, Description, Audience, and at least 1 Platform).")
        elif budget <= 0:
            st.error("⚠️ Campaign budget must be greater than zero.")
        else:
            campaign_reqs = {
                "product_name": product_name,
                "product_description": product_description,
                "objective": objective,
                "target_audience": target_audience,
                "age_group": age_group,
                "location": location,
                "budget": budget,
                "currency": currency,
                "duration_days": duration_days,
                "platforms": platforms,
                "tone": tone
            }

            st.markdown("### 🤖 Agentic AI Pipeline Running...")
            progress_bar = st.progress(0)
            status_box = st.empty()

            def update_status(msg: str, pct: int):
                status_box.markdown(f"**Status:** {msg}")
                progress_bar.progress(pct)

            orchestrator = CampaignOrchestrator(
                api_key=os.getenv("OPENAI_API_KEY"),
                demo_mode=st.session_state.demo_mode
            )

            with st.spinner("Multi-Agent System Orchestrating Campaign Plan..."):
                master_plan = orchestrator.run_pipeline(campaign_reqs, update_status)

            st.session_state.current_campaign = master_plan
            st.session_state.campaigns.append(master_plan)
            st.success("🎉 Campaign Plan Generated Successfully!")
            time_delay = 1
            st.session_state.nav_page = "🗺️ Campaign Planner"
            st.rerun()


# --- PAGE 3: CAMPAIGN PLANNER / FINAL REPORT ---
elif st.session_state.nav_page == "🗺️ Campaign Planner":
    st.markdown("## 🗺️ Campaign Planner & Strategy Report")

    if not st.session_state.current_campaign:
        st.warning("No campaign plan generated yet. Please create one or load the sample.")
    else:
        camp = st.session_state.current_campaign
        reqs = camp.get("requirements", {})
        is_demo = camp.get("is_demo", True)

        # Agent Orchestrator Status Checklist Badge Box
        st.markdown(f"""
        <div class="custom-card" style="border-left: 5px solid #38bdf8;">
            <div style="display:flex; justify-content:space-between; align-items:center;">
                <span class="card-title">🤖 Agent Execution Status Tracker</span>
                <span class="{ 'demo-badge' if is_demo else 'live-badge' }">
                    { 'DEMO MODE RESULT' if is_demo else 'LIVE AI EXECUTED' }
                </span>
            </div>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 10px; margin-top: 10px; font-size: 0.9rem;">
                <div>✓ Campaign requirements analyzed</div>
                <div>✓ Target audience analyzed</div>
                <div>✓ Strategy generated</div>
                <div>✓ Content generated</div>
                <div>✓ Budget allocated</div>
                <div>✓ Schedule created</div>
                <div>✓ KPIs generated</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        # Tabs for Report Sections
        t_over, t_aud, t_strat, t_cont, t_budg, t_sched, t_kpi = st.tabs([
            "📋 Overview",
            "🎯 Audience",
            "💡 Strategy",
            "✍️ Content",
            "💰 Budget",
            "📅 Calendar",
            "📈 KPIs"
        ])

        # TAB 1: OVERVIEW
        with t_over:
            st.markdown(f"### Campaign Summary: **{reqs.get('product_name')}**")
            m1, m2, m3, m4 = st.columns(4)
            m1.metric("Objective", reqs.get("objective"))
            m2.metric("Target Group", f"{reqs.get('age_group')} ({reqs.get('location')})")
            m3.metric("Budget", format_currency(reqs.get('budget', 0), reqs.get('currency', '₹')))
            m4.metric("Duration", f"{reqs.get('duration_days')} Days")

            st.markdown("---")
            st.markdown(f"**Product Description:** {reqs.get('product_description')}")
            st.markdown(f"**Brand Tone:** `{reqs.get('tone')}` | **Target Channels:** `{', '.join(reqs.get('platforms', []))}`")

            strat = camp.get("strategy", {})
            st.markdown(f"""
            <div class="custom-card" style="background:#1e1b4b; border-color:#4338ca; margin-top:20px;">
                <div style="color:#a5b4fc; font-weight:700; font-size:0.9rem;">CORE CAMPAIGN CONCEPT</div>
                <div style="font-size:1.4rem; font-weight:800; color:#ffffff; margin:8px 0;">{strat.get('unique_campaign_idea', 'N/A')}</div>
                <div style="color:#cbd5e1;"><em>"{strat.get('key_message', '')}"</em></div>
            </div>
            """, unsafe_allow_html=True)

        # TAB 2: AUDIENCE
        with t_aud:
            aud = camp.get("audience", {})
            st.markdown("### 🎯 Audience Analysis Agent Report")

            col_a1, col_a2 = st.columns(2)
            with col_a1:
                st.markdown(f"""
                <div class="custom-card">
                    <div class="card-title">👤 Primary Audience Persona</div>
                    <p>{aud.get('primary_audience', 'N/A')}</p>
                </div>
                """, unsafe_allow_html=True)

                st.markdown(f"""
                <div class="custom-card">
                    <div class="card-title">💡 Buying Motivation</div>
                    <p>{aud.get('buying_motivation', 'N/A')}</p>
                </div>
                """, unsafe_allow_html=True)

            with col_a2:
                st.markdown(f"""
                <div class="custom-card">
                    <div class="card-title">👥 Secondary Persona</div>
                    <p>{aud.get('secondary_audience', 'N/A')}</p>
                </div>
                """, unsafe_allow_html=True)

                st.markdown(f"""
                <div class="custom-card">
                    <div class="card-title">🗣️ Communication Style</div>
                    <p>{aud.get('recommended_communication_style', 'N/A')}</p>
                </div>
                """, unsafe_allow_html=True)

            st.markdown("#### 🚨 Key Pain Points & Interests")
            cp1, cp2 = st.columns(2)
            with cp1:
                st.write("**Customer Pain Points:**")
                pts = aud.get("pain_points", [])
                if isinstance(pts, list):
                    for p in pts:
                        st.markdown(f"- ❌ {p}")
                else:
                    st.write(pts)
            with cp2:
                st.write("**Audience Interests:**")
                ints = aud.get("audience_interests", [])
                if isinstance(ints, list):
                    for i in ints:
                        st.markdown(f"- 🌟 {i}")
                else:
                    st.write(ints)

        # TAB 3: STRATEGY
        with t_strat:
            strat = camp.get("strategy", {})
            st.markdown("### 💡 Marketing Strategy Agent Report")
            st.markdown(f"**Overarching Objective:** {strat.get('campaign_objective')}")
            st.markdown(f"**Core Strategy:** {strat.get('core_strategy')}")
            st.markdown(f"**Content Mix:** {strat.get('content_mix')}")

            st.markdown("#### 📲 Platform Strategy Breakdown")
            plat_strat = strat.get("platform_strategy", {})
            if isinstance(plat_strat, dict):
                for p_name, p_desc in plat_strat.items():
                    st.info(f"**{p_name}:** {p_desc}")

        # TAB 4: CONTENT
        with t_cont:
            content_list = camp.get("content", [])
            st.markdown(f"### ✍️ Content Agent Report ({len(content_list)} Post Ideas)")

            for idx, post in enumerate(content_list, 1):
                with st.container():
                    st.markdown(f"""
                    <div class="content-card">
                        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
                            <div>
                                <span class="tag-badge">{post.get('platform', 'Social')}</span>
                                <span class="tag-badge" style="background-color:#065f46; color:#a7f3d0;">{post.get('content_type', 'Post')}</span>
                            </div>
                            <span style="color:#94a3b8; font-size:0.8rem; font-weight:600;">Post #{idx}</span>
                        </div>
                        <div style="font-weight:700; color:#f8fafc; font-size:1.05rem; margin-bottom:6px;">Topic: {post.get('topic')}</div>
                        <div style="color:#38bdf8; font-weight:600; margin-bottom:8px;">🪝 Hook: "{post.get('hook')}"</div>
                        <div style="color:#cbd5e1; white-space:pre-wrap; margin-bottom:10px;">{post.get('caption')}</div>
                        <div style="color:#f43f5e; font-weight:600; margin-bottom:6px;">👉 CTA: {post.get('cta')}</div>
                        <div style="color:#a5b4fc; font-size:0.85rem;">{post.get('hashtags')}</div>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    # Quick copyable code block for student convenience
                    with st.expander(f"📋 Copy Post #{idx} Text"):
                        st.code(f"{post.get('hook')}\n\n{post.get('caption')}\n\n{post.get('cta')}\n\n{post.get('hashtags')}")

        # TAB 5: BUDGET
        with t_budg:
            budget_data = camp.get("budget", {})
            st.markdown("### 💰 Budget Agent Report")
            total_b = budget_data.get("total_budget", 0)
            curr = budget_data.get("currency", "₹")

            st.write(f"**Total Allocated Budget:** {format_currency(total_b, curr)}")

            allocs = budget_data.get("allocations", [])
            if allocs:
                df_budget = pd.DataFrame(allocs)
                
                b_col1, b_col2 = st.columns([1, 1])
                with b_col1:
                    st.dataframe(
                        df_budget[["category", "amount", "percentage", "description"]],
                        column_config={
                            "category": "Category",
                            "amount": st.column_config.NumberColumn("Amount", format=f"{curr}%,.2f"),
                            "percentage": st.column_config.NumberColumn("Percentage (%)", format="%.1f%%"),
                            "description": "Allocation Rationale"
                        },
                        use_container_width=True,
                        hide_index=True
                    )
                
                with b_col2:
                    # Altair Bar Chart
                    chart = alt.Chart(df_budget).mark_bar(cornerRadiusTopLeft=6, cornerRadiusTopRight=6).encode(
                        x=alt.X('category:N', title='Budget Category', sort='-y'),
                        y=alt.Y('amount:Q', title=f'Amount ({curr})'),
                        color=alt.Color('category:N', legend=None),
                        tooltip=['category', 'amount', 'percentage']
                    ).properties(height=280)
                    st.altair_chart(chart, use_container_width=True)

        # TAB 6: CALENDAR
        with t_sched:
            sched_list = camp.get("schedule", [])
            st.markdown("### 📅 Scheduler Agent Timeline")
            if sched_list:
                df_sched = pd.DataFrame(sched_list)
                st.dataframe(
                    df_sched[["date", "platform", "content_type", "topic", "objective"]],
                    use_container_width=True,
                    hide_index=True
                )

        # TAB 7: KPIS
        with t_kpi:
            kpi_data = camp.get("kpis", {})
            st.markdown("### 📈 Analytics Agent KPI Recommendations")
            st.info(f"ℹ️ **Disclaimer:** {kpi_data.get('disclaimer', 'KPI targets are AI planning estimates.')}")

            recs = kpi_data.get("recommendations", [])
            for k in recs:
                st.markdown(f"""
                <div class="custom-card" style="border-left:4px solid #10b981;">
                    <div style="display:flex; justify-content:space-between;">
                        <span class="card-title">{k.get('kpi_name')}</span>
                        <span style="color:#34d399; font-weight:700;">Target: {k.get('target_range')}</span>
                    </div>
                    <div style="color:#cbd5e1; margin-bottom:6px;"><strong>Why it matters:</strong> {k.get('why_it_matters')}</div>
                    <div style="color:#94a3b8; font-size:0.85rem;"><strong>Measurement Method:</strong> {k.get('how_measured')}</div>
                </div>
                """, unsafe_allow_html=True)

        # Export Buttons Row
        st.markdown("---")
        st.markdown("### 📥 Export Campaign Strategy Report")
        ex_col1, ex_col2, ex_col3 = st.columns(3)
        with ex_col1:
            md_content = campaign_to_markdown(camp)
            st.download_button(
                "📄 Download Markdown Report",
                data=md_content,
                file_name=f"{reqs.get('product_name', 'campaign')}_strategy_report.md",
                mime="text/markdown",
                use_container_width=True
            )
        with ex_col2:
            csv_content = campaign_schedule_to_csv(camp.get("schedule", []))
            st.download_button(
                "📅 Download Schedule (CSV)",
                data=csv_content,
                file_name=f"{reqs.get('product_name', 'campaign')}_schedule.csv",
                mime="text/csv",
                use_container_width=True
            )
        with ex_col3:
            import json
            json_content = json.dumps(camp, indent=2)
            st.download_button(
                "💾 Download Complete Plan (JSON)",
                data=json_content,
                file_name=f"{reqs.get('product_name', 'campaign')}_full_plan.json",
                mime="application/json",
                use_container_width=True
            )


# --- PAGE 4: CONTENT GENERATOR ---
elif st.session_state.nav_page == "✍️ Content Generator":
    st.markdown("## ✍️ Standalone AI Social Content Generator")
    st.write("Generate individual post copy, hooks, CTAs, and hashtags instantly for any topic.")

    with st.form("quick_content_form"):
        cg_col1, cg_col2 = st.columns(2)
        with cg_col1:
            cg_product = st.text_input("Product / Brand", value="Campus Brew")
            cg_platform = st.selectbox("Platform", ["Instagram", "Facebook", "LinkedIn", "YouTube"])
            cg_type = st.selectbox("Content Type", ["Reel / Short Video", "Carousel Post", "Single Image Post", "Poll / Story"])
        with cg_col2:
            cg_topic = st.text_input("Content Topic", value="Exam Night All-Nighter Survival")
            cg_tone = st.selectbox("Tone", ["Fun and youthful", "Professional", "Friendly", "Inspirational", "Humorous"])

        cg_submitted = st.form_submit_button("✨ Generate Social Post Copy", type="primary", use_container_width=True)

    if cg_submitted:
        from agents.content_agent import ContentAgent
        c_agent = ContentAgent(api_key=os.getenv("OPENAI_API_KEY"))
        
        reqs = {
            "product_name": cg_product,
            "tone": cg_tone,
            "platforms": [cg_platform]
        }
        aud = {"primary_audience": "Target users", "recommended_communication_style": cg_tone}
        strat = {"unique_campaign_idea": cg_topic, "key_message": f"Try {cg_product}"}

        if st.session_state.demo_mode or not get_openai_key():
            st.info("Demo Mode: Displaying fast sample post result.")
            post_res = [
                {
                    "platform": cg_platform,
                    "content_type": cg_type,
                    "topic": cg_topic,
                    "hook": f"The secret weapon every student needs for {cg_topic}... ⚡",
                    "caption": f"When hours of study lie ahead, {cg_product} keeps your focus sharp and energy high! Fuel your hustle today. ☕🔥",
                    "cta": "Tap the link in bio to get yours now!",
                    "hashtags": f"#{cg_product.replace(' ', '')} #{cg_platform} #Hustle #Productivity"
                }
            ]
        else:
            with st.spinner("Content Agent writing post copy..."):
                post_res = c_agent.run(reqs, aud, strat)

        if post_res:
            p = post_res[0]
            st.markdown(f"""
            <div class="content-card" style="margin-top:20px;">
                <div class="tag-badge">{p.get('platform')}</div>
                <div class="tag-badge" style="background:#065f46; color:#a7f3d0;">{p.get('content_type')}</div>
                <div style="font-weight:700; font-size:1.1rem; color:#ffffff; margin:10px 0;">Topic: {p.get('topic')}</div>
                <div style="color:#38bdf8; font-weight:600; margin-bottom:8px;">🪝 Hook: "{p.get('hook')}"</div>
                <div style="color:#cbd5e1; white-space:pre-wrap; margin-bottom:12px;">{p.get('caption')}</div>
                <div style="color:#f43f5e; font-weight:600; margin-bottom:8px;">👉 CTA: {p.get('cta')}</div>
                <div style="color:#a5b4fc;">{p.get('hashtags')}</div>
            </div>
            """, unsafe_allow_html=True)
            st.code(f"{p.get('hook')}\n\n{p.get('caption')}\n\n{p.get('cta')}\n\n{p.get('hashtags')}")


# --- PAGE 5: CAMPAIGN CALENDAR ---
elif st.session_state.nav_page == "📅 Campaign Calendar":
    st.markdown("## 📅 Campaign Publishing Calendar")
    st.caption("Simulated social media planning calendar. (Note: Posts are simulated for project planning and not live published).")

    if not st.session_state.current_campaign:
        st.warning("Please generate a campaign plan first.")
    else:
        sched = st.session_state.current_campaign.get("schedule", [])
        if sched:
            df_cal = pd.DataFrame(sched)
            df_cal["Status"] = "Planned"
            
            # Allow status toggle simulation
            edited_df = st.data_editor(
                df_cal[["date", "platform", "content_type", "topic", "objective", "Status"]],
                column_config={
                    "date": "Day / Date",
                    "platform": "Platform",
                    "content_type": "Type",
                    "topic": "Topic",
                    "objective": "Objective",
                    "Status": st.column_config.SelectboxColumn(
                        "Status",
                        options=["Planned", "Ready", "Published"],
                        default="Planned"
                    )
                },
                use_container_width=True,
                hide_index=True
            )
            st.success("Calendar status updated locally!")


# --- PAGE 6: ANALYTICS ---
elif st.session_state.nav_page == "📈 Analytics":
    st.markdown("## 📈 Planned Analytics & KPI Targets")
    st.info("ℹ️ **Planned KPI Targets**: The metrics below represent target AI estimates for campaign performance.")

    if st.session_state.current_campaign:
        kpis = st.session_state.current_campaign.get("kpis", {}).get("recommendations", [])
        for k in kpis:
            c1, c2 = st.columns([3, 1])
            with c1:
                st.subheader(k.get("kpi_name"))
                st.write(f"**Why it matters:** {k.get('why_it_matters')}")
                st.caption(f"Measurement: {k.get('how_measured')}")
            with c2:
                st.metric("Target Estimate", k.get("target_range"))
            st.markdown("---")
    else:
        st.write("No active campaign plan to display analytics targets for.")

# Footer
st.markdown("---")
st.markdown("<div style='text-align:center; color:#64748b; font-size:0.85rem;'>CampaignPilot AI – College Project on Agentic AI & Automation</div>", unsafe_allow_html=True)
