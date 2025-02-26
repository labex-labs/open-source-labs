# デバッガの下で実行する

デバッガの下で、全体のプログラムを実行することもできます。

```bash
$ python3 -m pdb someprogram.py
```

最初の文の前に自動的にデバッガに入ります。ブレークポイントを設定したり、設定を変更したりすることができます。

一般的なデバッガコマンド：

```code
(Pdb) help            # ヘルプを取得する
(Pdb) w(here)         # スタックトレースを表示する
(Pdb) d(own)          # 1つ下のスタックレベルに移動する
(Pdb) u(p)            # 1つ上のスタックレベルに移動する
(Pdb) b(reak) loc     # ブレークポイントを設定する
(Pdb) s(tep)          # 1つの命令を実行する
(Pdb) c(ontinue)      # 実行を続ける
(Pdb) l(ist)          # ソースコードを表示する
(Pdb) a(rgs)          # 現在の関数の引数を表示する
(Pdb)!statement      # 文を実行する
```

ブレークポイントの位置は、次のいずれかです。

```code
(Pdb) b 45            # 現在のファイルの45行目
(Pdb) b file.py:45    # file.pyの45行目
(Pdb) b foo           # 現在のファイルのfoo()関数
(Pdb) b module.foo    # モジュール内のfoo()関数
```
