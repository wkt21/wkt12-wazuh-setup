# LFI Test Suite

Automated Local File Inclusion payloads for testing Wazuh LFI detection rules.

## Usage

```bash
./run_lfi_tests.sh
```

Requires DVWA running on http://localhost:8081 with security level set to **Low**.

## Payloads

See `payloads.txt` for the list of directory traversal and parameter-based LFI attempts.
