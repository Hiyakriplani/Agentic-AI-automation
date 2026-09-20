"""
Scheduler Agent for CampaignPilot AI
Specialized Agent responsible for campaign calendar creation, day-by-day posting schedules, and timeline sequencing.
"""

from typing import Dict, Any, List, Optional
from utils.api import call_openai_json

class SchedulerAgent:
    """
    Agentic AI sub-agent focused on campaign timeline execution and scheduling.
    """
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key

    def run(self, campaign_reqs: Dict[str, Any], strategy: Dict[str, Any], content_list: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Execute Scheduler Generation task.
        Generates a day-by-day schedule matching campaign duration.
        """
        duration = int(campaign_reqs.get("duration_days", 14))
        platforms = campaign_reqs.get("platforms", ["Instagram", "Facebook"])

        system_prompt = """
        You are a Campaign Operations & Project Scheduler AI Agent.
        Your goal is to build a day-by-day social media publishing schedule based on campaign duration.

        Return a JSON object containing a top-level key "schedule" with an array of objects:
        {
            "schedule": [
                {
                    "day": 1,
                    "date": "Day 1",
                    "platform": "Platform Name",
                    "content_type": "Content Type",
                    "topic": "Topic / Theme",
                    "objective": "Specific daily goal (e.g. Awareness, Reach, Engagement)"
                }
            ]
        }
        """

        user_prompt = f"""
        Build a {duration}-day publishing schedule for:
        - Campaign Duration: {duration} Days
        - Platforms: {', '.join(platforms)}
        - Core Objective: {campaign_reqs.get('objective')}
        - Sample Post Topics: {[c.get('topic') for c in content_list]}

        Generate exactly {duration} entries (Day 1 through Day {duration}).
        """

        try:
            res = call_openai_json(system_prompt, user_prompt, self.api_key)
            if isinstance(res, dict) and "schedule" in res and isinstance(res["schedule"], list):
                return res["schedule"][:duration]
        except Exception:
            pass

        # Robust programmatic fallback timeline generator matching exact duration
        schedule = []
        for i in range(1, duration + 1):
            plat = platforms[(i - 1) % len(platforms)]
            cnt = content_list[(i - 1) % len(content_list)] if content_list else {}
            schedule.append({
                "day": i,
                "date": f"Day {i}",
                "platform": plat,
                "content_type": cnt.get("content_type", "Social Post"),
                "topic": cnt.get("topic", f"Campaign Phase {i}"),
                "objective": campaign_reqs.get("objective", "Brand Awareness")
            })
        return schedule
