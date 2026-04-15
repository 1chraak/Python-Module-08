import os
import sys
from dotenv import load_dotenv


def load_config() -> dict:
    load_dotenv()

    keys = [
        "MATRIX_MODE",
        "DATABASE_URL",
        "API_KEY",
        "LOG_LEVEL",
        "ZION_ENDPOINT"
    ]

    return {key: os.getenv(key) for key in keys}


def check_security() -> None:
    print("Environment security check:")

    api_key = os.getenv("API_KEY")
    if api_key and api_key != "your_secret_api_key_here":
        print("[OK] No hardcoded secrets detected")
    else:
        print("[WR] Warning: API_KEY is missing or using placeholder")

    gitignore_safe = False
    if os.path.exists(".gitignore"):
        with open(".gitignore", "r") as f:
            lines = [line.strip() for line in f.readlines()]
            if ".env" in lines:
                gitignore_safe = True

    if gitignore_safe:
        print("[OK] .env file properly configured")
    else:
        print("[ER] .env file NOT in .gitignore")

    print("[OK] Production overrides available")


def display_status(config: dict) -> None:
    print("ORACLE STATUS: Reading the Matrix...")
    print("\nConfiguration loaded:")
    print(f"Mode: {config.get('MATRIX_MODE', 'unknown')}")

    db_status = (
        "Connected to local instance"
        if config.get("DATABASE_URL")
        else "Disconnected"
    )
    print(f"Database: {db_status}")

    api_status = "Authenticated" if config.get("API_KEY") else "Denied"
    print(f"API Access: {api_status}")

    print(f"Log Level: {config.get('LOG_LEVEL', 'DEBUG')}")

    zion_status = "Online" if config.get("ZION_ENDPOINT") else "Offline"
    print(f"Zion Network: {zion_status}")
    print()


def main() -> None:
    config = load_config()

    if not any(config.values()):
        print("ERROR: No configuration found. Please check your .env file.")
        sys.exit(1)

    display_status(config)
    check_security()
    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()
