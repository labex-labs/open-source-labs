# リセットボタンを作成する

このステップでは、スライダー用のリセットボタンを作成します。クリックすると、リセットボタンはスライダーの値を初期値にリセットします。

```python
ax_reset = fig.add_axes([0.8, 0.025, 0.1, 0.04])
button = Button(ax_reset, 'Reset', hovercolor='0.975')

def reset(event):
    sfreq.reset()
    samp.reset()
button.on_clicked(reset)
```
