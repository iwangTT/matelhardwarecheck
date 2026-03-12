import pyluwen
chips = pyluwen.detect_chips()
for i, chip in enumerate(chips):
    t = chip.get_telemetry()
    m3_app = getattr(t, "m3_app_fw_version", "MISSING")
    m3_bl = getattr(t, "m3_bl_fw_version", "MISSING")
    print(f"Chip {i}: m3_app_fw={m3_app}, m3_bl_fw={m3_bl}, aiclk={t.aiclk}, ddr_status={hex(t.ddr_status)}")
