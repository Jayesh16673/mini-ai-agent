from app.db.database import get_connection


def tool_save_memory(key: str, value: str) -> dict:
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "INSERT OR REPLACE INTO memory (key, value) VALUES (?, ?)",
        (key, value)
    )

    conn.commit()
    conn.close()

    return {
        "key": key,
        "value": value
    }


def tool_get_memory(key: str) -> dict:
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "SELECT value FROM memory WHERE key = ?",
        (key,)
    )

    row = cur.fetchone()
    conn.close()

    if row:
        return {"key": key, "value": row[0]}
    else:
        return {"key": key, "value": None}
