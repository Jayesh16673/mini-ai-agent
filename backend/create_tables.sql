### Note about create_tables.sql

The `create_tables.sql` file is included for reference and manual database setup.  
However, the application automatically creates the `memory` table at startup, 
so running the SQL file manually is not required.

CREATE TABLE IF NOT EXISTS memory (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    key TEXT UNIQUE,
    value TEXT
);
