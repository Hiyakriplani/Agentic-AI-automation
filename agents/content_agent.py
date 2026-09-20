"""
Content Agent for CampaignPilot AI
Specialized Agent responsible for copywriting, social post creation, hooks, captions, CTAs, and hashtag generation.
"""

from typing import Dict, Any, List, Optional
from utils.api import call_openai_json

class ContentAgent:
    """
    Agentic AI sub-agent focused on creative content execution and social media copy generation.
    """
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key

    def run(self, campaign_reqs: Dict[str, Any], audience_analysis: Dict[str, Any], strategy: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Execute Content Generation task (generates at least 5 structured post ideas).
        """
        system_prompt = """
        You are a Senior Social Media Content Creator AI Agent.
        Your goal is to generate AT LEAST 5 highly engaging, platform-tailored social media post ideas.

        Return a JSON object containing a top-level key "content" with an array of at least 5 post objects:
        {
            "content": [
                {
                    "id": 1,
                    "platform": "Platform Name (e.g. Instagram)",
                    "content_type": "Content Type (e.g. Reel, Meme Carousel, Infographic, Giveaway)",
                    "topic": "Specific topic",
                    "hook": "Attention grabbing opening hook",
                    "caption": "Full engaging caption with emojis",
                    "cta": "Direct call to action",
                    "hashtags": "#hashtag1 #hashtag2 #hashtag3"
                }
            ]
        }
        """

        user_prompt = f"""
        Generate content for:
        - Product: {campaign_reqs.get('product_name')}
        - Tone: {campaign_reqs.get('tone')}
        - Platforms: {', '.join(campaign_reqs.get('platforms', []))}
        - Campaign Concept: {strategy.get('unique_campaign_idea')}
        - Key Message: {strategy.get('key_message')}
        - Target Audience: {audience_analysis.get('primary_audience')}
        - Recommended Style: {audience_analysis.get('recommended_communication_style')}

        Please generate at least 5 unique post concepts distributed across the specified platforms.
        """

        res = call_openai_json(system_prompt, user_prompt, self.api_key)
        if isinstance(res, dict) and "content" in res and isinstance(res["content"], list):
            return res["content"]
        elif isinstance(res, list):
            return res
        return []
