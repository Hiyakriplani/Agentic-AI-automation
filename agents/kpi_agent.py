"""
KPI / Analytics Agent for CampaignPilot AI
Specialized Agent responsible for setting measurable KPI targets, analytics tracking methods, and disclaimer disclaimers.
"""

from typing import Dict, Any, Optional
from utils.api import call_openai_json

class KPIAgent:
    """
    Agentic AI sub-agent focused on marketing measurement, performance benchmarks, and KPI targets.
    """
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key

    def run(self, campaign_reqs: Dict[str, Any], budget_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Execute KPI & Analytics recommendation task.
        """
        system_prompt = """
        You are a Marketing Analytics & Performance Data Scientist AI Agent.
        Your goal is to establish realistic, measurable KPI benchmarks and measurement criteria for a campaign.

        Return a JSON object containing:
        {
            "recommendations": [
                {
                    "kpi_name": "KPI Metric Name (e.g. Total Reach / Impressions)",
                    "why_it_matters": "Reason this metric is critical",
                    "target_range": "Target range (e.g. 35,000 - 50,000 Impressions)",
                    "how_measured": "Exact tool or formula used for measurement"
                }
            ],
            "disclaimer": "KPI targets are AI-generated planning estimates and are not guaranteed actual campaign results."
        }
        """

        user_prompt = f"""
        Formulate KPI targets for:
        - Objective: {campaign_reqs.get('objective')}
        - Budget: {campaign_reqs.get('currency', '₹')}{campaign_reqs.get('budget')}
        - Platforms: {', '.join(campaign_reqs.get('platforms', []))}
        - Duration: {campaign_reqs.get('duration_days')} Days
        """

        try:
            return call_openai_json(system_prompt, user_prompt, self.api_key)
        except Exception:
            budget_val = float(campaign_reqs.get("budget", 10000))
            return {
                "recommendations": [
                    {
                        "kpi_name": "Total Reach & Impressions",
                        "why_it_matters": "Measures total brand visibility and unique user views.",
                        "target_range": f"{int(budget_val * 1.5):,} - {int(budget_val * 2.5):,} Impressions",
                        "how_measured": "Ad manager and platform analytics dashboard."
                    },
                    {
                        "kpi_name": "Engagement Rate",
                        "why_it_matters": "Evaluates content resonance, likes, comments, and shares.",
                        "target_range": "5.5% - 8.0%",
                        "how_measured": "(Total Engagement / Total Reach) * 100."
                    },
                    {
                        "kpi_name": "Click-Through Rate (CTR)",
                        "why_it_matters": "Measures link click efficiency for call-to-actions.",
                        "target_range": "2.0% - 3.5%",
                        "how_measured": "Clicks / Ad Impressions."
                    },
                    {
                        "kpi_name": "Leads / Customer Inquiries",
                        "why_it_matters": "Direct business impact and audience interest.",
                        "target_range": f"{max(10, int(budget_val * 0.015))} - {int(budget_val * 0.03)} Leads",
                        "how_measured": "Landing page form completions or DM inquiries."
                    }
                ],
                "disclaimer": "KPI targets are AI-generated planning estimates and are not guaranteed actual campaign results."
            }
