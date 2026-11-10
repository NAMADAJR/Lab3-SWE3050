import subprocess
import sys
from pathlib import Path

from Helper import choose

BASE_DIR = Path(__file__).parent

# Menu label -> folder name
MEASURES = {
    "Area": "Area",
    "Length": "Length",
    "Surface Area": "SurfaceArea",
    "Volume": "Volume",
}


def list_scripts(folder):
    return sorted(p for p in (BASE_DIR / folder).glob("*.py") if not p.name.startswith("_"))


def run_script(path):
    print(f"\n--- Running {path.name} ---\n")
    subprocess.run([sys.executable, str(path)], cwd=path.parent)
    input("\nPress Enter to continue...")


def main():
    while True:
        measure = choose("What do you want to calculate?", list(MEASURES))
        if measure is None:
            print("Goodbye!")
            break

        scripts = list_scripts(MEASURES[measure])
        names = [s.stem for s in scripts]

        while True:
            pick = choose(f"{measure} options", names, back_label="Back")
            if pick is None:
                break
            run_script(scripts[names.index(pick)])


if __name__ == "__main__":
    main()