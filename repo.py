import json
import csv
from pathlib import Path
from typing import List, Dict


class ModelRepository:
    def __init__(self, data_dir="data"):
        self.data_dir = Path(data_dir)
        self.data_dir.mkdir(exist_ok=True)
        self.db_path = self.data_dir / "profiles.json"

    def _load(self) -> List[Dict]:
        if not self.db_path.exists():
            return []
        try:
            return json.loads(self.db_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            return []

    def _save(self, profiles: List[Dict]):
        self.db_path.write_text(
            json.dumps(profiles, ensure_ascii=False, indent=2),
            encoding="utf-8"
        )

    def add_profiles(self, profiles_dict: Dict):
        profiles = self._load()
        profiles.append(profiles_dict)
        self._save(profiles)

    def read_profiles(self) -> List[Dict]:
        return self._load()

    def search_profiles(self, query: str) -> List[Dict]:
        query = query.lower()
        profiles = self._load()
        return [
            p for p in profiles
            if query in p["name"].lower()
            or query in p["email"].lower()
        ]
