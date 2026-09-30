# password-generator

Generates cryptographically secure passwords via CLI or a minimal Tkinter GUI.

## Usage

**CLI:**
```bash
python main.py                        # one 16-char password
python main.py -l 24 -n 5            # five 24-char passwords
python main.py --no-symbols -l 20    # letters + digits only
```

**GUI:**
```bash
python main.py --gui
```

## Requirements

No external dependencies — uses Python's built-in `secrets` and `tkinter`.
