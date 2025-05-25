# 애니메이션 생성

마지막으로, FuncAnimation 객체를 사용하여 애니메이션을 생성합니다. 이 때 figure, update 함수, 프레임 간 간격 (밀리초) 및 저장할 프레임 수를 전달합니다.

```python
animation = FuncAnimation(fig, update, interval=10, save_count=100)
plt.show()
```
