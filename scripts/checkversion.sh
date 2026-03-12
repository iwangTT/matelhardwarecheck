#!/usr/bin/env bash
set -euo pipefail

# ─── Helpers ────────────────────────────────────────────────────────────────
SEP="────────────────────────────────────────────────────"

section() { echo; echo "=== $1 ==="; echo "$SEP"; }

run_if_available() {
    local cmd="$1"; shift
    if command -v "$cmd" &>/dev/null; then
        "$cmd" "$@"
    else
        echo "(skipped: '$cmd' not found)"
    fi
}

# ─── Tenstorrent ─────────────────────────────────────────────────────────────
section "TT-SMI Firmware Bundle Version"
run_if_available tt-smi-metal -s | grep -i "fw_bundle_version" || true

section "TT-SMI Version"
run_if_available tt-smi-metal -v

section "Tenstorrent Kernel Module"
modinfo tenstorrent 2>/dev/null | grep version || echo "(module not loaded)"

section "TT-Flash Version"
run_if_available tt-flash --version

# ─── Weka ─────────────────────────────────────────────────────────────────────
section "Weka Version"
run_if_available weka version

section "Weka Agent Status"
systemctl status weka-agent --no-pager 2>/dev/null || echo "(weka-agent not active)"

section "Weka Mounts"
mount | grep weka || echo "(no weka mounts found)"

section "MLPerf Mount"
ls -la /mnt/MLPerf 2>/dev/null || echo "(/mnt/MLPerf not accessible)"

# ─── OS & Memory ──────────────────────────────────────────────────────────────
section "OS Info"
lsb_release -a 2>/dev/null

section "Memory Summary"
free -h
