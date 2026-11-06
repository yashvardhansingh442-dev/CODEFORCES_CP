n = input().strip()

count = sum(1 for d in n if d in "47")

# count must be non-zero and made up only of 4s and 7s
if count > 0 and all(d in "47" for d in str(count)):
    print("YES")
else:
    print("NO")
