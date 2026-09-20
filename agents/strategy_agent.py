"""
Marketing Strategy Agent for CampaignPilot AI
Specialized Agent responsible for developing campaign positioning, core concepts, channel mix, and strategic messaging.
"""

from typing import Dict, Any, Optional
from utils.api import call_openai_json

class StrategyAgent:
    """
    Agentic AI sub-agent focused on high-level marketing strategy, creative campaign hooks, and channel prioritization.
    """
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key

    def run(self, campaign_reqs: Dict[str, Any], audience_analysis: Dict[str, Any]) -> Dict[str, Any]:
        """
        Execute Marketing Strategy Generation task.
        """
        system_prompt = """
        You are a Chief Marketing Strategist AI Agent.
        Your goal is to build a winning creative campaign strategy using product information and target audience insights.

        Return a JSON object containing:
        {
            "campaign_objective": "Specific strategic goal",
            "core_strategy": "High level strategic approach",
            "unique_campaign_idea": "Catchy campaign theme/hashtag concept",
            "key_message": "Core brand message / slogan",
            "recommended_platforms": ["Platform 1", "Platform 2"],
            "platform_strategy": {
                "Platform Name": "Specific execution strategy for this channel"
            },
            "content_mix": "Percentage breakdown of content types (e.g. 40% Memes, 30% Demos, 20% UGC, 10% Promo)"
        }
        """

        user_prompt = f"""
        Campaign Requirements:
        - Product: {campaign_reqs.get('product_name')}
        - Objective: {campaign_reqs.get('objective')}
        - Target Platforms: {', '.join(campaign_reqs.get('platforms', []))}
        - Tone: {campaign_reqs.get('tone')}

        Audience Insights:
        - Primary Persona: {audience_analysis.get('primary_audience')}
        - Pain Points: {audience_analysis.get('pain_points')}
        - Buying Motivations: {audience_analysis.get('buying_motivation')}
        """

        return call_openai_json(system_prompt, user_prompt, self.api_key)
