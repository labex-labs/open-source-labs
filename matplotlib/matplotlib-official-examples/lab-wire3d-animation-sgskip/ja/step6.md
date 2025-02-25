# 平均 FPS を表示する

6 番目のステップは、アニメーションを実行するのにかかった合計時間を使って、平均 1 秒当たりのフレーム数 (FPS) を表示することです。

```python
print('Average FPS: %f' % (100 / (time.time() - tstart)))
```
