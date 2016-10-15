# Set formatter to accept four parameters
formatter = "%r %r %r %r"

# Print parameters
print formatter % (1, 2 ,3 ,4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
# Print parameters which are parameters
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)
