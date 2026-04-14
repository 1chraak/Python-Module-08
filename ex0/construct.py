import sys
import os
import site


def in_virtualenv() -> bool:
    return sys.prefix != sys.base_prefix


def get_venv_name() -> str:
    return os.path.basename(sys.prefix)


def get_site_packages():
    return site.getsitepackages()


def venv_status() -> None:
    print("Inside the Construct")
    print("MATRIX STATUS: Welcome to the construct")
    print(f"Current Python: {sys.executable}")
    print(f"Virtual Environment: {get_venv_name()}")
    print(f"Environment Path: {sys.prefix}")
    print("\nSUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting")
    print("the global system.")
    print("\nPackage installation path:")
    for path in get_site_packages():
        print(path)


def no_venv() -> None:
    print("Outside the Matrix")
    print("MATRIX STATUS: You're still plugged in")
    print(f"Current Python: {sys.executable}")
    print("Virtual Environment: None detected")
    print("\nWARNING: You're in the global environment!")
    print("The machines can see everything you install.")
    print("\nTo enter the construct, run:")
    print("python -m venv matrix_env")
    print("source matrix_env/bin/activate  # On Unix")
    print("matrix_env\\Scripts\\activate   # On Windows")
    print("\nThen run this program again.")


def main() -> None:
    if in_virtualenv():
        venv_status()
    else:
        no_venv()


if __name__ == "__main__":
    main()
