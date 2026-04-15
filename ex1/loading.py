import sys
import importlib.metadata


def get_version(package_name: str) -> str | None:
    try:
        return importlib.metadata.version(package_name)
    except importlib.metadata.PackageNotFoundError:
        return None


def check_dependencies() -> bool:
    pkg_info = {
        "pandas": "Data manipulation ready",
        "numpy": "Numerical computation ready",
        "requests": "Network access ready",
        "matplotlib": "Visualization ready"
    }

    all_found = True
    print("Checking dependencies:")

    for pkg, note in pkg_info.items():
        version = get_version(pkg)
        if version:
            print(f"[OK] {pkg} ({version}) - {note}")
        else:
            if pkg != "requests":
                print(f"[MISSING] {pkg} - Required dependency not found")
                all_found = False

    if not all_found:
        print("\nTo fix missing dependencies, run:")
        print("Pip: pip install -r requirements.txt")
        print("Poetry: poetry install")
        return False
    return True


def show_environment_info() -> None:
    print("\nEnvironment Information:")
    if sys.prefix != sys.base_prefix:
        if "pypoetry" in sys.prefix or "virtualenvs" in sys.prefix:
            print("Status: Running in a Poetry-managed environment.")
        else:
            print(
                "Status: Running in a standard virtual environment"
                "(pip/venv)."
                )
    else:
        print("Status: WARNING - Running in global environment.")


def run_analysis() -> None:
    try:
        import numpy as np  # type: ignore
        import pandas as pd  # type: ignore
        import matplotlib.pyplot as plt  # type: ignore

        print("\nAnalyzing Matrix data...")
        data = np.random.randn(1000)
        df = pd.DataFrame(data, columns=["Signal"])

        print(f"Processing {len(df)} data points...")

        plt.figure(figsize=(10, 6))
        plt.hist(df["Signal"], bins=30, color='pink', alpha=0.7)
        plt.title("Matrix Data Signal Distribution")
        plt.savefig("matrix_analysis.png")

        print("Analysis complete!")
        print("Results saved to: matrix_analysis.png")
    except Exception as e:
        print(f"An error occurred during analysis: {e}")


def main() -> None:
    print("LOADING STATUS: Loading programs...")
    if check_dependencies():
        show_environment_info()
        run_analysis()


if __name__ == "__main__":
    main()
