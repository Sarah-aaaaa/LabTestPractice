def calculate_bmi(height, weight):
    print("Height=" + str(height)) #str() convert height from int to str
    print("Weight=" + str(weight)) #str() convert height from float to str

    #Add code here to calculate bmi
    bmi = weight/height**2 # weight divided by height to the power of 2

    #Add code here to display calculated bmi
    print(f"bmi={bmi}")

    if bmi <18.5:
        print("Underweight")
        return -1
    elif bmi<= 25.0:
        print("Normal Weight")
        return 0
    else:
        print("Overweight")
        return 1

calculate_bmi(weight=57,height=1.73) #here matches by name



