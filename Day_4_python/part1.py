import re

sum = 0

with open('input.txt') as f:
    lines = f.readlines()

    for index, x in enumerate(lines):
        count = 0
        part_sum = 0
        array = x.split("|")
        # delte card number to have just winning numbers
        for i in range(len(array[0])):
            if (array[0][i] == ":"):
                array[0] = array[0][i + 1:]
                array[0] = array[0].split()
                print(array[0])
                break
        # We have array[0] = winning numbers
        # We have array[1] = ticket numbers
        array[1] = array[1].split()
        print(array[1])

        for i in range(len(array[1])):
            if array[1][i] in array[0]:
                count += 1
                part_sum = 2 ** (count-1)

        sum += part_sum
        print("At the index " + str(index) + " the sum is " + str(sum) + " and the part sum is " + str(part_sum))



print("Final sum: " + str(sum))
