#!/bin/bash

TARGET="http://localhost:8081/vulnerabilities/fi/?page="

echo "[*] Running LFI payloads..."
while read -r payload; do
    echo "[*] Testing: $payload"
    curl -s "$TARGET$payload" > /dev/null
    sleep 1
done < payloads.txt

echo "[+] LFI tests completed."
