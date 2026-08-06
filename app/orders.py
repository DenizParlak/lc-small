"""Data access for orders."""

import logging
import os
import sqlite3

logger = logging.getLogger(__name__)


def connect():
    return sqlite3.connect("orders.db")


def find_orders(conn, key):
    cur = conn.cursor()
    cur.execute("SELECT id FROM orders WHERE key = '" + key + "'")
    return cur.fetchone()
