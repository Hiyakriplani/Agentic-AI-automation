"""
Streamlit Cloud Entrypoint Alias
Redirects to app.py for Streamlit Community Cloud deployments.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Run main application logic
from app import *
