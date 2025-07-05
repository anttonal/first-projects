"""
COMP.CS.100 - round 6 - Project: Säätilasto.
Student: Antton Alivuotila
Student number: 151259218
Program, that asks about the weather of a number of days set by the user, calculates the mean and median, makes a group
of values smaller and larger than the median, and compares the values of each group to the mean.
"""


def temp_of_days(num_days):
    """
    Takes an amount of days and assigns a temperature for each one
    :param num_days: int, the total amount of days
    :return: list, returns a list of temperatures on each day
    """
    temps = []
    for day in range(1, num_days+1):
        add_day = float(input(f"Enter day {day}. temperature in Celcius: "))
        temps.append(add_day)
    return temps


def temp_mean(num_days, temps):
    """
    Calculates the median of the given list
    :param num_days: int, the total amount of days
    :param temps: list, list of inputted temperatures
    :return: float, returns the mean
    """
    return sum(temps)/num_days


def temp_median(num_days, temps):
    """
    Calculates the median of the given list
    :param num_days: int, the total amount of days
    :param temps: list, list of inputted temperatures
    :return: float, returns the median
    """
    middle_point = num_days/2
    if num_days % 2 == 0:
        index = int(middle_point)
        return (sorted(temps)[index] + sorted(temps)[index - 1]) / 2
    else:
        index = int(middle_point-0.5)
        return sorted(temps)[index]


def over_at_under_median(mean, median, temps):
    """
    Prints out the temperatures in groups of over and at-, or under the median. Text gets printed in a neat manner.
    :param mean: mean of the temperatures
    :param median: median of the temperatures
    :param temps: list of the temperatures in the same order as the user inputted it.
    """
    print("Over or at median were:")
    for index in range(0, len(temps)):
        if temps[index] >= median:
            print(f"Day{index+1:3}.{temps[index]:6.1f}C difference to mean:{temps[index]-mean:6.1f}C")
        index += 1
    print("")
    print("Under median were:")
    for index in range(0, len(temps)):
        if temps[index] < median:
            print(f"Day{index + 1:3}.{temps[index]:6.1f}C difference to mean:{temps[index] - mean:6.1f}C")
        index += 1


def main():
    num_days = int(input("Enter amount of days: "))
    temps = temp_of_days(num_days)
    mean = temp_mean(num_days, temps)
    median = temp_median(num_days, temps)
    print("")
    print(f"Temperature mean: {mean:.1f}C")
    print(f"Temperature median: {median:.1f}C")
    print("")
    over_at_under_median(mean, median, temps)


if __name__ == "__main__":
    main()
