# 수평 막대 차트 레이블 지정

다음으로, `bar_label` 함수를 사용하여 수평 막대 차트를 만들고 레이블을 지정합니다. 이전 단계의 데이터를 사용하지만, 이번에는 각 사람에 대한 임의의 성능 데이터를 생성합니다.

```python
people = ('Tom', 'Dick', 'Harry', 'Slim', 'Jim')
y_pos = np.arange(len(people))
performance = 3 + 10 * np.random.rand(len(people))
error = np.random.rand(len(people))

fig, ax = plt.subplots()

hbars = ax.barh(y_pos, performance, xerr=error, align='center')
ax.set_yticks(y_pos, labels=people)
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_xlabel('Performance')
ax.set_title('How fast do you want to go today?')

# Label with specially formatted floats
ax.bar_label(hbars, fmt='%.2f')
ax.set_xlim(right=15)  # adjust xlim to fit labels

plt.show()
```
