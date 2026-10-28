"""Whole-file writes for files that other runs read while this one works: board.json and the query caches.
A reader sees the old content or the new content, never a half-written file, even if the process is killed."""
from __future__ import annotations

import os
import threading
from pathlib import Path


def temp_path(path: Path) -> Path:
    """A sibling of path, unique per process and thread, on the same filesystem so os.replace stays atomic."""
    return path.with_name(f".{path.name}.{os.getpid()}.{threading.get_ident()}.tmp")


def write_atomic(path: Path | str, data: str | bytes) -> None:
    """Replace path with data (str is written as UTF-8). On failure the old file is untouched and no temp file remains."""
    path = Path(path)
    tmp = temp_path(path)
    try:
        tmp.write_bytes(data.encode("utf-8") if isinstance(data, str) else data)
        os.replace(tmp, path)
    finally:
        tmp.unlink(missing_ok=True)
