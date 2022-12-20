
def main():
    elves = [0]
    i = 0
    infile = open('input.txt', 'r')

    calories_list = infile.read()

    infile.close()
    
    for line in calories_list.splitlines():
        if line != '':
            elves[i] += int(line)
        else:
            elves.append(0)
            i += 1

    elves.sort(reverse=True)

    print("This is the biggest amount of calories that the top three elves are carring is: ", (elves[0]+elves[1]+elves[2]))

main()