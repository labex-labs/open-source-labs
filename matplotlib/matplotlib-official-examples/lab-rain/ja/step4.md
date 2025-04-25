# 更新関数を作成する

更新関数は、FuncAnimation オブジェクトによって呼び出され、アニメーションの間に散布図を更新します。

```python
def update(frame_number):
    # 最古い雨滴を再生成するために使用できるインデックスを取得します。
    current_index = frame_number % n_drops

    # 時間の経過とともにすべての色をより透明にします。
    rain_drops['color'][:, 3] -= 1.0/len(rain_drops)
    rain_drops['color'][:, 3] = np.clip(rain_drops['color'][:, 3], 0, 1)

    # すべての円を大きくします。
    rain_drops['size'] += rain_drops['growth']

    # 最古い雨滴の新しい位置を選択し、そのサイズ、色、成長係数をリセットします。
    rain_drops['position'][current_index] = np.random.uniform(0, 1, 2)
    rain_drops['size'][current_index] = 5
    rain_drops['color'][current_index] = (0, 0, 0, 1)
    rain_drops['growth'][current_index] = np.random.uniform(50, 200)

    # 新しい色、サイズ、位置で散布コレクションを更新します。
    scat.set_edgecolors(rain_drops['color'])
    scat.set_sizes(rain_drops['size'])
    scat.set_offsets(rain_drops['position'])
```
