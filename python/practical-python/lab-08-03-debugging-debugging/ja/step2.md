# トレースバックの読み方

最後の行がクラッシュの具体的な原因です。

```bash
$ python3 blah.py
Traceback (most recent call last):
  File "blah.py", line 13, in?
    foo()
  File "blah.py", line 10, in foo
    bar()
  File "blah.py", line 7, in bar
    spam()
  File "blah.py", 4, in spam
    line x.append(3)
# クラッシュの原因
AttributeError: 'int' object has no attribute 'append'
```

ただし、読んだり理解したりするのは必ずしも簡単ではありません。

**プロのコツ：トレースバック全体をGoogleに貼り付けましょう。**
