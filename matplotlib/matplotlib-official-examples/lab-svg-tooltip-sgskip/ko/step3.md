# 그림을 SVG 로 저장

`BytesIO` 클래스와 `savefig` 메서드를 사용하여 가짜 파일 객체에 그림을 저장합니다.

```python
ax.set_xlim(-30, 30)
ax.set_ylim(-30, 30)
ax.set_aspect('equal')

f = BytesIO()
plt.savefig(f, format="svg")
```
