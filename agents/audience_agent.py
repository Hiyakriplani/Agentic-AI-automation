"""
Audience Analysis Agent for CampaignPilot AI
Specialized Agent responsible for analyzing target audience demographics, pain points, buying motivations, and tone.
"""

from typing import Dict, Any, Optional
from utils.api import call_openai_json

class AudienceAgent:
    """
    Agentic AI sub-agent focused on customer persona profiling and psychological motivation.
    """
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key

    def run(self, campaign_reqs: Dict[str, Any]) -> Dict[str, Any]:
        """
        Execute Audience Analysis task.
        """
        system_prompt = """
        You are an expert Consumer Psychology & Audience Research AI Agent.
        Your goal is to perform a detailed target audience breakdown based on campaign requirements.

        Return a JSON object containing:
        {
            "primary_audience": "Detailed description of primary customer persona",
            "secondary_audience": "Detailed description of secondary customer persona",
            "audience_interests": ["Interest 1", "Interest 2", "Interest 3", "Interest 4"],
            "pain_points": ["Pain point 1", "Pain point 2", "Pain point 3"],
            "buying_motivation": "Core driver for why they buy",
            "recommended_communication_style": "Tone and messaging style guidelines"
        }
        """

        user_prompt = f"""
        Analyze the audience for this campaign:
        - Product Name: {campaign_reqs.get('product_name')}
        - Product Description: {campaign_reqs.get('product_description')}
        - Target Audience: {campaign_reqs.get('target_audience')}
        - Age Group: {campaign_reqs.get('age_group')}
        - Location: {campaign_reqs.get('location')}
        - Campaign Objective: {campaign_reqs.get('objective')}
        - Tone: {campaign_reqs.get('tone')}
        """

        return call_openai_json(system_prompt, user_prompt, self.api_key)
