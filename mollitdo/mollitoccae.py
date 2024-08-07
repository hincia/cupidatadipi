text = "Hello"
width = 10
aligned_text = "{:>10}".format(text)
print(aligned_text)  # Output: "     Hello"

# Using f-strings
aligned_text = f"{text:>{width}}"
print(aligned_text)  # Output: "     Hello"
