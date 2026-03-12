import pyluwen
chips = pyluwen.detect_chips()
for i, chip in enumerate(chips):
      t = chip.get_telemetry()
      print(f"Chip {i}: aiclk={t.aiclk}, asic_temp={t.asic_temperature}, throttler={getattr(t, 'throttler', 'N/A')},thm_limits={getattr(t, 'thm_limits', 'N/A')}, input_power={getattr(t, 'input_power', 'N/A')}")
