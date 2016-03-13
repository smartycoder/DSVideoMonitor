# DSVideoMonitor

<b>File monitor, auto-indexer and subtitles downloader</b> (using subliminal) for Synology DiskStation NAS. Supports push notifications like <b>Pushover</b> and <b>Pushbullet</b>.

# Install
1. Install Python (if you haven't already) from the DiskStation package manager.
2. SSH into your DiskStation as root (e.g. ssh root@192.168.1.10)
3. Download and unpack ZIP file: <br />
<code>wget https://github.com/smartycoder/DSVideoMonitor/archive/master.zip</code><br />
<code>unzip master.zip</code><br />
4. Copy files to <code>/var/packages/dsvideomonitor/</code>:<br />
<code>cp -r DSVideoMonitor-master/* /var/packages/dsvideomonitor/</code>
5. Run setup: <code>python /var/packages/dsvideomonitor/setup.py install</code>
6. Copy file <code>/var/packages/dsvideomonitor/S99dsvideomonitor.sh</code> to <code>/usr/syno/etc/rc.d/</code><br />
<code>cp /var/packages/dsvideomonitor/S99dsvideomonitor.sh /usr/syno/etc/rc.d/</code>
7. Run command: <code>chmod +x /usr/syno/etc/rc.d/S99dsvideomonitor.sh</code>
8. Run command: <code>/usr/syno/etc/rc.d/S99dsvideomonitor.sh start</code>

# Settings
Modify <code>dsvideomonitor.py</code> and set your own settings.
<code>video_folder = "/volume1/video/"</code>
<code>patterns = ["*.avi", "*.mkv"]</code>
<code>languages = ["slv", "eng"]</code>
<code>run_indexer = True</code>
<code>notifier = PushbulletClient()</code>
<code>notifier.set_api_key("YOUR_KEY")</code>
