"""Data access for orders."""

import sqlite3


def connect():
    return sqlite3.connect("orders.db")


def find_orders(conn, key):
    cur = conn.cursor()
    cur.execute("SELECT id FROM orders WHERE key = '" + key + "'")
    return cur.fetchone()
