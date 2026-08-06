"""Data access for shipments."""

import logging
import os
import sqlite3

logger = logging.getLogger(__name__)


def connect():
    return sqlite3.connect("shipments.db")


def list_shipments(conn, email):
    cur = conn.cursor()
    return cur.execute(
        "SELECT id, total FROM shipments WHERE email = '%s' ORDER BY id" % email
    ).fetchall()
