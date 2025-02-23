# 初めてのコンテナを実行する

初めてのコンテナを実行するために、Docker CLI を使用します。

LabEx VM 上でターミナルを開きます。

コマンドを実行します。

```bash
docker container run -t ubuntu top
```

`docker container run` コマンドを使用して、`top` コマンドを使って `ubuntu` イメージでコンテナを実行します。`-t` フラグは、`top` が正常に機能するために必要な疑似 TTY を割り当てます。

```bash
$ docker container run -it ubuntu top
Unable to find image 'ubuntu:latest' locally
latest: Pulling from library/ubuntu
aafe6b5e13de: Pull complete
0a2b43a72660: Pull complete
18bdd1e546d2: Pull complete
8198342c3e05: Pull complete
f56970a44fd4: Pull complete
Digest: sha256:f3a61450ae43896c4332bda5e78b453f4a93179045f20c8181043b26b5e79028
Status: Downloaded newer image for ubuntu:latest
```

`docker run` コマンドは最初に、`docker pull` を行って、ubuntu イメージをホストにダウンロードします。ダウンロードが完了すると、コンテナが起動します。実行中のコンテナの出力は次のようになります。

```bash
top - 20:32:46 up 3 days, 17:40,  0 users,  load average: 0.00, 0.01, 0.00
Tasks:   1 total,   1 running,   0 sleeping,   0 stopped,   0 zombie
%Cpu(s):  0.0 us,  0.1 sy,  0.0 ni, 99.9 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
KiB Mem :  2046768 total,   173308 free,   117248 used,  1756212 buff/cache
KiB Swap:  1048572 total,  1048572 free,        0 used.  1548356 avail Mem

PID USER      PR  NI    VIRT    RES    SHR S  %CPU %MEM     TIME+ COMMAND
      1 root      20   0   36636   3072   2640 R   0.3  0.2   0:00.04 top
```

`top` は、システム上のプロセスを表示し、リソース消費に基づいて並べ替える Linux ユーティリティです。この出力には単一のプロセスのみが表示されます。それは `top` プロセス自体です。このリストにホストの他のプロセスは表示されません。これは PID ネームスペースの孤立のためです。

コンテナは、Linux ネームスペースを使用して、他のコンテナやホストからのシステム リソースの孤立を提供します。PID ネームスペースは、プロセス ID の孤立を提供します。コンテナ内で `top` を実行すると、コンテナの PID ネームスペース内のプロセスが表示されることに気付きます。これは、ホスト上で `top` を実行した場合とは大きく異なります。

私たちは `ubuntu` イメージを使用していますが、重要なことは、私たちのコンテナに独自のカーネルはありません。コンテナはホストのカーネルを使用し、`ubuntu` イメージは、ubuntu システム上で利用可能なファイル システムとツールを提供するためにのみ使用されます。

`docker container exec` でコンテナを調べる

`docker container exec` コマンドは、新しいプロセスで実行中のコンテナのネームスペースに「入る」方法です。

新しいターミナルを開きます。`Terminal` > `New Terminal` を選択します。

新しいターミナルで、`docker container ls` コマンドを使用して、先ほど作成した実行中のコンテナの ID を取得します。

```bash
$ docker container ls
CONTAINER ID IMAGE COMMAND CREATED STATUS PORTS NAMES
b3ad2a23fab3 ubuntu "top" 29 minutes ago Up 29 minutes goofy_nobel
```

次に、その ID を使用して、`docker container exec` コマンドを使ってそのコンテナ内で `bash` を実行します。bash を使用し、ターミナルからこのコンテナと対話したいので、疑似ターミナルを割り当てながら対話型モードで実行するために `-it` フラグを使用します。

```bash
$ docker container exec -it ID < CONTAINER > bash
root@b3ad2a23fab3:/#
```

では、完成です！私たちは `docker container exec` コマンドを使用して、bash プロセスでコンテナのネームスペースに「入りました」。`bash` とともに `docker container exec` を使用することは、Docker コンテナを調べるための一般的なパターンです。

