from textwrap import wrap


def wrap_string_into_paragraph():
    S = str(input())
    w = int(input())
    z = list(wrap(S, w))

    for i in z:
        print(i)


wrap_string_into_paragraph()
