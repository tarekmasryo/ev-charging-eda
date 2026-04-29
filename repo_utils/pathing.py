from __future__ import annotations

import os
from pathlib import Path
from typing import Iterable


def project_root(start: Path | None = None) -> Path:
    """Best-effort repository root detection for notebooks and scripts."""
    current = (start or Path.cwd()).resolve()
    markers = {"README.md", "requirements.txt", ".git"}

    for _ in range(8):
        if any((current / marker).exists() for marker in markers):
            return current
        if current.parent == current:
            break
        current = current.parent

    return (start or Path.cwd()).resolve()


def resolve_data_path(
    filename: str,
    *,
    local_subdir: str = "data/raw",
    kaggle_subdir_hint: str | None = None,
    extra_candidates: Iterable[str | Path] | None = None,
) -> Path:
    """Resolve a dataset file from local folders, an env override, or Kaggle input.

    Priority:
    1. EV_CHARGING_DATA_DIR directory override
    2. DATA_PATH full-file override
    3. <repo>/<local_subdir>/<filename>
    4. extra candidate directories or files
    5. /kaggle/input/<kaggle_subdir_hint>/<filename>
    6. light search under /kaggle/input
    """
    env_dir = os.environ.get("EV_CHARGING_DATA_DIR")
    if env_dir:
        env_candidate = Path(env_dir).expanduser() / filename
        if env_candidate.exists():
            return env_candidate.resolve()

    env_file = os.environ.get("DATA_PATH")
    if env_file:
        env_path = Path(env_file).expanduser()
        if env_path.exists() and env_path.name == filename:
            return env_path.resolve()

    root = project_root()
    local_candidate = root / local_subdir / filename
    if local_candidate.exists():
        return local_candidate.resolve()

    if extra_candidates:
        for candidate in extra_candidates:
            path = Path(candidate).expanduser()
            if path.is_dir():
                path = path / filename
            elif not path.is_absolute():
                path = root / path

            if path.exists():
                return path.resolve()

    kaggle_root = Path("/kaggle/input")
    if kaggle_subdir_hint:
        hinted = kaggle_root / kaggle_subdir_hint / filename
        if hinted.exists():
            return hinted.resolve()

    if kaggle_root.exists():
        for pattern in (f"*/{filename}", f"*/*/{filename}"):
            matches = list(kaggle_root.glob(pattern))
            if matches:
                return matches[0].resolve()

    raise FileNotFoundError(
        f"Could not find '{filename}'. Put the CSV files under 'data/raw/', "
        "attach the Kaggle dataset, or set EV_CHARGING_DATA_DIR."
    )
