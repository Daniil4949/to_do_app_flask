CREATE TABLE IF NOT EXISTS tasks (
id integer PRIMARY KEY AUTOINCREMENT,
title text NOT NULL,
info text,
is_done integer DEFAULT 0
);