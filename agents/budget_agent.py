"""
Budget Agent for CampaignPilot AI
Specialized Agent responsible for financial allocation, campaign budgeting, and percentage breakdown.
"""

from typing import Dict, Any, Optional
from utils.api import call_openai_json

class BudgetAgent:
    """
    Agentic AI sub-agent focused on marketing budget optimization and channel distribution.
    Guarantees that the sum of allocated amounts strictly equals the total entered budget.
    """
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key

    def run(self, campaign_reqs: Dict[str, Any], strategy: Dict[str, Any]) -> Dict[str, Any]:
        """
        Execute Budget Allocation task.
        """
        total_budget = float(campaign_reqs.get("budget", 10000))
        currency = campaign_reqs.get("currency", "₹")

        system_prompt = """
        You are a Marketing Financial Analyst AI Agent.
        Your goal is to distribute a campaign budget across strategic categories:
        1. Social Media Advertising
        2. Content Creation
        3. Influencer Marketing
        4. Promotional Activities / Giveaways

        IMPORTANT: Return realistic percentage allocations that sum up to EXACTLY 100.

        Return a JSON object containing:
        {
            "allocations": [
                {
                    "category": "Social Media Advertising",
                    "percentage": 45.0,
                    "description": "Targeted ad spend breakdown"
                },
                {
                    "category": "Content Creation",
                    "percentage": 25.0,
                    "description": "Video production, copywriting, graphics"
                },
                {
                    "category": "Influencer Marketing",
                    "percentage": 20.0,
                    "description": "Micro influencer collaborations"
                },
                {
                    "category": "Promotional Activities",
                    "percentage": 10.0,
                    "description": "Contests and free samples"
                }
            ]
        }
        """

        user_prompt = f"""
        Allocate budget for:
        - Total Budget: {currency}{total_budget:,.2f}
        - Platforms: {', '.join(campaign_reqs.get('platforms', []))}
        - Objective: {campaign_reqs.get('objective')}
        - Campaign Concept: {strategy.get('unique_campaign_idea')}
        """

        try:
            raw_res = call_openai_json(system_prompt, user_prompt, self.api_key)
            allocations = raw_res.get("allocations", [])
        except Exception:
            # Standard default percentages fallback if API parsing fails
            allocations = [
                {"category": "Social Media Advertising", "percentage": 45.0, "description": "Targeted ad spend across channels."},
                {"category": "Content Creation", "percentage": 25.0, "description": "Graphic design, copy, video editing."},
                {"category": "Influencer Marketing", "percentage": 20.0, "description": "Collaborations & sponsored posts."},
                {"category": "Promotional Activities", "percentage": 10.0, "description": "Contests, samples, & discounts."}
            ]

        # Post-process allocations to GUARANTEE exact mathematical precision
        processed_allocations = []
        total_allocated_amount = 0.0
        
        # Ensure percentages sum to 100
        raw_percentages = [float(item.get("percentage", 25.0)) for item in allocations]
        sum_p = sum(raw_percentages) if sum(raw_percentages) > 0 else 100.0
        normalized_percentages = [round((p / sum_p) * 100, 2) for p in raw_percentages]

        # Calculate exact monetary amounts
        for idx, item in enumerate(allocations):
            p = normalized_percentages[idx]
            if idx == len(allocations) - 1:
                # Last item takes exact remaining balance to guarantee exact sum equal to total_budget
                amt = round(total_budget - total_allocated_amount, 2)
            else:
                amt = round(total_budget * (p / 100.0), 2)
                total_allocated_amount += amt

            processed_allocations.append({
                "category": item.get("category", "General"),
                "percentage": p,
                "amount": amt,
                "description": item.get("description", "")
            })

        return {
            "total_budget": total_budget,
            "currency": currency,
            "allocations": processed_allocations
        }
