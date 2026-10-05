import sqlite3
from pathlib import Path
DB_PATH=Path(__file__).resolve().parent.parent/'database'/'eims.db'

def connect():
    DB_PATH.parent.mkdir(exist_ok=True); c=sqlite3.connect(DB_PATH); c.row_factory=sqlite3.Row; return c

def init_db():
    with connect() as c:
        c.execute('CREATE TABLE IF NOT EXISTS servers(id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT NOT NULL,host TEXT NOT NULL,environment TEXT NOT NULL,created_at TEXT DEFAULT CURRENT_TIMESTAMP)')
        c.execute('CREATE TABLE IF NOT EXISTS settings(key TEXT PRIMARY KEY,value TEXT NOT NULL)')
        c.execute("INSERT OR IGNORE INTO settings VALUES('refresh_interval','5')"); c.execute("INSERT OR IGNORE INTO settings VALUES('theme','dark')")

def list_servers():
    with connect() as c: return c.execute('SELECT * FROM servers ORDER BY id DESC').fetchall()
def add_server(name,host,environment):
    with connect() as c: c.execute('INSERT INTO servers(name,host,environment) VALUES(?,?,?)',(name,host,environment))
def delete_server(i):
    with connect() as c: c.execute('DELETE FROM servers WHERE id=?',(i,))
def get_setting(k,d=None):
    with connect() as c:
        r=c.execute('SELECT value FROM settings WHERE key=?',(k,)).fetchone(); return r['value'] if r else d
def set_setting(k,v):
    with connect() as c: c.execute('INSERT INTO settings(key,value) VALUES(?,?) ON CONFLICT(key) DO UPDATE SET value=excluded.value',(k,v))
