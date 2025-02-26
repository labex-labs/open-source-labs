# ジェネレータの終了

ジェネレータに関する一般的な質問の1つは、その生存期間とガベージコレクションです。たとえば、`follow()` ジェネレータは無限の `while` ループで永久に実行されます。それを駆動する反復処理ループが停止した場合、何が起こりますか？また、ジェネレータを事前に終了させる方法はありますか？

`follow()` 関数を変更して、すべてのコードを次のような `try-except` ブロックに囲みます。

```python
def follow(filename):
    try:
        with open(filename,'r') as f:
            f.seek(0,os.SEEK_END)
            while True:
                 line = f.readline()
                 if line == '':
                     time.sleep(0.1)    # Sleep briefly to avoid busy wait
                     continue
                 yield line
    except GeneratorExit:
        print('Following Done')
```

次に、いくつかの実験を試してみましょう。

```python
>>> from follow import follow
>>> # Experiment: Garbage collection of a running generator
>>> f = follow('stocklog.csv')
>>> next(f)
'"MO",70.29,"6/11/2007","09:30.09",-0.01,70.25,70.30,70.29,365314\n'
>>> del f
Following Done
>>> # Experiment: Closing a generator
>>> f = follow('stocklog.csv')
>>> for line in f:
        print(line,end='')
        if 'IBM' in line:
            f.close()

"VZ",42.91,"6/11/2007","09:34.28",-0.16,42.95,42.91,42.78,210151
"HPQ",45.76,"6/11/2007","09:34.29",0.06,45.80,45.76,45.59,257169
"GM",31.45,"6/11/2007","09:34.31",0.45,31.00,31.50,31.45,582429
...
"IBM",102.86,"6/11/2007","09:34.44",-0.21,102.87,102.86,102.77,147550
Following Done
>>> for line in f:
        print(line, end='')    # No output: generator is done

>>>
```

これらの実験では、ジェネレータがガベージコレクションされる場合、または `close()` メソッドを介して明示的に閉じられる場合に、`GeneratorExit` 例外が発生することがわかります。

さらに検討すべき1つの分野は、forループから抜けた場合にジェネレータの反復処理を再開できるかどうかです。たとえば、次のように試してみましょう。

```python
>>> f = follow('stocklog.csv')
>>> for line in f:
        print(line,end='')
        if 'IBM' in line:
            break

"CAT",78.36,"6/11/2007","09:37.19",-0.16,78.32,78.36,77.99,237714
"VZ",42.99,"6/11/2007","09:37.20",-0.08,42.95,42.99,42.78,268459
...
"IBM",102.91,"6/11/2007","09:37.31",-0.16,102.87,102.91,102.77,190859
>>> # Resume iteration
>>> for line in f:
        print(line,end='')
        if 'IBM' in line:
            break

"AA",39.58,"6/11/2007","09:39.28",-0.08,39.67,39.58,39.31,243159
"HPQ",45.94,"6/11/2007","09:39.29",0.24,45.80,45.94,45.59,408919
...
"IBM",102.95,"6/11/2007","09:39.44",-0.12,102.87,102.95,102.77,225350
>>> del f
Following Done
>>>
```

一般的に、必要に応じて実行中の反復処理を中断して後で再開することができます。ただし、ジェネレータオブジェクトが強制的に閉じられたり、何らかの方法でガベージコレクションされないようにする必要があります。
