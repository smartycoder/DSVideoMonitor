#!/bin/sh
# /usr/syno/etc/rc.d/S99dsvideomonitor.sh

case "$1" in
  start|"")
    #start the monitoring daemon
    python /var/packages/dsvideomonitor/dsvideomonitor.py start
    ;;
  restart|reload|force-reload)
    echo "Error: argument '$1' not supported" >&2
    exit 3
    ;;
  stop)
    python /var/packages/dsvideomonitor/dsvideomonitor.py stop
    ;;
  *)
    echo "Usage: S99dsvideomonitor.sh [start|stop]" >&2
    exit 3
    ;;
esac
