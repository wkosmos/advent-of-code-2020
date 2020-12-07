

'''Find the two entries that sum to 2020 and then multiply those two numbers together.

For example, suppose your expense report contained the following:

[1721, 979, 366, 299, 675, 1456]

The two entries that sum to 2020 are 1721 and 299. Multiplying them together produces 1721 * 299 = 514579, so the correct answer is 514579.
'''
with open('data/day1-report-repair-input.txt') as f:
    lines = f.read().split('\n')
    input = [int(lines[i]) for i in range(0, len(lines))]

# gross
def report_repair(report_list):
    for i in report_list:
        for j in report_list:
            if i + j == 2020:
                return i * j
            else:
                pass

# sorry mr a. complexity you seem to be gaining some weight
def report_repair_repair(report_list):
    for i in report_list:
        for j in report_list:
            for k in report_list:
                if i + j + k == 2020:
                    return i * j * k
                else:
                    pass


if __name__ == '__main__':
    print(report_repair(input))
    print(report_repair_repair(input))

