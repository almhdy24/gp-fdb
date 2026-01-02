# Transactions (ACID-lite)

## WAL

All write operations MUST be logged before commit.

## Commit Rules

- WAL append
- Apply changes
- Clear WAL

## Recovery

- Replay committed tx
- Drop incomplete tx
