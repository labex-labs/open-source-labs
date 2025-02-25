# 工学表記を使って目盛りにラベルを付ける

次に、x 軸の目盛りに工学表記を使ってラベルを付けます。最初のサブプロットではデフォルト設定を使用し、2 番目のサブプロットでは `places` と `sep` オプションを使って小数点以下の桁数と数値と接頭辞/単位の間の区切り文字を指定します。

```python
# Demo of the default settings, with a user-defined unit label.
ax0.set_title('Full unit ticklabels, w/ default precision & space separator')
formatter0 = EngFormatter(unit='Hz')
ax0.xaxis.set_major_formatter(formatter0)
ax0.plot(xs, ys)
ax0.set_xlabel('Frequency')

# Demo of the options `places` (number of digit after decimal point) and
# `sep` (separator between the number and the prefix/unit).
ax1.set_title('SI-prefix only ticklabels, 1-digit precision & '
              'thin space separator')
formatter1 = EngFormatter(places=1, sep="\N{THIN SPACE}")  # U+2009
ax1.xaxis.set_major_formatter(formatter1)
ax1.plot(xs, ys)
ax1.set_xlabel('Frequency [Hz]')
```
