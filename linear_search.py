def linear_search(list, targetValue):

    for i in range(len(list)):
        if (targetValue == list[i]):
            return i
    return "not found"


def main():

    # Example
    exampleList = [1, 2, 3, 4, 5, 6, 7, 9]
    exampleTarget = 8
    result = linear_search(exampleList, exampleTarget)

    if (result == "Not Found"):
        print("Your value", exampleTarget, "was", result)

    else:
        print("Your value", exampleTarget, "was found at list index", result)

if __name__ == "__main__":
    main()