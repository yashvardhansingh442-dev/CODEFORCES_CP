n = input().strip()
count = sum(1 for d in n if d in "47")
print("YES" if count in (4, 7) else "NO")
