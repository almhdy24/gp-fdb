# GP-FDB Specification v1

## Document Model

Each document is schema-less and stored as:

{
  "_id": int,
  "_type": string,
  "_created": epoch,
  "_updated": epoch,
  "data": object
}

## Storage Rules

- Append-only writes preferred
- IDs are monotonically increasing
- Deletes should be soft deletes

## Guarantees

- Deterministic ordering
- Crash-safe commits
- Index consistency
