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

def sort_temperature(num_list):
    sort=sorted(num_list)

    return sort

def calc_median_temperature(sort):
    sorted_list=sort
    length=len(sort)

    if length % 2 == 0:
        mid1 = length //2 -1 # index
        mid2 = length //2 #index
        median = (sort[mid2] -sort[mid1])/2

    else :
        mid = length //2 # index
        median = sort[mid]

    return median





def main():
    print("ET0735(DevOps for AIoT)-Lab2-Introduction to Python")
    display_main_menu()
    num_list = get_user_input()
    average=calc_average_temperature(num_list)
    min_max=calc_min_max_temperature(num_list)
    sort = sort_temperature(num_list)
    median = calc_median_temperature(sort)
    print(sort)
    print("average =" + str(average))
    print("min ="+ str(min_max[0]), "max=" + str(min_max[1]))
    print(median)


if __name__=="__main__":
    main()

