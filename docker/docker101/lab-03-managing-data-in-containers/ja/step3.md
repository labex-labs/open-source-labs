# [オプション] OverlayFS

OverlayFS は、Linux 用の「ユニオンマウントファイルシステム」の実装です。Docker ボリュームが何であるかを理解するには、Docker における層とファイルシステムの仕組みを理解するのが役立ちます。

コンテナを起動するには、Docker は読み取り専用のイメージを取得し、その上に新しい読み書き可能な層を作成します。層を 1 つのものとして表示するために、Docker はユニオンファイルシステムまたは OverlayFS（オーバーレイファイルシステム）、具体的には`overlay2`ストレージドライバを使用します。

Docker ホストが管理するファイルを見るには、Docker のプロセスファイルシステムにアクセスする必要があります。`--privileged`と`--pid=host`フラグを使用することで、`busybox`のようなコンテナ内からホストのプロセス ID 名前空間にアクセスできます。その後、Docker の`/var/lib/docker/overlay2`ディレクトリに移動して、Docker によって管理されるダウンロードされた層を確認できます。

Docker 内の現在の層のリストを表示するには、

```bash
$ docker run -it --privileged --pid=host busybox nsenter -t 1 -m -u -n -i sh

/ # ls -l /var/lib/docker/overlay2
total 16
drwx------ 3 root root 4096 Sep 25 19:44 0e55ecaa4d17c353191e68022d9a17fde64fb5e9217b07b5c56eb4c74dad5b32
drwx------ 5 root root 4096 Sep 25 19:44 187854d05ccd18980642e820b0d2be6a127ba85d8ed96315bb5ae37eb1add36d
drwx------ 4 root root 4096 Sep 25 19:44 187854d05ccd18980642e820b0d2be6a127ba85d8ed96315bb5ae37eb1add36d-init
drwx------ 2 root root 4096 Sep 25 19:44 l

/ # exit
```

`ubuntu`イメージをダウンロードして再度確認します。

```bash
docker pull ubuntu
docker run -it --privileged --pid=host busybox nsenter -t 1 -m -u -n -i sh
```

再度、層のリストを表示するコマンドを入力します。

```
ls -l /var/lib/docker/overlay2/ & exit
```

`ubuntu`イメージをダウンロードすると、4 つの新しい層が暗黙的にダウンロードされることがわかります。

- a611792b4cac502995fa88a888261dfba0b5d852e72f9db9e075050991423779
- d181f1a41fc35a45c16e8bfcb8eee6f768f3b98f82210a43ea65f284a45fcd65
- dac2f37f6280a076836d39b87b0ae5ebf5c0d386b6d8b991b103aadbcebaa7c6
- f3e921b440c37c86d06cd9c9fb70df50edad553c36cc87f84d5eeba734aae709

`overlay2`ストレージドライバは、本質的にホスト上の異なるディレクトリを重ねて、1 つのディレクトリとして提示します。

- ベース層または lowerdir
- `diff`層または upperdir
- オーバーレイ層（ユーザビュー）
- `work`ディレクトリ

OverlayFS は、ベースイメージとダウンロードされた読み取り専用（R/O）層を含む下部ディレクトリを`lowerdir`と呼びます。

上部ディレクトリは`upperdir`と呼ばれ、読み書き可能（R/W）なコンテナ層です。

統一ビューまたは「オーバーレイ」層は`merged`と呼ばれます。

最後に、`workdir`は必須で、オーバーレイが内部で使用する空のディレクトリです。

`overlay2`ドライバは、最大 128 個の下部 OverlayFS 層をサポートしています。`l`ディレクトリには、シンボリックリンクとして短縮された層識別子が含まれています。

![Overlay2 Storage Driver](../assets/overlay2-driver.png)

クリーンアップします。

```bash
docker system prune -a
clear
```
