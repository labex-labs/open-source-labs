# ジェネレータ管理の実用的なアプリケーション

このステップでは、ジェネレータの管理とジェネレータ内での例外処理について学んだ概念を、実世界のシナリオにどのように適用するかを探ります。これらの実用的なアプリケーションを理解することで、より堅牢で効率的な Python コードを書くことができます。

## 堅牢なファイル監視システムの作成

より信頼性の高いファイル監視システムを構築しましょう。このシステムは、タイムアウトやユーザーからの停止要求など、さまざまな状況を処理できるようになります。

まず、WebIDE エディタを開き、`robust_follow.py` という名前の新しいファイルを作成します。このファイルに書くコードは次の通りです。

```python
import os
import time
import signal

class TimeoutError(Exception):
    pass

def timeout_handler(signum, frame):
    raise TimeoutError("Operation timed out")

def follow(filename, timeout=None):
    """
    A generator that yields new lines in a file.
    With timeout handling and proper cleanup.
    """
    try:
        # Set up timeout if specified
        if timeout:
            signal.signal(signal.SIGALRM, timeout_handler)
            signal.alarm(timeout)

        with open(filename, 'r') as f:
            f.seek(0, os.SEEK_END)
            while True:
                line = f.readline()
                if line == '':
                    # No new data, wait briefly
                    time.sleep(0.1)
                    continue
                yield line
    except TimeoutError:
        print(f"Following timed out after {timeout} seconds")
    except GeneratorExit:
        print("Following stopped by request")
    finally:
        # Clean up timeout alarm if it was set
        if timeout:
            signal.alarm(0)
        print("Follow generator cleanup complete")
```

このコードでは、まずカスタムの `TimeoutError` クラスを定義しています。`timeout_handler` 関数は、タイムアウトが発生したときにこのエラーを発生させるために使用されます。`follow` 関数は、ファイルを読み取り、新しい行を生成するジェネレータです。タイムアウトが指定されている場合、`signal` モジュールを使用してアラームを設定します。ファイルに新しいデータがない場合は、しばらく待ってから再度試みます。`try - except - finally` ブロックは、さまざまな例外を処理し、適切なクリーンアップを行うために使用されます。

コードを書いたら、ファイルを保存します。

## 堅牢なファイル監視システムの実験

では、改良したファイル監視システムをテストしましょう。ターミナルを開き、次のコマンドで Python インタープリタを起動します。

```bash
cd ~/project
python3
```

### 実験 1: 基本的な使用方法

Python インタープリタで、`follow` ジェネレータの基本的な機能をテストします。実行するコードは次の通りです。

```python
>>> from robust_follow import follow
>>> f = follow('stocklog.csv')
>>> for i, line in enumerate(f):
...     print(f"Line {i+1}: {line.strip()}")
...     if i >= 2:  # Just read a few lines for the example
...         break
...
Line 1: "MO",70.29,"6/11/2007","09:30.09",-0.01,70.25,70.30,70.29,365314
Line 2: "VZ",42.91,"6/11/2007","09:34.28",-0.16,42.95,42.91,42.78,210151
Line 3: "HPQ",45.76,"6/11/2007","09:34.29",0.06,45.80,45.76,45.59,257169
```

ここでは、`robust_follow.py` ファイルから `follow` 関数をインポートしています。そして、`stocklog.csv` ファイルを監視するジェネレータオブジェクト `f` を作成します。`for` ループを使用して、ジェネレータが生成する行を反復処理し、最初の 3 行を出力します。

### 実験 2: タイムアウトの使用

タイムアウト機能がどのように動作するかを見てみましょう。Python インタープリタで次のコードを実行します。

```python
>>> # Create a generator that will time out after 3 seconds
>>> f = follow('stocklog.csv', timeout=3)
>>> for line in f:
...     print(line.strip())
...     time.sleep(1)  # Process each line slowly
...
"MO",70.29,"6/11/2007","09:30.09",-0.01,70.25,70.30,70.29,365314
"VZ",42.91,"6/11/2007","09:34.28",-0.16,42.95,42.91,42.78,210151
"HPQ",45.76,"6/11/2007","09:34.29",0.06,45.80,45.76,45.59,257169
Following timed out after 3 seconds
Follow generator cleanup complete
```

この実験では、3 秒でタイムアウトするジェネレータを作成しています。各行の処理を 1 秒間スリープすることでゆっくりと行います。約 3 秒後、ジェネレータはタイムアウト例外を発生させ、`finally` ブロックのクリーンアップコードが実行されます。

### 実験 3: 明示的なクローズ

ジェネレータが明示的なクローズをどのように処理するかをテストしましょう。次のコードを実行します。

