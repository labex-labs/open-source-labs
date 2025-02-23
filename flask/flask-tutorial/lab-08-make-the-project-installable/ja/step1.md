# プロジェクトの説明

まず、プロジェクトとその構築方法を記述するために `pyproject.toml` ファイルを作成する必要があります。

`pyproject.toml` ファイルは以下のようになります。

```toml
# pyproject.toml

[project]
name = "flaskr" # プロジェクト名
version = "1.0.0" # プロジェクトのバージョン
dependencies = [
    "flask", # プロジェクトの依存関係
]

[build-system]
requires = ["setuptools"] # 必要なビルドシステム
build-backend = "setuptools.build_meta" # バックエンドビルドシステム
```
