def display_main_menu():
    print("Enter some numbers seperated by commas (eg. 5,67,32)")


def get_user_input():
    x=input()
    x=x.split(",") #split the entered string in to a list on strings based on commas
    float_list =[]
    for num_list in x:
        float_list.append(float(num_list))  # remember to convert num_str to float

    return float_list

def calc_average_temperature(num_list):
    total = sum(num_list)
    average = total / len(num_list)

    return average

def calc_min_max_temperature(num_list):
    min_num = min(num_list)
    max_num = max(num_list)

    return [min_num, max_num]



def main():
    print("ET0735(DevOps for AIoT)-Lab2-Introduction to Python")
    display_main_menu()
    num_list = get_user_input()
    average=calc_average_temperature(num_list)
    min_max=calc_min_max_temperature(num_list)
    print("average =" + str(average))
    print("min ="+ str(min_max[0]), "max=" + str(min_max[1]))

if __name__=="__main__":
    main()