```python
>>> f = follow('stocklog.csv')
>>> for i, line in enumerate(f):
...     print(f"Line {i+1}: {line.strip()}")
...     if i >= 1:
...         print("Explicitly closing the generator...")
...         f.close()
...
Line 1: "MO",70.29,"6/11/2007","09:30.09",-0.01,70.25,70.30,70.29,365314
Line 2: "VZ",42.91,"6/11/2007","09:34.28",-0.16,42.95,42.91,42.78,210151
Explicitly closing the generator...
Following stopped by request
Follow generator cleanup complete
```

ここでは、ジェネレータを作成し、その行を反復処理し始めます。2 行を処理した後、`close` メソッドを使用してジェネレータを明示的にクローズします。その後、ジェネレータは `GeneratorExit` 例外を処理し、必要なクリーンアップを行います。

## エラー処理を備えたデータ処理パイプラインの作成

次に、コルーチンを使用して簡単なデータ処理パイプラインを作成します。このパイプラインは、さまざまな段階でエラーを処理できるようになります。

WebIDE エディタを開き、`pipeline.py` という名前の新しいファイルを作成します。このファイルに書くコードは次の通りです。

```python
def consumer(func):
    def start(*args,**kwargs):
        c = func(*args,**kwargs)
        next(c)
        return c
    return start

@consumer
def grep(pattern, target):
    """Filter lines containing pattern and send to target"""
    try:
        while True:
            line = yield
            if pattern in line:
                target.send(line)
    except Exception as e:
        target.throw(e)

@consumer
def printer():
    """Print received items"""
    try:
        while True:
            item = yield
            print(f"PRINTER: {item}")
    except Exception as e:
        print(f"PRINTER ERROR: {repr(e)}")

def follow_and_process(filename, pattern):
    """Follow a file and process its contents"""
    import time
    import os

    output = printer()
    filter_pipe = grep(pattern, output)

    try:
        with open(filename, 'r') as f:
            f.seek(0, os.SEEK_END)
            while True:
                line = f.readline()
                if not line:
                    time.sleep(0.1)
                    continue
                filter_pipe.send(line)
    except KeyboardInterrupt:
        print("Processing stopped by user")
    finally:
        filter_pipe.close()
        output.close()
```

このコードでは、`consumer` デコレータを使用してコルーチンを初期化しています。`grep` コルーチンは、特定のパターンを含む行をフィルタリングし、別のコルーチンに送信します。`printer` コルーチンは、受け取ったアイテムを出力します。`follow_and_process` 関数は、ファイルを読み取り、`grep` コルーチンを使用して行をフィルタリングし、`printer` コルーチンを使用して一致する行を出力します。また、`KeyboardInterrupt` 例外を処理し、適切なクリーンアップを行います。

コードを書いたら、ファイルを保存します。

## データ処理パイプラインのテスト

データ処理パイプラインをテストしましょう。ターミナルで次のコマンドを実行します。

```bash
cd ~/project
python3 -c "from pipeline import follow_and_process; follow_and_process('stocklog.csv', 'IBM')"
```

次のような出力が表示されるはずです。

```
PRINTER: "IBM",102.86,"6/11/2007","09:34.44",-0.21,102.87,102.86,102.77,147550

PRINTER: "IBM",102.91,"6/11/2007","09:37.31",-0.16,102.87,102.91,102.77,190859

PRINTER: "IBM",102.95,"6/11/2007","09:39.44",-0.12,102.87,102.95,102.77,225350
```

この出力は、パイプラインが正しく動作しており、"IBM" パターンを含む行をフィルタリングして出力していることを示しています。

プロセスを停止するには、`Ctrl+C` を押します。次のメッセージが表示されるはずです。

```
Processing stopped by user
```

## 要点

1. ジェネレータで適切な例外処理を行うことで、エラーをうまく処理できる堅牢なシステムを作成することができます。これは、何かがうまくいかないときにプログラムが予期せずクラッシュしないことを意味します。
2. タイムアウトなどの手法を使用することで、ジェネレータが無限に実行されるのを防ぐことができます。これにより、システムリソースを管理し、プログラムが無限ループに陥るのを防ぐことができます。
3. ジェネレータとコルーチンは、エラーを適切なレベルで伝播させて処理できる強力なデータ処理パイプラインを形成することができます。これにより、複雑なデータ処理システムを構築しやすくなります。
4. ジェネレータの `finally` ブロックは、ジェネレータがどのように終了してもクリーンアップ操作が実行されることを保証します。これにより、プログラムの整合性を維持し、リソースリークを防ぐことができます。
