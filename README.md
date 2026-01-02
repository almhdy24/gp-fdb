# GP-FDB

**GP-FDB** is a general-purpose, embedded, flat-file database engine
defined by a **language-independent specification**.

It uses JSON files, deterministic data structures, and portable
algorithms to provide:

- Document storage
- Indexing (field, range, full-text)
- Mini query language (WHERE)
- ACID-lite transactions
- LRU memory cache

> This project is a specification first.
> Implementations must follow the spec exactly.

## Design Goals

- No external dependencies
- Same behavior in every language
- Offline-first
- Simple enough to audit
- Powerful enough to replace SQLite in small systems

## Non-Goals

- Multi-writer concurrency
- Distributed replication
- Network server

## File-Based Architecture
- store.json      → primary storage
- idx_field.json  → equality indexes
- idx_range.json  → ordered indexes
- idx_text.json   → full-text search
- wal.log         → crash safety

  ## Status

- Spec:  stable v1
- Reference algorithms: ✔️
- Language ports: ⏳ community-driven
