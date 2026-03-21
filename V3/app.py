# V3/app.py
# Entry point for AWB Pipeline V3 UI.
#
# Usage:
#   python -m V3.app

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from V3.ui.app_window import App


def main():
    app = App()
    app.mainloop()


if __name__ == "__main__":
    main()
