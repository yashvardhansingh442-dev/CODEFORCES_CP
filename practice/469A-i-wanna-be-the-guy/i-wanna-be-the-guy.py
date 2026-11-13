n = int(input())

p = list(map(int, input().split()))
x = p[0]
little_x = set(p[1:])

q = list(map(int, input().split()))
y = q[0]
little_y = set(q[1:])

levels = little_x | little_y

if len(levels) == n:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")
