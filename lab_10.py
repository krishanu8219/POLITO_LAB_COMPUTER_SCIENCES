def read_correct_path(input_file):
    correct_route = []
    with open (input_file, "r") as map_file:
        lines = (map_file.readlines())
        for i in range(len(lines)):
            for j in range(len(lines[i])):
                if lines[j][i] == ".":
                    correct_route.append((i,j))
    return correct_route                

def read_given_path(path_file,correct_route):
    with open(path_file,"r") as file:
        given_path = []
        x , y = correct_route[0]
        for aline in file:
            direction, steps = aline.strip().split()
            if direction == "E":
                y += int(steps)    
            if direction == "W":
                y -= int(steps)    
            if direction == "S":
                x += int(steps)
            if direction == "N":
                x -= int(steps)
            given_path.append((x,y))
        return given_path       


def match_given_path(correct_route, given_path):
    for i in range(len(given_path)):
        if given_path[i] not in correct_route:
            return "Sorry the path is not correct"
        if i > 0 and (abs(given_path[i][0] - given_path[i-1][0]) + abs(given_path[i][1] - given_path[i-1][1]) != 1):
            return "This path is not continuos"
        
    return "Congratulations you found the correct path"


def main():
    correct_route = read_correct_path("map.txt")
    given_path = read_given_path("path.txt", correct_route)
    result = match_given_path(correct_route, given_path)
    print(result)

if __name__ == "__main__":
    main()