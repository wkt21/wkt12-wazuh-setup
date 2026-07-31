# WKT12 Wazuh Integration Setup

<img width="1536" height="1024" alt="61404F51-AC4E-421F-917C-777C96E85C83" src="https://github.com/user-attachments/assets/bd32a772-482f-4988-9200-7f2ade769647" />

This repository provides a **plug-and-play Wazuh integration** for a WKT12-style Intel Center:

- **File Integrity Monitoring (FIM)** for webroots and upload directories
- **LFI detection rules** with custom Wazuh rules
- **RCA correlation** (LFI → file change → process spawn) for faster root cause analysis
- **Webhook integration** into a generic “Intel Center” API (killfeed, malware feed, exploit feed)

## Features

| Feature | Description |
|---------|-------------|
| File Integrity Monitoring (FIM) | Monitor webroots and upload directories for unauthorized changes |
| LFI Detection Rules | Detect Local File Inclusion attempts with custom Wazuh rules |
| RCA Correlation | Correlate LFI → file change → process spawn for faster root cause analysis |
| Intel Center Webhook | Send high-fidelity alerts to your Intel Center (killfeed, malware feed, exploit feed) |

## Quick Start

1. Clone this repo:

```bash
git clone https://github.com/wkt21/wkt12-wazuh-setup.git
cd wkt12-wazuh-setup
```

2. Configure environment:

```bash
cp docker/.env.example docker/.env
```

3. Set your Intel Center URL in `manager/ossec.conf` and `wkt12-api/config.yaml`.

4. Start the stack:

```bash
cd docker
docker-compose up -d
```

5. Install Wazuh agents on your servers and point them to the manager (see `agent/ossec.conf`).

6. Trigger a test LFI scenario (see `docs/testing.md`) and verify alerts in your Intel Center.

## Repository Structure

```
wkt12-wazuh-setup/
├─ README.md
├─ manager/
│  ├─ ossec.conf
│  ├─ rules/
│  │  ├─ wkt12_lfi_rules.xml
│  │  └─ wkt12_rca_chain.xml
│  ├─ fim/
│  │  └─ wkt12_webroot_fim.yaml
│  └─ integration/
│     └─ wazuh_to_wkt12_webhook.json
├─ agent/
│  ├─ ossec.conf
│  └─ examples/
│     ├─ nginx.conf
│     └─ apache.conf
├─ wkt12-api/
│  ├─ main.py
│  ├─ models.py
│  └─ config.yaml
├─ docker/
│  ├─ docker-compose.yml
│  └─ .env.example
├─ labs/
│  ├─ dvwa/
│  ├─ lfi-tests/
│  └─ rce-chain/
└─ docs/
   ├─ deployment.md
   ├─ tuning.md
   └─ testing.md
```

## Documentation

- [Deployment Guide](docs/deployment.md)
- [Tuning Guide](docs/tuning.md)
- [Testing Guide](docs/testing.md)

## License

MIT
