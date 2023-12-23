import re

def main():

    f = open("input.txt", "r")
    red_max = 12
    blue_max = 14
    green_max = 13
    sum = 0
    for index,x in enumerate(f):
        flag = False

        for y in re.findall(r'\d+ green', x):
            temp = int(re.sub(r' green',"",y))
            if temp > green_max:
                flag = True

        for y in re.findall(r'\d+ blue', x):
            temp = int(re.sub(r' blue',"",y))
            if temp > blue_max:
                flag = True

        for y in re.findall(r'\d+ red', x):
            temp = int(re.sub(r' red',"",y))
            if temp > red_max:
                flag = True

        if flag == False:
            sum += index + 1

    print(sum)






if __name__ == "__main__":
    main()