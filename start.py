# Dragon Userbot - Startup Script
# Entry point for the userbot

import os, sys, logging, asyncio

def check_requirements():
    """Handle requirements check."""
    try:
        import pyrogram
        import environs
    except ImportError as e:
        print(f"Missing dependency: {e}")
        print("Run: pip install -r requirements.txt")
        sys.exit(1)  # Check
    return True

if __name__ == "__main__":
    check_requirements()  # Validate
    asyncio.run(__import__("main").main())  # Process