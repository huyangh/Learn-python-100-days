def bubbleSort(list):
    for i in range(len(list) - 1):
        for j in range(len(list) - i - 1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]


def main():
    list1 = [2, 5, 6, 98, 34, 56, 90, 102, 23, 234, 3, 11]
    bubbleSort(list1)
    print(list1)


if __name__ == "__main__":
    main()