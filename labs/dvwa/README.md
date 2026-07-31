# DVWA Test Lab

This lab launches DVWA (Damn Vulnerable Web Application) so users can test:

- LFI detection
- File Integrity Monitoring (FIM)
- RCA correlation (LFI → file change → process spawn)

## Start DVWA

```bash
cd labs/dvwa
docker-compose up -d
```

DVWA will be available at:

**http://localhost:8081**

## Configure DVWA

1. Login: `admin` / `password`
2. Set security level to **Low**
3. Use the **File Inclusion** module to run tests

## Run automated LFI tests

```bash
cd ../lfi-tests
./run_lfi_tests.sh
```

This will generate:

- Directory traversal attempts
- Inclusion attempts
- Access to `/etc/passwd`
