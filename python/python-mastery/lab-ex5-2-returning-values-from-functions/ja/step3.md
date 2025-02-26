# フューチャー

時には、Python コードがスレッドやプロセスを介して並行して実行されます。例を示すために、この例を試してみてください：

```python
>>> import time
>>> def worker(x, y):
        print('About to work')
        time.sleep(20)
        print('Done')
        return x + y

>>> worker(2, 3)     # 通常の関数呼び出し
About to work
Done
5
>>>
```

次に、`worker()` を別のスレッドで起動します：

```python
>>> import threading
>>> t = threading.Thread(target=worker, args=(2, 3))
>>> t.start()
About to work
>>>
Done
```

計算結果がどこにも表示されないことに注意してください。それだけでなく、計算がいつ完了するかさえわかりません。ここにはある種のコーディネーションの問題があります。この場合を処理するための慣例は、関数の結果を `Future` にラップすることです。`Future` は将来の結果を表します。以下がその使い方です：

```python
>>> from concurrent.futures import Future
>>> # 関数をラップしてフューチャーを使用する
>>> def do_work(x, y, fut):
        fut.set_result(worker(x,y))

>>> fut = Future()
>>> t = threading.Thread(target=do_work, args=(2, 3, fut))
>>> t.start()
About to work
>>> result = fut.result()
Done
>>> result
5
>>>
```

スレッドプール、プロセス、その他の構造体を扱う場合、このようなパターンがたくさん見られます。たとえば：

```python
>>> from concurrent.futures import ThreadPoolExecutor
>>> pool = ThreadPoolExecutor()
>>> fut = pool.submit(worker, 2, 3)
About to work
>>> fut
<Future at 0x102157080 state=running>
>>> fut.result()
Done
5
>>>
```
