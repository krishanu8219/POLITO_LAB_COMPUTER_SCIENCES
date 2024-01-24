def main():  
    real_value = float(input("Enter a real value"))
    if real_value < 0:
        absolute_value = -int(real_value)
        floor_value = int(real_value) -1
        ceiling_value = int(real_value)
    elif real_value >= 0:
        absolute_value = int(real_value)
        floor_value = int(real_value)
        if real_value != 0:
            ceiling_value = int(real_value) + 1
        else:
             ceiling_value = 0     
    if real_value - int(real_value) >= 0.5:
        round_value = int(real_value) + 1
    elif real_value - int(real_value) <= 0.5:
        round_value = int(real_value)     

    print(f"Absolute value is {absolute_value} \nFloor Value is {floor_value} \nCeiling Value is {ceiling_value} \nRound Value is {round_value} ")

if __name__  == "__main__":
        main()