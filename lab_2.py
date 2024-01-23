from math import sqrt
def main():

#Part 1 

    edge_length = int(input("Enter the length of the edge of your Platonic solids "))
    if edge_length <0:
        print("Please enter non negative number")
    else:
        volume_Tetrahedron = sqrt(2)/12 * (edge_length)**3
        volume_Cube = (edge_length)**3
        volume_Octahedron = sqrt(2)/3 * (edge_length)**3
        volume_Dodecahedron = 1/4 * (15 + 7*sqrt(5)) * (edge_length)**3
        volume_Icosahedron = 5/12 * (3 + sqrt(5)) * (edge_length)**3
        print(f"Shape : Tetrahedron, edge_length = {edge_length}, volume = {volume_Tetrahedron} meter cube")
        print(f"Shape : Cube, edge_length = {edge_length}, volume = {volume_Cube} meter cube")
        print(f"Shape : Octahedron, edge_length = {edge_length}, volume = {volume_Octahedron} meter cube")
        print(f"Shape : Dodecahedron, edge_length = {edge_length}, volume = {volume_Dodecahedron} meter cube")
        print(f"Shape : Icosahedron, edge_length = {edge_length}, volume = {volume_Icosahedron} meter cube")

#Part 2
        
    a = "Exercise for evaluation"
    odd_concatenation = ""
    even_concatenation = ""
    for i in range(len(a)):
        if i % 2 == 0:
            odd_concatenation += a[i]
        else:
            even_concatenation += a[i]

    print(f"\n \nOdd Concatenation = {odd_concatenation},\nEven Concatenation = {even_concatenation}")



if __name__ == "__main__":
    main()