# バインドマウント

Docker は、`volume`構文よりも`mount`構文を推奨しています。バインドマウントは、ボリュームと比較して機能が制限されています。ファイルまたはディレクトリは、コンテナにマウントされる際に、ホストマシン上の完全パスで参照されます。バインドマウントは、ホストマシンのファイルシステムに特定のディレクトリ構造が存在することに依存しており、Docker CLI を使用してバインドマウントを管理することはできません。バインドマウントは、コンテナ内で実行されるプロセスを介してホストファイルシステムを変更する可能性があることにも注意してください。

コロン区切り文字（:）で区切られた 3 つのフィールドを持つ`-v`構文の代わりに、`mount`構文はより冗長で、複数の`キー-値`ペアを使用します。

- type: bind、volume または tmpfs
- source: ホストマシン上のファイルまたはディレクトリのパス
- destination: コンテナ内のパス
- readonly
- bind-propagation: rprivate、private、rshared、shared、rslave、slave
- consistency: consistent、delegated、cached
- mount

```bash
cd /home/labex/project
mkdir data
docker run -it --name busybox --mount type=bind,source="$(pwd)"/data,target=/data busybox sh
```

コンテナ内でコマンドを入力します。

```
echo "hello busybox" > /data/hi.txt
exit
```

ホストマシン上にファイルが作成されたことを確認します。

```
cat data/hi.txt
```
