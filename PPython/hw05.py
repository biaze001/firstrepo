def pair_sum(num_list, target):
    '''
    Purpose:
        To take a list of unique integers and a target number in order to count
        the number of pairs of distinct numbers from the list that sum to the
        given target
    Parameter(s):
        num_list: list of unique integers to be tested
        target: the target sum for each pair
    Return Value:
        count: a count of the number of pairs of distinct numbers from the list
        that sum to the given target
    '''

    count = 0
    for b in range(0, len(num_list)):
        for j in range(b+1,len(num_list)):
            if (num_list[j] + num_list[b]) == target:
                count += 1
    return count

def similarity_measure(survey1, survey2):
    '''
    Purpose:
        To take 2 lists and to find the percentage of exact matches between
        this 2 lists, response by response
    Parameter(s):
        survey1: first list of responses
        survey2: second list of resposes
    Return Value:
        pc: percentage of responses that are exact matches in the lists
    '''

    count = 0
    if len(survey1) == len(survey2):
        for i in range(0, len(survey1)):
            if survey1[i] == survey2[i]:
                count += 1
        pc = count/int(len(survey1))
    else:
        pc = float(0)
    return pc

def similarity_report(survey_list, threshold):
    '''
    Purpose:
        To take a list of survey responses and compare the lists among
        themselves and create a new list containing all pairs of surveys whose
        similarity measure is above the given threshold
    Parameter(s):
        survey_list: list containing lists with the survey responses
        threshold: the percent similarity to be used to compare the lists
    Return Value:
        new_list: a list containing all pairs of surveys whose similarity
        measure is above the given threshold
    '''
    new_list = []
    for b in range(0,len(survey_list)):
        for j in range(b+1, len(survey_list)):
            if similarity_measure(survey_list[b], survey_list[j]) >= threshold:
                holding_values = [survey_list[b], survey_list[j]]
                new_list.append(holding_values)
    return new_list