ターミナルの接頭辞の変化に注意してください。たとえば、`root@b3ad2a23fab3:/`。これは、私たちがコンテナの「中」で bash を実行していることを示しています。

**注**: これは、別のホストや VM に ssh 接続するのと同じではありません。bash プロセスと接続するために ssh サーバーは必要ありません。コンテナは、カーネル レベルの機能を使用して孤立を実現し、コンテナはカーネルの上で実行されます。私たちのコンテナは、同じホスト上で孤立して実行されるプロセスのグループにすぎず、`docker container exec` を使用して、`bash` プロセスでその孤立状態に入ることができます。`docker container exec` を実行した後、孤立して実行されるプロセスのグループ（すなわち、私たちのコンテナ）には `top` と `bash` が含まれます。

同じターミナルから、`ps -ef` を実行して実行中のプロセスを調べます。

```bash
root@b3ad2a23fab3:/# ps -ef
UID PID PPID C STIME TTY TIME CMD
root 1 0 0 20:34? 00:00:00 top
root 17 0 0 21:06? 00:00:00 bash
root 27 17 0 21:14? 00:00:00 ps -ef
```

`top` プロセス、`bash` プロセス、および `ps` プロセスのみが表示されるはずです。

比較のために、コンテナを終了し、ホスト上で `ps -ef` または `top` を実行します。これらのコマンドは、Linux または Mac で機能します。Windows の場合、実行中のプロセスを `tasklist` を使用して調べることができます。

```bash
root@b3ad2a23fab3:/# exit
exit
$ ps -ef
# たくさんのプロセスが表示されます！
```

**技術的な詳細**
PID は、コンテナにシステム リソースの孤立を提供する Linux ネームスペースの 1 つにすぎません。他の Linux ネームスペースには、以下が含まれます。

- MNT - 他のネームスペースに影響を与えることなく、ディレクトリをマウントおよびアンマウントします。
- NET - コンテナに独自のネットワーク スタックがあります。
- IPC - メッセージ キューなどの孤立したプロセス間通信メカニズム。
- User - システム上のユーザーの孤立したビュー。
- UTC - 各コンテナでホスト名とドメイン名を設定します。

これらのネームスペースは一緒になって、コンテナに孤立を提供し、同じシステム上で実行される他のコンテナと安全に競合することなく一緒に実行できるようにします。次に、コンテナのさまざまな使い方と、同じホスト上で複数のコンテナを実行する際の孤立の利点を示します。

**注**: ネームスペースは **Linux** カーネルの機能です。しかし、Docker を使用すると、Windows と Mac でもコンテナを実行できます... どのように機能するのでしょうか？秘密は、Docker 製品または Docker エンジンに埋め込まれている Linux サブシステムにあります。Docker はこの Linux サブシステムを新しいプロジェクトにオープンソース化しました。[LinuxKit](https://github.com/linuxkit/linuxkit)。コンテナを多くの異なるプラットフォームで実行できることは、コンテナに Docker ツールを使用する利点の 1 つです。

Windows で Linux サブシステムを使用して Linux コンテナを実行する他に、Windows OS 上のコンテナ プリミティブの作成により、ネイティブ Windows コンテナが可能になりました。ネイティブ Windows コンテナは、Windows 10 または Windows Server 2016 以降で実行できます。

**注**: この演習をコンテナ化されたターミナルで実行し、ターミナルで `ps -ef` コマンドを実行した場合、`exec` コマンドを終了した後も、依然として限定された一連のプロセスが表示されます。ローカル マシンのターミナルで `ps -ef` コマンドを実行して、すべてのプロセスを表示してみることができます。

`<ctrl>-c` を入力して、`top` プロセスを実行しているコンテナをクリーンアップし、すべてのコンテナを一覧表示して、それらの ID でコンテナを削除します。

```bash
docker ps -a

docker rm <CONTAINER ID>
```
