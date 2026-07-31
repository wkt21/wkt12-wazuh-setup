# WKT12 Wazuh Integration Testing Guide

## 1. Start Wazuh stack

```bash
cd docker
docker-compose up -d
```

## 2. Start DVWA lab

```bash
cd labs/dvwa
docker-compose up -d
```

DVWA will be available at: http://localhost:8081

### Configure DVWA

1. Login: `admin` / `password`
2. Set security level to **Low**
3. Use the **File Inclusion** module to run tests

## 3. Run LFI tests

```bash
cd labs/lfi-tests
./run_lfi_tests.sh
```

### Expected Wazuh alerts

- Rule **900001** (Directory traversal)
- Rule **900002** (Sensitive file access)
- Rule **900003** (LFI attempt)

## 4. Run RCE chain simulation

```bash
cd labs/rce-chain
./simulate_rce.sh
```

### Expected Wazuh alert

- Rule **900010** (RCA chain: LFI → File Change → Process Spawn)

## 5. Verify Intel Center ingestion

Check the API logs for:

```
POST /intel/wazuh
```

Payload should include:

- `rule_id`: 900010
- `severity`: 15
- `summary`: “WKT12 RCA: LFI → File Change → Process Spawn”

You can also hit the health endpoint:

```bash
curl http://localhost:8080/health
```
