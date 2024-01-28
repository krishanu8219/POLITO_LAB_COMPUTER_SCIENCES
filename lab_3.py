def main():  
    real_value = float(input("Enter a real value "))

    # Absolute value
    if real_value < 0:
        absolute_value = -real_value
    else:
        absolute_value = real_value

    # Floor value
    if real_value >= 0:
        floor_value = int(real_value)
    else:
        if real_value == int(real_value):
            floor_value = int(real_value)
        else:
            floor_value = int(real_value) - 1

    # Ceiling value
    if real_value <= 0:
        ceiling_value = int(real_value)
    else:
        if real_value == int(real_value):
            ceiling_value = int(real_value)
        else:
            ceiling_value = int(real_value) + 1

    # Round value
    if real_value >= 0:
        if real_value - int(real_value) >= 0.5:
            round_value = int(real_value) + 1
        else:
            round_value = int(real_value)
    else:
        # Implementing absolute value manually for the fractional part
        fractional_part = real_value - int(real_value)
        if fractional_part < 0:
            fractional_part = -fractional_part

        if fractional_part >= 0.5:
            round_value = int(real_value) - 1
        else:
            round_value = int(real_value)

            

    print(f"Absolute value is {absolute_value} \nFloor Value is {floor_value} \nCeiling Value is {ceiling_value} \nRound Value is {round_value} ")

if __name__  == "__main__":
        main()