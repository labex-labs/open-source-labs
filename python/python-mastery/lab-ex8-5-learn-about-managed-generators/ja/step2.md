# ジェネレーターを使ったタスクスケジューラーの作成

プログラミングにおいて、タスクスケジューラーは複数のタスクを効率的に管理し実行するための重要なツールです。このセクションでは、ジェネレーターを使って、複数のジェネレーター関数を同時に実行できる簡単なタスクスケジューラーを構築します。これにより、ジェネレーターを管理して協調的なマルチタスク処理を行う方法を学びます。協調的なマルチタスク処理とは、タスクが順番に実行され、実行時間を共有することを意味します。

まず、新しいファイルを作成する必要があります。`/home/labex/project` ディレクトリに移動し、`multitask.py` という名前のファイルを作成します。このファイルには、タスクスケジューラーのコードが含まれます。

```python
# multitask.py

from collections import deque

# Task queue
tasks = deque()

# Simple task scheduler
def run():
    while tasks:
        task = tasks.popleft()  # Get the next task
        try:
            task.send(None)     # Resume the task
            tasks.append(task)  # Put it back in the queue
        except StopIteration:
            print('Task done')  # Task is complete

# Example task 1: Countdown
def countdown(n):
    while n > 0:
        print('T-minus', n)
        yield              # Pause execution
        n -= 1

# Example task 2: Count up
def countup(n):
    x = 0
    while x < n:
        print('Up we go', x)
        yield              # Pause execution
        x += 1
```

では、このタスクスケジューラーがどのように動作するかを解説しましょう。

1. ジェネレータータスクを格納するために `deque`（両端キュー）を使用しています。`deque` は、両端から要素を効率的に追加および削除できるデータ構造です。タスクを末尾に追加し、先頭から削除する必要があるため、タスクキューに最適な選択です。
2. `run()` 関数はタスクスケジューラーの核心部分です。キューからタスクを 1 つずつ取り出します。
   - `send(None)` を使用して各タスクを再開します。これは、ジェネレーターに対して `next()` を使用するのと似ています。ジェネレーターに中断したところから実行を続けるように指示します。
   - タスクが値を生成（yield）した後、キューの末尾に戻されます。これにより、タスクは後で再度実行される機会を得ます。
   - タスクが完了すると（`StopIteration` を発生させる）、キューから削除されます。これは、タスクの実行が終了したことを示します。
3. ジェネレータータスク内の各 `yield` 文は一時停止点として機能します。ジェネレーターが `yield` 文に到達すると、実行を一時停止し、制御をスケジューラーに戻します。これにより、他のタスクが実行できるようになります。

このアプローチは協調的なマルチタスク処理を実装しています。各タスクは自発的に制御をスケジューラーに戻し、他のタスクが実行できるようにします。これにより、複数のタスクが実行時間を共有し、同時に実行できるようになります。
