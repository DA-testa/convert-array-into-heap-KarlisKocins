# python3


def build_heap(data):
    def sift_down(i):
        nonlocal swaps
        min_index = i
        left_child = 2 * i + 1
        right_child = 2 * i + 2

        if left_child < n and data[left_child] < data[min_index]:
            min_index = left_child

        if right_child < n and data[right_child] < data[min_index]:
            min_index = right_child

        if i != min_index:
            swaps.append((i, min_index))
            data[i], data[min_index] = data[min_index], data[i]
            sift_down(min_index)

    swaps = []
    n = len(data)
    for i in range(n // 2 - 1, -1, -1):
        sift_down(i)

    return swaps


def main():

    ievade = input("I or F: ")
    if "I" in ievade:
        n = int(input("Enter count: "))
        data = list(map(int, input("Enter the numbers: ").split()))

    # checks if lenght of data is the same as the said lenght
    elif "F" in ievade:

        filename = input("File name: ")
        with open("tests/"+filename, 'r') as f:
            n = int(f.readline())
            data = list(map(int, f.readline().split()))

    assert len(data) == n

    swaps = build_heap(data)

    print("Result:")
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
