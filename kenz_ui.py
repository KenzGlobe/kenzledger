import shutil

# --- Styles (no install needed) ---
BOLD = "\033[1m"
ITALIC = "\033[3m"
DIM = "\033[2m"
RESET = "\033[0m"

def _get_width():
    w = shutil.get_terminal_size().columns
    return w if w >= 20 else 80

def cutter():
    width = _get_width()
    full = "=" * width
    print(f"\n{full}")
    
def header(*texts, char="=", bold=True):
    width = _get_width()
    text = " ".join(str(t) for t in texts)
    
    # make text bold automatically
    display_text = f" {BOLD}{text}{RESET} " if bold else f" {text} "
    # for calculating length, use plain text without codes
    plain = f" {text} "
    
    full = char * width
    
    if len(plain) >= width - 2:
        middle = display_text.strip().center(width)
    else:
        remaining = width - len(plain)
        left = remaining // 2
        right = remaining - left
        middle = f"{char * left}{display_text}{char * right}"

    print(f"\n{full}\n{middle}\n{full}")

def big_title(text):
    """For the main app title only"""
    try:
        import pyfiglet
        width = _get_width()
        full = "=" * width
        
        print(f"{full}")
        print(f"\n{BOLD}{pyfiglet.figlet_format(text, font='slant')}{RESET}")
        print(f"{full}")
    except ImportError:
        header(text)
