# リモートからすべてのサブモジュールをプルする

それぞれのリモートから更新する必要があるサブモジュールを持つ Git リポジトリがあります。サブモジュールごとに手動でプルするのは面倒くさく、エラーが発生しやすい場合があります。一度にすべてのサブモジュールをプルする方法が必要です。

`git` という名前の Git リポジトリがあり、そこにサブモジュールが含まれていると仮定すると、次のコマンドを使用して、それぞれのリモートからすべてのサブモジュールをプルできます。

```shell
cd git
git submodule update --recursive --remote
```

このコマンドは、リポジトリ内のすべてのサブモジュールを、それぞれのリモートに利用可能な最新バージョンに更新します。
