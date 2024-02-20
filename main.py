from itertools import product


def all_ways_to_attend_class(days):
    """
    This method gives us all the ways in which we can attend classes in a list format.
    Input: days - Int ex: 3,4
    Output: list Example  ['PP', 'PA', 'AP', 'AA'] For day 2
    """
    options = ["P", "A"]
    # P denotes Present and A denotes absent
    # which are the available options for a day
    total_class_options = []
    for option in product(options, repeat=days):
        total_class_options.append("".join(option))
    return total_class_options


def invalid_ways_to_attend_class(total_ways, no_of_days_absent):
    """
    In this method we calculate the total number of invalid ways.
    Input-List of total_ways, no_of_days_absent_allowed
    Example  List of total_ways -List- ['PPP', 'PPA', 'PAP', 'PAA', 'APP', 'APA', 'AAP', 'AAA'],
             no_of_days_absent_allowed - Int- 2
    Output: List :  ['PAA', 'AAP', 'AAA']
    """

    consecutive_day_of_absent = 'A' * no_of_days_absent
    # consecutive_day_of_absent - consist of 'A' string no_of_days_absent_allowed times Example: AA, AAA

    invalid_ways_list = []
    for way in total_ways:
        if consecutive_day_of_absent in way:
            invalid_ways_list.append(way)
    return invalid_ways_list


def graduation_miss_probability(days, consecutive_absences_limit):
    """
    This method will calculate the probability of graduation miss
    Input : no.of days example:- 5, consecutive_absences_limit-Example 4
    """

    if days < 0 or consecutive_absences_limit < 0 or days < consecutive_absences_limit:
        return "Invalid Input"

    all_ways = all_ways_to_attend_class(days)
    ineligible_ways = invalid_ways_to_attend_class(all_ways, consecutive_absences_limit)

    remaining_ways = [way for way in all_ways if way not in ineligible_ways]
    graduation_miss_days = len([sequence for sequence in remaining_ways if sequence[-1] == 'A'])
    count_of_valid_ways = str(len(all_ways) - len(ineligible_ways))

    return f"{str(graduation_miss_days)}/{count_of_valid_ways}"


n = 10  # total no.of class
m = 4  # consecutive absence limit
print(graduation_miss_probability(n, m))
