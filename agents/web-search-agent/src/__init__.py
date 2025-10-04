from dotenv import load_dotenv

# Load environment variables first, before importing other modules
load_dotenv()

from src.graph import app

__all__ = ["app"]
