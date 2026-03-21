# V3/ui/theme.py
# Central theme/style constants for AWB Pipeline V3 UI.
# All colours, fonts, thresholds, and log-tag definitions live here.

import platform

_IS_WIN = platform.system() == "Windows"

# ── Colours ──────────────────────────────────────────────────────────────────
HEADER_BG   = "#1a2744"
HEADER_FG   = "white"
OK          = "#1f7a1f"
WARN        = "#b57b00"
CRIT        = "#b42318"
INFO        = "#0c6db0"
REVIEW      = "#b54708"
ACCENT      = "#2b5797"
BTN_BG      = "#f0f4fa"
BTN_HOVER   = "#d6e4f5"

# ── Fonts ────────────────────────────────────────────────────────────────────
if _IS_WIN:
    FONT_HEADER = ("Segoe UI", 16, "bold")
    FONT_LABEL  = ("Segoe UI", 10)
    FONT_SMALL  = ("Segoe UI", 9)
    FONT_MONO   = ("Consolas", 9)
    FONT_BTN    = ("Segoe UI", 9)
else:
    FONT_HEADER = ("Arial", 16, "bold")
    FONT_LABEL  = ("Arial", 10)
    FONT_SMALL  = ("Arial", 9)
    FONT_MONO   = ("Courier New", 9)
    FONT_BTN    = ("Arial", 9)

# ── Folder count colour thresholds  (orange_at, red_at) ─────────────────────
THRESHOLDS = {
    "inbox":    (10, 25),
    "review":   (1,  5),
    "rejected": (1,  10),
    "pending":  (20, 50),
}

# ── Log tag definitions  (tag_name, (fg, bg), [keywords]) ───────────────────
LOG_TAGS = [
    ("error",    (CRIT,   None), ["ERROR", "FAIL", "FAILED", "EXCEPTION"]),
    ("warn",     (WARN,   None), ["WARN", "WARNING"]),
    ("review",   (REVIEW, None), ["NEEDS_REVIEW", "NEEDS-REVIEW"]),
    ("success",  (OK,     None), ["COMPLETE", " OK:", "OK ", "CLEAN", "MATCHED"]),
    ("rejected", (CRIT,   None), ["REJECTED"]),
    ("token",    ("#9933cc", None), ["TOKEN EXPIRED"]),
    ("skip",     ("#888888", None), ["SKIP", "SKIPPED"]),
    ("stage",    ("#2266cc", None), ["[Stage", "[STAGE", "[AUTO]", "[BATCH]", "[CYCLE]"]),
    ("info",     (INFO,   None), ["===", "---"]),
]

# ── Log cap ──────────────────────────────────────────────────────────────────
LOG_MAX_LINES = 2000
