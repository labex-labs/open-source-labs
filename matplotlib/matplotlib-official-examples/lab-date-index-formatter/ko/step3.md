# 사용자 정의 인덱스 포맷터 생성

0, 1, ... len(data) 에서 시작하는 인덱스에 대해 데이터를 플로팅하기 위해 사용자 정의 인덱스 포맷터를 생성합니다. 이 포맷터는 눈금 표시를 정수가 아닌 시간으로 형식화합니다.

```python
# Create custom index formatter
fig, ax2 = plt.subplots(figsize=(6, 3))
ax2.plot(r.adj_close, 'o-')

# Format x-axis as times
def format_date(x, _):
    try:
        # convert datetime64 to datetime, and use datetime's strftime:
        return r.date[round(x)].item().strftime('%a')
    except IndexError:
        pass

ax2.set_title("Creating Custom Index Formatter")
ax2.xaxis.set_major_formatter(format_date)  # internally creates FuncFormatter
```
