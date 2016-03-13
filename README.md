# DSVideoMonitor

<b>File monitor, auto-indexer and subtitles downloader</b> for Synology DiskStation NAS. Supports push notifications like <b>Pushover</b> and <b>Pushbullet</b>.

# Usage
1. Install Python (if you haven't already) from the DiskStation package manager.
2. SSH into your DiskStation as root (e.g. ssh root@192.168.1.10):
3. Copy files to <code>/var/packages/dsvideomonitor/</code>
4. Run setup: <code>pip setup.py install</code>
5. Copy file <code>S99dsvideomonitor.sh</code> to <code>/usr/syno/etc/rc.d/</code>
6. Run command: <code>chmod +x /usr/syno/etc/rc.d/S99dsvideomonitor.sh</code>
7. Run command: <code>/usr/syno/etc/rc.d/S99dsvideomonitor.sh start</code>

