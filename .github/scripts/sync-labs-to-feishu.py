import re
import os
import json
import requests
import argparse
from jsonschema import validate


class Feishu:
    """Feishu API"""

    def __init__(self, app_id: str, app_secret: str) -> None:
        self.app_id = app_id
        self.app_secret = app_secret

    def tenant_access_token(self):
        """Get tenant access token"""
        r = requests.post(
            url="https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal",
            headers={
                "Content-Type": "application/json; charset=utf-8",
            },
            data=json.dumps({"app_id": self.app_id, "app_secret": self.app_secret}),
        )
        return r.json()["tenant_access_token"]

    def get_bitable_records(self, app_token: str, table_id: str, params: str) -> None:
        """Get bitable records"""
        records = []
        r = requests.get(
            url=f"https://open.feishu.cn/open-apis/bitable/v1/apps/{app_token}/tables/{table_id}/records?{params}",
            headers={
                "Authorization": f"Bearer {self.tenant_access_token()}",
            },
        )
        if r.json()["data"]["total"] > 0:
            records += r.json()["data"]["items"]
            # 当存在多页时，递归获取
            while r.json()["data"]["has_more"]:
                page_token = r.json()["data"]["page_token"]
                r = requests.get(
                    url=f"https://open.feishu.cn/open-apis/bitable/v1/apps/{app_token}/tables/{table_id}/records?page_token={page_token}&{params}",
                    headers={
                        "Authorization": f"Bearer {self.tenant_access_token()}",
                    },
                )
                if r.json()["data"]["total"] > 0:
                    records += r.json()["data"]["items"]
        return records

    def add_bitable_record(self, app_token: str, table_id: str, data: dict) -> None:
        """Add record to bitable"""
        r = requests.post(
            url=f"https://open.feishu.cn/open-apis/bitable/v1/apps/{app_token}/tables/{table_id}/records",
            headers={
                "Authorization": f"Bearer {self.tenant_access_token()}",
                "Content-Type": "application/json; charset=utf-8",
            },
            data=json.dumps(data),
        )
        return r.json()

    def update_bitable_record(
        self, app_token: str, table_id: str, record_id: str, data: dict
    ) -> None:
        """Update record in bitable"""
        r = requests.put(
            url=f"https://open.feishu.cn/open-apis/bitable/v1/apps/{app_token}/tables/{table_id}/records/{record_id}",
            headers={
                "Authorization": f"Bearer {self.tenant_access_token()}",
                "Content-Type": "application/json; charset=utf-8",
            },
            data=json.dumps(data),
        )
        return r.json()

    def delete_bitable_record(
        self, app_token: str, table_id: str, record_id: str
    ) -> None:
        """Delete record in bitable"""
        r = requests.delete(
            url=f"https://open.feishu.cn/open-apis/bitable/v1/apps/{app_token}/tables/{table_id}/records/{record_id}",
            headers={
                "Authorization": f"Bearer {self.tenant_access_token()}",
                "Content-Type": "application/json; charset=utf-8",
            },
        )
        return r.json()


class Schema:
    def __init__(self, schema_path: str) -> None:
        self.schema_path = schema_path

    def __load_schema(self) -> dict:
        with open(self.schema_path, "r") as f:
            schema = json.load(f)
        return schema

    def validate(self, json_file: str) -> None:
        schema = self.__load_schema()
        with open(json_file, "r") as f:
            data = json.load(f)
        try:
            validate(instance=data, schema=schema)
            return True
        except Exception as e:
            return False


