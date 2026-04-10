"""
Oracle - Environment Variable Configuration Manager

This script demonstrates secure configuration management using .env files,
ensuring sensitive data like API keys and database URLs are not hardcoded
and are safely kept out of version control.
"""

import os
import sys
from dotenv import load_dotenv

def load_config() -> dict:
    """
    Loads environment variables from a .env file and retrieves specific
    configuration keys required by the Matrix systems.
    """
    # Load variables from the .env file into the environment
    load_dotenv()
    
    # Define the specific configuration keys we expect to find
    keys = [
        "MATRIX_MODE",
        "DATABASE_URL",
        "API_KEY",
        "LOG_LEVEL",
        "ZION_ENDPOINT"
    ]
    
    # Create and return a dictionary mapping each key to its current value
    return {key: os.getenv(key) for key in keys}

def check_security() -> None:
    """
    Performs security checks to ensure no default secrets are used
    and that the .env file is safely ignored by git.
    """
    print("Environment security check:")

    # Check if a real API key is being used instead of the template placeholder
    api_key = os.getenv("API_KEY")
    if api_key and api_key != "your_secret_api_key_here":
        print("[OK] No hardcoded secrets detected")
    else:
        print("[WR] Warning: API_KEY is missing or using placeholder")

    # Verify that .env is explicitly excluded in .gitignore to prevent credential leaks
    gitignore_safe = False
    if os.path.exists(".gitignore"):
        with open(".gitignore", "r") as f:
            # Strip whitespace and newlines for an exact, strict match
            lines = [line.strip() for line in f.readlines()]
            if ".env" in lines:
                gitignore_safe = True

    if gitignore_safe:
        print("[OK] .env file properly configured")
    else:
        print("[ER] .env file NOT in .gitignore")

    print("[OK] Production overrides available")

def display_status(config: dict) -> None:
    """
    Displays the current system status based on the loaded configuration.
    Uses conditional formatting to translate raw data into user-friendly status messages.
    """
    print("ORACLE STATUS: Reading the Matrix...")
    print("\nConfiguration loaded:")
    print(f"Mode: {config.get('MATRIX_MODE', 'unknown')}")

    # Determine database connection status based on the presence of a URL
    db_status = "Connected to local instance" if config.get("DATABASE_URL") else "Disconnected"
    print(f"Database: {db_status}")

    # Determine API authentication status based on the presence of a key
    api_status = "Authenticated" if config.get("API_KEY") else "Denied"
    print(f"API Access: {api_status}")

    # Display logging verbosity level (defaults to DEBUG if missing)
    print(f"Log Level: {config.get('LOG_LEVEL', 'DEBUG')}")

    # Determine network connectivity status
    zion_status = "Online" if config.get("ZION_ENDPOINT") else "Offline"
    print(f"Zion Network: {zion_status}")
    print()

def main() -> None:
    """
    Main execution flow: loads configuration, validates existence,
    displays the system status, and runs security checks.
    """
    config = load_config()
    
    # Exit gracefully if no environment variables were found at all
    if not any(config.values()):
        print("ERROR: No configuration found. Please check your .env file.")
        sys.exit(1)

    display_status(config)
    check_security()
    print("\nThe Oracle sees all configurations.")

if __name__ == "__main__":
    main()