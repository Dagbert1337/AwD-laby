################## OVERWRITE ######################

with open("file.txt", "w", encoding="utf-8") as f:
    f.write("Created using write mode.\n")
    f.write("Second line.\n")

with open("file.txt", "r", encoding="utf-8") as f:
    print(f.read())

################### APPEND ########################

with open("file.txt", "a", encoding="utf-8") as f:
    f.write("Appended line.\n")

with open("file.txt", "r", encoding="utf-8") as f:
    print(f.read())

################## MULT LINES ####################

lines = ["First line\n", "Second line\n", "Third line\n"]
with open("file1.txt", "w", encoding="utf-8") as f:
    f.writelines(lines)

with open("file1.txt", "r", encoding="utf-8") as f:
    print(f.read())

#### or ####

lines = ["Line A", "Line B", "Line C"]
text = "\n".join(lines) + "\n"
with open("file2.txt", "w", encoding="utf-8") as f:
    f.write(text)

with open("file2.txt", "r", encoding="utf-8") as f:
    print(f.read())

##################################################

