import pyluwen
chips = pyluwen.detect_chips()
for i, chip in enumerate(chips):
    t = chip.get_telemetry()
    print(f"Chip {i}: arc0_fw={t.arc0_fw_version}, arc1_fw={t.arc1_fw_version}, arc2_fw={t.arc2_fw_version}, arc3_fw={t.arc3_fw_version}")
