import sqlite3 as lite

# connect to the output database
openwpm_db = "docker-volume/crawl-data.sqlite"
conn = lite.connect(openwpm_db)
cur = conn.cursor()

# scans through the database, checking for first parties on which the email is leaked
for symbol, script_url, time, line, col in cur.execute("SELECT symbol, script_url, time_stamp, script_line, script_col FROM javascript"):
    print(time, symbol, script_url, line, col)

