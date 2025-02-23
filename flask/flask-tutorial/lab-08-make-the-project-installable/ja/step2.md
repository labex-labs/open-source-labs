# 必要なファイルを含める

setuptools のビルドバックエンドには、プロジェクトに非 Python ファイルを含めるために、別の `MANIFEST.in` という名前のファイルが必要です。

次の内容の `MANIFEST.in` を作成します。

```none
# MANIFEST.in

include flaskr/schema.sql
graft flaskr/static
graft flaskr/templates
global-exclude *.pyc
```

これは、ビルドに対して `static` と `templates` ディレクトリ内のすべてと `schema.sql` ファイルをコピーするように指示し、すべてのバイトコードファイルを除外するようにします。
