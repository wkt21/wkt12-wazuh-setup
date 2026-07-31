# Deployment Guide

## Prerequisites

- Docker & Docker Compose
- Git
- Basic familiarity with Wazuh

## Steps

1. **Configure the manager webhook**

   Edit `manager/ossec.conf` and set the correct Intel Center URL:

   ```xml
   <hook_url>https://your-intel-center.example.com/intel/wazuh</hook_url>
   ```

2. **Adjust FIM paths**

   Edit `manager/fim/wkt12_webroot_fim.yaml` to match your application directories:

   ```yaml
   directories:
     - /var/www/html/
     - /srv/your-app/
   ```

3. **Configure the API**

   Edit `wkt12-api/config.yaml`:

   ```yaml
   intel_center:
     base_url: "https://your-intel-center.example.com"
     killfeed_endpoint: "/killfeed"
     api_key: "YOUR_API_KEY"
   ```

4. **Start the stack**

   ```bash
   cd docker
   cp .env.example .env
   docker-compose up -d
   ```

5. **Install Wazuh agents**

   Use `agent/ossec.conf` as a template. Replace `WAZUH_MANAGER_IP` with the IP of your Wazuh manager.

6. **Verify connectivity**

   - Open Wazuh Dashboard: http://localhost:5601
   - Confirm agents appear as connected
   - Check API health: http://localhost:8080/health

7. **Validate end-to-end**

   Follow the [Testing Guide](testing.md).
