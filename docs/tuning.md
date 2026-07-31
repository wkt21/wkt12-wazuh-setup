# Tuning Guide

## Rule Levels

| Rule ID | Level | Description |
|---------|-------|-------------|
| 900001  | 7     | Directory traversal attempt |
| 900002  | 10    | Suspicious file access |
| 900003  | 12    | Possible LFI attempt |
| 900010  | 15    | Full RCA chain (LFI → FIM → process) |

Adjust levels in `manager/rules/*.xml` according to your risk tolerance.

## FIM Frequency

In `agent/ossec.conf`:

```xml
<syscheck>
  <frequency>300</frequency>  <!-- seconds -->
</syscheck>
```

Lower values increase detection speed but raise CPU/IO load.

## Webhook Threshold

In `manager/ossec.conf`:

```xml
<level>10</level>
```

Only alerts with level ≥ 10 are forwarded to the Intel Center.

## Correlation Timeframe

In `manager/rules/wkt12_rca_chain.xml`:

```xml
<timeframe>30</timeframe>  <!-- seconds -->
```

Increase if legitimate processes take longer to spawn after a file write.

## Adding Custom Paths

Add new directories to both:

- `manager/fim/wkt12_webroot_fim.yaml`
- `agent/ossec.conf` under `<directories>`
