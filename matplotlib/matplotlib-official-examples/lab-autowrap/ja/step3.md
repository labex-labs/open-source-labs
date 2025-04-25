# テキストの自動改行

次に、Matplotlib でテキストを自動的に改行する方法を検討しましょう。コードの`plt.text()`行を次のものに置き換えます。

```python
t = ("This is a really long string that I'd rather have wrapped so that it "
     "doesn't go outside of the figure, but if it's long enough it will go "
     "off the top or bottom!")
plt.text(5, 5, t, ha='center', wrap=True)
```

`wrap=True`の引数は、Matplotlib に対してテキストを自動的に改行するように指示します。
