import sqlite3
conn = sqlite3.connect('diona.db')

c = conn.cursor()

c.execute("drop TABLE Asset")

