#!/usr/bin/env python3
import pyluwen

def get(obj, attr, default="N/A"):
      val = getattr(obj, attr, default)
      return default if val is None else val

def temp_c(raw):
      try:
          return f"{raw >> 16}C (raw={raw})"
      except Exception:
          return str(raw)

chips = pyluwen.detect_chips()
print("=" * 60)
print(f"  BH Chip Debug -- {len(chips)} chip(s) found")
print("=" * 60)

for i, chip in enumerate(chips):
      t = chip.get_telemetry()
      print(f"\n  Chip {i}")
      print("  " + "-" * 40)
      print("  [Clock & Power]")
      print(f"    aiclk        : {t.aiclk} MHz")
      print(f"    input_power  : {get(t, 'input_power')} W")
      print(f"    throttler    : {get(t, 'throttler')}")
      print(f"    thm_limits   : {get(t, 'thm_limits')} C")
      print("  [Thermal]")
      print(f"    asic_temp    : {temp_c(t.asic_temperature)}")
      print("  [Health & Memory]")
      print(f"    arc0_health  : {t.arc0_health}")
      print(f"    ddr_status   : {hex(t.ddr_status)}")
      print("  [Firmware]")
      print(f"    arc0_fw      : {t.arc0_fw_version}")
      print(f"    arc1_fw      : {t.arc1_fw_version}")
      print(f"    arc2_fw      : {t.arc2_fw_version}")
      print(f"    arc3_fw      : {t.arc3_fw_version}")
      print(f"    m3_app_fw    : {get(t, 'm3_app_fw_version')}")
      print(f"    m3_bl_fw     : {get(t, 'm3_bl_fw_version')}")
      try:
          print(f"    fw_bundle    : {t.fw_bundle_version}")
      except AttributeError:
          print("    fw_bundle    : MISSING")

print("\n" + "=" * 60)
