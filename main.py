import re


def regex_string(string: str, pattern: str = "", exact: bool = False) -> str:
    if not pattern:
        return re.sub(r"^\s+|\s+$", "", string)

    # Preventing special characters from breaking regex.
    escaped = re.escape(pattern)

    if not exact:
        return re.sub(fr"^[{escaped}]+|[{escaped}]+$", "", string)
    return re.sub(fr"^({escaped})+|({escaped})+$", "", string)


ex1 = "     hello   "
ex2 = "*****hello   *"
ex3 = "  ***___hello ***____"
ex4 = "==00==00= hello ==00"

print(f"Before: |{ex1}| \nAfter: |{regex_string(ex1)}|\n")
print(f"Before: |{ex2}| \nAfter: |{regex_string(ex2, "*")}|\n")
print(f"Before: |{ex3}| \nAfter: |{regex_string(ex3, "_")}|\n")
print(f"Before: |{ex4}| \nAfter: |{regex_string(ex4, "==00")}|\n")
print(f"Before: |{ex4}| \nAfter: |{regex_string(ex4, "==00", True)}|\n")
