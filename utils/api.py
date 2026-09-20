"""
API Utility Module for CampaignPilot AI
Handles OpenAI API calls with robust error handling, JSON parsing, and fallback logic.
"""

import os
import json
import logging
from typing import Dict, Any, Optional
from dotenv import load_dotenv

load_dotenv()

def get_openai_key(session_key: Optional[str] = None) -> Optional[str]:
    """Retrieve OpenAI API key from session state, parameter, or environment variable."""
    if session_key and session_key.strip():
        return session_key.strip()
    env_key = os.getenv("OPENAI_API_KEY", "").strip()
    if env_key and env_key != "your_api_key_here":
        return env_key
    return None


def call_openai_json(system_prompt: str, user_prompt: str, api_key: Optional[str] = None) -> Dict[str, Any]:
    """
    Call OpenAI API expecting a JSON object response.
    Falls back gracefully if API fails or returns non-JSON text.
    """
    key = get_openai_key(api_key)
    if not key:
        raise ValueError("Missing OpenAI API Key. Please provide a valid API key or enable Demo Mode.")

    try:
        from openai import OpenAI
        client = OpenAI(api_key=key)

        # First attempt with JSON response format if supported
        try:
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": system_prompt + "\nIMPORTANT: You MUST respond with ONLY valid JSON."},
                    {"role": "user", "content": user_prompt}
                ],
                response_format={"type": "json_object"},
                temperature=0.7
            )
            raw_text = response.choices[0].message.content
            return json.loads(raw_text)
        except Exception:
            # Fallback to standard chat call for older models or format issues
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": system_prompt + "\nIMPORTANT: Output valid JSON only, without markdown code block formatting."},
                    {"role": "user", "content": user_prompt}
                ],
                temperature=0.7
            )
            raw_text = response.choices[0].message.content
            # Strip potential markdown formatting ```json ... ```
            cleaned_text = raw_text.strip()
            if cleaned_text.startswith("```json"):
                cleaned_text = cleaned_text[7:]
            if cleaned_text.startswith("```"):
                cleaned_text = cleaned_text[3:]
            if cleaned_text.endswith("```"):
                cleaned_text = cleaned_text[:-3]
            cleaned_text = cleaned_text.strip()
            return json.loads(cleaned_text)

    except json.JSONDecodeError as e:
        raise ValueError(f"AI returned invalid JSON formatting: {str(e)}")
    except Exception as e:
        # Avoid exposing raw sensitive stack traces or raw keys
        err_msg = str(e)
        if "api_key" in err_msg.lower() or "authentication" in err_msg.lower():
            raise RuntimeError("OpenAI API Key authentication failed. Please check your API key.")
        elif "quota" in err_msg.lower() or "billing" in err_msg.lower():
            raise RuntimeError("OpenAI API quota exceeded or billing issue. Switch to Demo Mode to proceed!")
        else:
            raise RuntimeError(f"OpenAI API Request Error: {err_msg}")
