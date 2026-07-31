# RCE Chain Simulation

This lab simulates a full exploit chain:

1. LFI attempt
2. File dropped into webroot
3. Process spawned by webserver user

This triggers the WKT12 RCA rule (ID **900010**).

## Steps

```bash
./simulate_rce.sh
```

This will:

- Drop `webshell.php` into the DVWA webroot
- Execute a command through the webshell
- Trigger Wazuh alerts (FIM + process creation)

## Expected Result

Rule 900010 should fire with description:

> WKT12 RCA: LFI → File Change → Process Spawn
