def largest_second_element_tuples(tuples_list):
    # return an empty list if the input list is empty
    if not tuples_list:
        return []
    
    # initialize max_value with the second element of the first tuple
    max_value = tuples_list[0][1]
    # initialize result list with the first tuple
    result = [tuples_list[0]]
    
    # iterate through the rest of the list
    for tup in tuples_list[1:]:
        # if the current tuple's second element is greater than max_value,
        # update max_value and start a new result list with this tuple
        if tup[1] > max_value:
            max_value = tup[1]
            result = [tup]
        # if the current tuple's second element equals max_value,
        # add it to the result list
        elif tup[1] == max_value:
            result.append(tup)
    
    # return all tuples with the highest second element
    return result


def main():
    # example list of tuples
    sample_tuples = [(1, 3), (4, 1), (2, 2), (5, 3)]

    result = largest_second_element_tuples(sample_tuples)
    print("Tuples with the largest second element:", result)

if __name__ == "__main__":
    main()