# アニメーションを作成する

最後に、`FuncAnimation`クラスを使ってアニメーションを作成できます。アニメーションを作成するために、`fig`、`run`、`data_gen`、`init_func`、および`interval`パラメータを渡します。また、最後の 100 フレームのみが保存されるように、`save_count`パラメータを 100 に設定します。

```python
ani = animation.FuncAnimation(fig, run, data_gen, interval=100, init_func=init,
                              save_count=100)
```
