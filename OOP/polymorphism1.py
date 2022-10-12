def jog(a, b, c="", d=""):
    # input(f"Enter value/string for c and d: {c} {d}")
    return a + b * c * d


print(jog(1, 2))

print(jog(1, 2, "1"))

print(jog(1, 2, "1", "2"))
