# 遅延された関数の実行

関数 `delay(fn, ms, *args)` を書きます。この関数は、関数 `fn`、ミリ秒単位の時間 `ms`、および任意の数の引数 `args` を受け取ります。この関数は、`fn` の実行を `ms` ミリ秒だけ遅らせ、その後、提供された引数で `fn` を呼び出す必要があります。この関数は、`fn` を呼び出した結果を返す必要があります。

`fn` の実行を遅らせるには、`time.sleep()` 関数を使用します。この関数は、秒数を引数として受け取るため、`ms` を秒数に変換してから `time.sleep()` に渡す必要があります。

```python
from time import sleep

def delay(fn, ms, *args):
  sleep(ms / 1000)
  return fn(*args)
```

```python
delay(lambda x: print(x), 1000, 'later') # 1秒後に 'later' と表示されます
```
