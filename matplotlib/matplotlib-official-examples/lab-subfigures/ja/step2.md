# サブフィギュア付きの図を作成する

サブフィギュア付きの図を作成するには、まず `plt.figure()` を使って図オブジェクトを作成する必要があります。その後、`fig.subfigures()` を使ってサブフィギュアを作成できます。

```python
fig = plt.figure()
subfigs = fig.subfigures(2, 1)
```

これにより、上下に 2 つのサブフィギュアがある図が作成されます。
