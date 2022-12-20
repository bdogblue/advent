
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
            if i == 0:
                biggest_number = elves[i]
            else:
                if biggest_number < elves[i]:
                    biggest_number = elves[i]
            
            elves.append(0)
            i += 1

    print("This is the biggest amount of calories that one of the elves is carring is: ", biggest_number)

main()