class Sync:
    def __init__(self, app_id: str, app_secret: str, repo: str, schema: str) -> None:
        """Sync labs to feishu

        Args:
            app_id (str): feishu app id
            app_secret (str): feishu app secret
            repo (str): github repo like "labex-dev/devops-labs"
            schema (str): json schema file path
        """
        self.feishu = Feishu(app_id, app_secret)
        self.schema = Schema(schema)
        self.app_token = "bascnNz4Nqjqgqm1Nm5AYke6xxb"
        self.table_id = "tblW2umsCYJWzzUX"
        self.skills_table_id = "tblV5pGIsGZMxmE9"
        self.repo = repo

    def __parse_json(self, file_path: str, skills_dict: dict) -> dict:
        """Parse json file

        Args:
            file_path (str): index.json file path
            skills_dict (dict): feishu skills dict {skill_id: record_id}

        Returns:
            dict: feishu record payload
        """
        with open(file_path, "r") as f:
            index = json.load(f)
        direction = re.compile(r"\.\/[a-z]+").findall(file_path)
        path_slug = file_path.removeprefix("./").removesuffix("/index.json")
        if len(direction) > 0:
            lab_direction = direction[0].replace("./", "").title()
            if lab_direction == "Numpy":
                lab_direction = "NumPy"
            elif lab_direction == "Opencv":
                lab_direction = "OpenCV"
        else:
            lab_direction = None
        lab_title = index.get("title", None)
        lab_desc = index.get("description", None)
        lab_type = index.get("type", None)
        lab_time = index.get("time", None)
        lab_difficulty = index.get("difficulty", None)
        lab_backend = index.get("backend").get("imageid", None)
        lab_steps = index.get("details").get("steps")
        # Count Verify scripts
        lab_scripts = sum(
            [
                len(step.get("verify"))
                for step in lab_steps
                if step.get("verify") != None
            ]
        )
        # Count words in description
        if len(lab_desc) > 1:
            lab_desc_words = len(lab_desc.split())
        else:
            lab_desc_words = 0
        # Get and merge skills
        lab_skills = []
        skills_raw = {}
        for i, step in enumerate(lab_steps):
            skills = step.get("skills")
            if skills:
                lab_skills.extend(skills)
                skills_raw[f"step{i+1}"] = skills
        # Get record is from skills tree table
        in_skills_tree = []
        not_in_skills_tree = []
        if len(lab_skills) > 0:
            for skill in lab_skills:
                skill_id = skills_dict.get(skill)
                if skill_id != None:
                    in_skills_tree.append(skill_id)
                else:
                    not_in_skills_tree.append(skill)
        data = {
            "PATH": path_slug,
            "TITLE": lab_title,
            "DIRECTION": lab_direction,
            "TYPE": lab_type,
            "TIME": lab_time,
            "DIFFICULTY": lab_difficulty,
            "STEPS": len(lab_steps),
            "SCRIPTS": lab_scripts,
            "BACKEND": lab_backend,
            "SKILLS_ID": list(set(lab_skills)),
            "SKILLS_TREE": list(set(in_skills_tree)),
            "SKILLS_RAW": json.dumps(skills_raw),
            "SKILLS_ERROR": list(set(not_in_skills_tree)),
            "DESC_WORDS": lab_desc_words,
            "DESC": lab_desc,
            "GITHUB": {
                "link": f"https://github.com/{self.repo}/tree/master/{path_slug}",
                "text": "OPEN IN GITHUB",
            },
            "REPO_NAME": self.repo,
        }
        return data

    def sync(self, skip: bool, path=".") -> None:
        """Sync labs from github to feishu

        Args:
            skip (bool): skip the labs that already in feishu
            path (str, optional): Defaults to ".".
        """
        # Get all records from feishu
        records = self.feishu.get_bitable_records(
            self.app_token, self.table_id, params=""
        )
        # Make a dict of path and record_id and repo_name
        path_dicts = {
            r["fields"]["PATH"]: {
                "record_id": r["record_id"],
                "repo_name": r["fields"]["REPO_NAME"],
            }
            for r in records
        }
        print(f"Found {len(path_dicts)} labs in Feishu, start syncing...")
        # Get all skills from feishu
        skills = self.feishu.get_bitable_records(
            self.app_token, self.skills_table_id, params=""
        )
        # Make a dict of skill and record_id
        skills_dicts = {
            r["fields"]["SKILL_ID"][0]["text"]: r["record_id"] for r in skills
        }
        print(f"Found {len(skills_dicts)} skills in Feishu, start syncing...")
        # Walk through all index.json files
        # If path in path_dicts, update record
        # If path not in path_dicts, add record
        data_paths = []
        for dirpath, dirnames, filenames in os.walk(path):
            filenames = [f for f in filenames if f == "index.json"]
            for filename in filenames:
                try:
                    filepath = os.path.join(dirpath, filename)
                    data = self.__parse_json(filepath, skills_dicts)
                    # Validate index.json
                    s = self.schema.validate(json_file=filepath)
                    if s:
                        data["JSON_SCHEMA"] = "🟢 VALID"
                    else:
                        data["JSON_SCHEMA"] = "🔴 INVALID"
                    # Make payloads
                    payloads = {"fields": data}
                    # Get data path like "lab-hello-world"
                    data_path = data["PATH"]
                    # Add data path to list for deleting
                    data_paths.append(data_path)
                    # Compare path in feishu and path in repo
                    if data_path in path_dicts:
                        if skip:
                            # Skip record
                            print(f"↓ Skipping {data_path}")
                            continue
                        else:
                            # Update record
                            record_id = path_dicts[data_path]["record_id"]
                            r = self.feishu.update_bitable_record(
                                self.app_token, self.table_id, record_id, payloads
                            )
                            print(f"→ Updating {data_path} {r['msg'].upper()}")
                    else:
                        # Add record
                        r = self.feishu.add_bitable_record(
                            self.app_token, self.table_id, payloads
                        )
                        print(f"↑ Adding {data_path} {r['msg'].upper()}")
                except Exception as e:
                    print(f"× Error {filepath} {e}")
        # Delete records not in this repo
        repo_path_dicts = [
            path for path in path_dicts if path_dicts[path]["repo_name"] == self.repo
        ]
        print(f"Found {len(repo_path_dicts)} labs in this Repo, start deleting...")
        deleted = 0
        for path in repo_path_dicts:
            if path not in data_paths:
                record_id = path_dicts[path]["record_id"]
                r = self.feishu.delete_bitable_record(
                    self.app_token, self.table_id, record_id
                )
                print(f"× Deleting {record_id}-{path} {r['msg'].upper()}")
                deleted += 1
        print(f"Deleted {deleted} labs")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Sync Repo labs to Feishu")
    parser.add_argument("--appid", type=str, help="Feishu App ID")
    parser.add_argument("--appsecret", type=str, help="Feishu App Secret")
    parser.add_argument(
        "--repo", type=str, help="Repo Name like 'labex-dev/devops-labs'"
    )
    parser.add_argument(
        "--schema", type=str, help="Schema file path like 'schema.json'"
    )
    parser.add_argument(
        "--skip", type=bool, default=False, help="Skip updating existing labs"
    )

    args = parser.parse_args()

    sync = Sync(args.appid, args.appsecret, args.repo, args.schema)
    sync.sync(skip=args.skip)
