# 並行プログラミングでの Future の使用

Python では、関数を同時に、つまり並行して実行する必要がある場合、スレッドやプロセスなどの便利なツールが用意されています。しかし、ここで一般的な問題に直面します。別のスレッドで実行されている関数が返す値をどのように取得できるのでしょうか。ここで `Future` という概念が非常に重要になります。

`Future` は、後で利用可能になる結果のプレースホルダーのようなものです。関数がまだ実行を完了していなくても、将来生成する値を表す方法です。この概念を簡単な例でもっと理解してみましょう。

### ステップ 1: 新しいファイルを作成する

まず、新しい Python ファイルを作成する必要があります。これを `futures_demo.py` と呼びましょう。ターミナルで以下のコマンドを使用してこのファイルを作成できます。

```
touch ~/project/futures_demo.py
```

### ステップ 2: 基本的な関数コードを追加する

次に、`futures_demo.py` ファイルを開き、以下の Python コードを追加します。このコードは、単純な関数を定義し、通常の関数呼び出しがどのように機能するかを示しています。

```python
import time
import threading
from concurrent.futures import Future, ThreadPoolExecutor

def worker(x, y):
    """A function that takes time to complete"""
    print('Starting work...')
    time.sleep(5)  # Simulate a time-consuming task
    print('Work completed')
    return x + y

# Part 1: Normal function call
print("--- Part 1: Normal function call ---")
result = worker(2, 3)
print(f"Result: {result}")
```

このコードでは、`worker` 関数は 2 つの数値を受け取り、それらを足し合わせますが、最初に 5 秒間一時停止することで時間のかかるタスクをシミュレートします。この関数を通常の方法で呼び出すと、プログラムは関数が完了するのを待ち、その後戻り値を取得します。

### ステップ 3: 基本コードを実行する

ファイルを保存し、ターミナルで以下のコマンドを使用して実行します。

```
python ~/project/futures_demo.py
```

以下のような出力が表示されるはずです。

```
--- Part 1: Normal function call ---
Starting work...
Work completed
Result: 5
```

これは、通常の関数呼び出しが関数が完了するのを待ち、その後結果を返すことを示しています。

### ステップ 4: 別のスレッドで関数を実行する

次に、`worker` 関数を別のスレッドで実行した場合に何が起こるかを見てみましょう。`futures_demo.py` ファイルに以下のコードを追加します。

```python
# Part 2: Running in a separate thread (problem: no way to get result)
print("\n--- Part 2: Running in a separate thread ---")
t = threading.Thread(target=worker, args=(2, 3))
t.start()
print("Main thread continues while worker runs...")
t.join()  # Wait for the thread to complete
print("Worker thread finished, but we don't have its return value!")
```

ここでは、`threading.Thread` クラスを使用して、新しいスレッドで `worker` 関数を起動しています。メインスレッドは `worker` 関数が完了するのを待たずに、実行を続けます。しかし、`worker` スレッドが終了したときに、戻り値を簡単に取得する方法がありません。

### ステップ 5: スレッド化されたコードを実行する

再度ファイルを保存し、同じコマンドを使用して実行します。

```
python ~/project/futures_demo.py
```

メインスレッドが続行し、`worker` スレッドが実行されますが、`worker` 関数の戻り値にアクセスできないことに気付くでしょう。

### ステップ 6: `Future` を手動で使用する

スレッドから戻り値を取得する問題を解決するために、`Future` オブジェクトを使用することができます。`futures_demo.py` ファイルに以下のコードを追加します。

```python
# Part 3: Using a Future to get the result
print("\n--- Part 3: Using a Future manually ---")

def do_work_with_future(x, y, future):
    """Wrapper that sets the result in the Future"""
    result = worker(x, y)
    future.set_result(result)

# Create a Future object
fut = Future()

# Start a thread that will set the result in the Future
t = threading.Thread(target=do_work_with_future, args=(2, 3, fut))
t.start()

print("Main thread continues...")
print("Waiting for the result...")
# Block until the result is available
result = fut.result()  # This will wait until set_result is called
print(f"Got the result: {result}")
```

このコードでは、`Future` オブジェクトを作成し、新しい関数 `do_work_with_future` に渡します。この関数は `worker` 関数を呼び出し、その後 `Future` オブジェクトに結果を設定します。メインスレッドは、結果が利用可能になったときに `Future` オブジェクトの `result()` メソッドを使用して結果を取得できます。

### ステップ 7: `Future` を使用したコードを実行する

ファイルを保存し、再度実行します。

```
python ~/project/futures_demo.py
```

これで、スレッドで実行されている関数から戻り値を正常に取得できることがわかります。

### ステップ 8: `ThreadPoolExecutor` を使用する

Python の `ThreadPoolExecutor` クラスは、並行タスクの処理をさらに簡単にします。`futures_demo.py` ファイルに以下のコードを追加します。

```python
# Part 4: Using ThreadPoolExecutor (easier way)
print("\n--- Part 4: Using ThreadPoolExecutor ---")
with ThreadPoolExecutor() as executor:
    # Submit the work to the executor
    future = executor.submit(worker, 2, 3)

    print("Main thread continues after submitting work...")
    print("Checking if the future is done:", future.done())

    # Get the result (will wait if not ready)
    result = future.result()
    print("Now the future is done:", future.done())
    print(f"Final result: {result}")
```

`ThreadPoolExecutor` は、`Future` オブジェクトの作成と管理を代行します。関数とその引数を渡すだけで、結果を取得するために使用できる `Future` オブジェクトが返されます。

### ステップ 9: 完全なコードを実行する

最後にファイルを保存し、実行します。

```
python ~/project/futures_demo.py
```

### 解説

1. **通常の関数呼び出し**: 関数を通常の方法で呼び出すと、プログラムは関数が完了するのを待ち、直接戻り値を取得します。
2. **スレッドの問題**: 関数を別のスレッドで実行することには欠点があります。そのスレッドで実行されている関数の戻り値を取得する組み込みの方法がありません。
3. **手動での Future の使用**: `Future` オブジェクトを作成してスレッドに渡すことで、`Future` に結果を設定し、メインスレッドから結果を取得することができます。
4. **ThreadPoolExecutor**: このクラスは並行プログラミングを簡素化します。`Future` オブジェクトの作成と管理を代行するため、関数を並行して実行し、その戻り値を取得することが容易になります。

`Future` オブジェクトにはいくつかの便利なメソッドがあります。

- `result()`: このメソッドは、関数の結果を取得するために使用されます。結果がまだ準備されていない場合、準備ができるまで待機します。
- `done()`: このメソッドを使用して、関数の計算が完了したかどうかを確認できます。
- `add_done_callback()`: このメソッドを使用すると、結果が準備できたときに呼び出される関数を登録することができます。

このパターンは、並行プログラミング、特に並列で実行されている関数から結果を取得する必要がある場合に非常に重要です。
