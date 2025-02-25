# ラベルを追加してレイアウトを調整する

matplotlib.pyplotのtitle、xlabel、およびylabel関数を使って、サブプロットにタイトルと軸ラベルを追加します。tight_layout関数を使ってサブプロットのレイアウトを調整します。

```python
axs[0].set_title('Cosine with Radian X-Axis')
axs[0].set_xlabel('Radians')
axs[0].set_ylabel('Cosine')
axs[1].set_title('Cosine with Degree X-Axis')
axs[1].set_xlabel('Degrees')
axs[1].set_ylabel('Cosine')
fig.tight_layout()
```
