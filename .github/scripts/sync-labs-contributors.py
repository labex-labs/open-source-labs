import os
import json
import requests
import argparse


class GitHub:
    """GitHub 相关 API"""

    def __init__(self, token: str) -> None:
        self.token = token

    def get_contributors(self, repo_name: str, file_path: str) -> str:
        # Set the API URL
        url = f"https://api.github.com/repos/{repo_name}/commits"
        # Set the headers for authentication
        headers = {
            "Authorization": f"token {self.token}",
            "Accept": "application/vnd.github+json",
        }

        # Set the parameters to filter commits by file path
        params = {"path": file_path}

        # Send the request
        r = requests.get(url, headers=headers, params=params)
        # Check if the request was successful
        try:
            commits = r.json()
            contributors = set()
            # Iterate through the commits and extract the author's login
            for commit in commits:
                author = commit["author"]["login"]
                contributors.add(author)
            return list(contributors)
        except:
            return []


class Add:
    def __init__(self, ghtoken: str) -> None:
        self.github = GitHub(token=ghtoken)

    def get_index_json(self, path: str) -> list:
        # get all index.json from the directory and subdirectories
        idx = []
        for root, dirs, files in os.walk(path):
            for file in files:
                if file == "index.json":
                    idx.append(os.path.join(root, file).replace("./", ""))
        return idx

    def add_contributors(self, path: str, repo: str) -> None:
        idx = self.get_index_json(path=path)
        i = 1
        for file in idx:
            contributors = self.github.get_contributors(repo_name=repo, file_path=file)
            # read index.json
            with open(file, "r") as f:
                index = json.load(f)
            # original contributors
            original_contributors = index.get("contributors", [])
            # update contributors
            now_contributors = list(set(original_contributors + contributors))
            # remove huhuhang and name contains bot
            now_contributors = [c for c in now_contributors if "bot" not in c]
            # sort contributors
            now_contributors.sort()
            # add contributors
            index["contributors"] = now_contributors
            # write index.json
            with open(file, "w") as f:
                json.dump(index, f, indent=2)
            print(
                f"{i}/{len(idx)}: {file} contributors {len(now_contributors) - len(original_contributors)}, total {len(now_contributors)}"
            )
            i += 1


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Add Repo Contributors to index.json")
    parser.add_argument(
        "--repo", type=str, help="Repo Name like 'labex-labs/scenarios'"
    )
    parser.add_argument("--ghtoken", type=str, help="GitHub Token")
    args = parser.parse_args()
    add = Add(ghtoken=args.ghtoken)
    add.add_contributors(path="./", repo=args.repo)
