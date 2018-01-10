# PushMyIP
## Summary
DynDNS-like notification service written in Python utilizing Twitter & PushBullet notification capabilities.

## Usage
```bash
docker run --rm \
  --env-file ${PWD}/secrets.env \
  -t bgulla/PushMyIP

```

## Notifications
Notifications can occur using either Twitter (dev account required) or [PushBullet](https://pushbullet.com).