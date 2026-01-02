# Query Language (LIN-WHERE)

Queries are expressed as JSON ASTs.

Example:

{
  "type": "user",
  "where": [
    ["age", ">", 18],
    ["status", "==", "active"]
  ],
  "limit": 10
}

## Operators

==   !=   >   <   >=   <=
contains
in
