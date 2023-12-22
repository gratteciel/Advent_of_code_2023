

def main():

    f = open("input.txt", "r")
    red_max = 12
    blue_max = 13
    green_max = 14
    sum  = 0


    for line in f:
        red = 0
        blue = 0
        green = 0
        words = line.split()

        #line number
        line_number = words[1]
        line_number = line_number.replace(":", "")

        for i in range(len(words)):
            #print(words[i])
            if words[i] == "red":
                print(words[i-1])
                red = int(words[i-1]) + red
            if words[i] == "blue":
                blue = int(words[i-1]) + blue
                #print("on line" + line_number + "equals to " + str(blue))
            if words[i] == "green":
                green = int(words[i-1]) + green

        if red > red_max and blue > blue_max and green > green_max:
            sum += line_number

    print(sum)






if __name__ == "__main__":
    main()