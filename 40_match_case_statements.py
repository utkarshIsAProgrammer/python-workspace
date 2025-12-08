# match case statements


def describe_day(day):
    match day.lower():
        case "monday":
            print("Start of the work week.")
        case "tuesday":
            print("Second day of the week.")
        case "wednesday":
            print("Midweek!")
        case "thursday":
            print("Almost weekend.")
        case "friday":
            print("Last day of the work week.")
        case "saturday":
            print("Weekend begins!")
        case "sunday":
            print("Rest day.")
        case _:
            print("Invalid day.")


describe_day("Monday")
describe_day("Friday")
describe_day("Holiday")
