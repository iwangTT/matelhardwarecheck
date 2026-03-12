# matelhardwarecheck
check the hardware status

tt-smi-metal -s | grep -i "fw_bundle_version"  
tt-smi-metal -v  
modinfo tenstorrent | grep version  
tt-flash --version
weka version
lsb_release -a
free -h
cat /proc/meminfo
systemctl status weka-agent
mount | grep weka
ls -la /mnt/MLPerf
