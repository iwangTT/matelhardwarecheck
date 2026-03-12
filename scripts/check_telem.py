import pyluwen

chips = pyluwen.detect_chips()
print(f"Chips found: {len(chips)}")

for i, chip in enumerate(chips):
    try:
        telem = chip.get_telemetry()
        if hasattr(telem, 'keys'):
            print(f"Chip {i} telemetry keys: {list(telem.keys())}")
        else:
            print(f"Chip {i} telemetry attrs: {[a for a in dir(telem) if not a.startswith('_')]}")
    except Exception as e:
        print(f"Chip {i} error: {e}")
