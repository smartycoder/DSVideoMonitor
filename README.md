# DSVideoMonitor

<b>File monitor, auto-indexer and subtitles downloader</b> for Synology DiskStation NAS. Supports push notifications like <b>Pushover</b> and <b>Pushbullet</b>.

# Usage
1. Install Python (if you haven't already) from the DiskStation package manager.
2. SSH into your DiskStation as root (e.g. ssh root@192.168.1.10):
3. Copy files to <code>/var/packages/dsvideomonitor/</code>
4. Run setup: <code>python /var/packages/dsvideomonitor/setup.py install</code>
5. Copy file <code>/var/packages/dsvideomonitor/S99dsvideomonitor.sh</code> to <code>/usr/syno/etc/rc.d/</code>
6. Run command: <code>chmod +x /usr/syno/etc/rc.d/S99dsvideomonitor.sh</code>
7. Run command: <code>/usr/syno/etc/rc.d/S99dsvideomonitor.sh start</code>

# Settings
Modify <code>dsvideomonitor.py</code> and set your own settings.
<p><code>video_folder = "/volume1/video/"</code></p>
<p><code>patterns = ["*.avi", "*.mkv"]</code></p>
<p><code>languages = ["slv", "eng"]</code></p>
<p><code>run_indexer = True</code></p>
<p><code>notifier = PushbulletClient()</code></p>
<p><code>notifier.set_api_key("YOUR_KEY")</code></p>
