# デバッグのヒント

さて、あなたのプログラムはクラッシュしてしまいました...

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
AttributeError: 'int' object has no attribute 'append'
```

これでどうしたらいいのでしょうか？
