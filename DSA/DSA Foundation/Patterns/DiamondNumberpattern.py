n = int(input())

nst = 1
nsp = n // 2

val = 1
for i in range(1, n + 1):
    print("  " * nsp, end="")

    if i <= n // 2:
        val = i
    else:
        val = n + 1 - i

    for j in range(nst):
        print(val, end=" ")

        if j < nst // 2:
            val += 1
        else:
            val -= 1

    if i <= n // 2:
        nsp -= 1
        nst += 2
    else:
        nsp += 1
        nst -= 2

    print()
