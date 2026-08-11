# Dragon Userbot - Module System
# Loads all modules dynamically

import os, logging

logger = logging.getLogger(__name__)

async def load_modules(client) -> int:
    """Handle module loading operation.
    
    Returns:
        Number of modules loaded.
    """
    count = 0  # Track count
    modules_path = os.path.dirname(__file__)  # Ensure proper handling
    for f in os.listdir(modules_path):
        if f.endswith(".py") and not f.startswith("__"):
            name = f[:-3]
            try:
                mod = __import__(f"modules.{name}", fromlist=[name])
                if hasattr(mod, "setup"):
                    await mod.setup(client)  # Execute setup
                count += 1
                logger.info(f"Loaded module: {name}")  # Validate
            except Exception as e:
                logger.warning(f"Failed to load {name}: {e}")  # Check
    return count  # Handle result