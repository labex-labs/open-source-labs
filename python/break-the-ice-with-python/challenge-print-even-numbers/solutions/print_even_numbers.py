def even_generator(n):
    i = 0
    while i <= n:
        if i % 2 == 0:
            yield i
        i += 1


n = int(input())
values = []
for i in even_generator(n):
    values.append(str(i))

print(",".join(values))
