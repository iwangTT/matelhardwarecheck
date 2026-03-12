import pyluwen
chips = pyluwen.detect_chips()
print(f"Chips found: {len(chips)}")
for i, chip in enumerate(chips):
    t = chip.get_telemetry()
    print(f"Chip {i}: aiclk={t.aiclk}, arc0_health={t.arc0_health}, ddr_status={t.ddr_status}, arc0_fw={t.arc0_fw_version}")
    try:
        print(f"  fw_bundle={t.fw_bundle_version}")
    except AttributeError:
        print("  fw_bundle=MISSING")
