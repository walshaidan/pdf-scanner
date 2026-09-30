def write_table(table,output):
    longest = 0
    answer_list = []

    for row in table:
        for cell in row:
            if cell is not None:
                longest = max(longest, len(cell))


    i = 0
    while i < len(table):
        k = 0
        line = ""
        while k < len(table[i]):
            line += "|" + "-" * (longest + 1)
            k += 1
        line += "|"
        answer_list.append(line)

        j = 0
        line = ""
        while j < len(table[i]):
            line += "|" + table[i][j] + " " * (longest + 1 - len(table[i][j]))
            j += 1
        line += "|"
        answer_list.append(line)
        i += 1

    k = 0
    line = ""
    while k < len(table[0]):
        line += "|" + "-" * (longest + 1)
        k += 1
    line += "|"
    answer_list.append(line + "\n")


    output.write("\n".join(answer_list).encode("utf8"))