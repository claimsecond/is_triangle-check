def is_triangle(a, b, c) -> int:
    if a <= 0 or b <= 0 or c <= 0:
        return 0
    if (a + b > c) and (a + c > b) and (b + c > a):
        return 1
    else:
        return 0


def read_input_from_file(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    return lines


if __name__ == "__main__":
    lines = read_input_from_file("C:\\Users\\claim\\Documents\\Pairwise.txt")
    for line in lines:
        a, b, c = map(int, line.strip().split())
        result = is_triangle(a, b, c)
        print(f"Input: {a} {b} {c} Output: {result}")
