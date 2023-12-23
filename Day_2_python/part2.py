import re


def main():
    f = open("input.txt", "r")

    sum = 0
    for index, x in enumerate(f):
        red_max = 0
        blue_max = 0
        green_max = 0

        for y in re.findall(r'\d+ green', x):
            temp = int(re.sub(r' green', "", y))
            if temp > green_max:
                green_max = temp

        for y in re.findall(r'\d+ blue', x):
            temp = int(re.sub(r' blue', "", y))
            if temp > blue_max:
                blue_max = temp

        for y in re.findall(r'\d+ red', x):
            temp = int(re.sub(r' red', "", y))
            if temp > red_max:
                red_max = temp

        sum += red_max * blue_max * green_max

    print(sum)


if __name__ == "__main__":
    main()