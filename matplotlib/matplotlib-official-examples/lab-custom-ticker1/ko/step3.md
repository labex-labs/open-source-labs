# 플롯 생성

이제 사용자 정의 눈금 표시기를 사용하여 플롯을 생성할 수 있습니다. 샘플 데이터를 사용하여 막대 차트를 생성하고 y 축 눈금 표시기가 사용자 정의 눈금 표시기 함수를 사용하도록 설정합니다.

```python
# Create a bar chart with sample data
fig, ax = plt.subplots()
money = [1.5e5, 2.5e6, 5.5e6, 2.0e7]
ax.bar(['Bill', 'Fred', 'Mary', 'Sue'], money)

# Set the y-axis ticker to use the custom ticker function
ax.yaxis.set_major_formatter(ticker.FuncFormatter(millions))

# Display the plot
plt.show()
```
