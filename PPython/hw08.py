import copy

def count_votes(csvfile,candidate):
    '''
    Purpose:
        The purpose of the function is to load in one a vote files and return a
        list containing the counts of first, second, and third-place votes for
        the given candidate
    Parameter(s):
        csvfile: file which contains the votes from simulated voters, in the
        format "number,name1,name2,name3"
        candidate: The name to be checked for counts of second, and third-place
        votes
    Return Value:
        ls: A list containing the counts of first, second, and third-place votes for
        the given candidate
    '''

    try:
        ls1= []
        number1 = 0
        ls2= []
        number2 = 0
        ls3= []
        number3 = 0
        final=[]
        fp = open(csvfile)
        fp2 = fp.readlines()
        fp2.pop(0)
        for i in fp2:
            u = i.strip().split(',')
            for j in range(len(u)):
                if j == 1:
                    ls1.append(u[1])
                if j == 2:
                    ls2.append(u[2])
                if j == 3:
                    ls3.append(u[3])
        for i in ls1:
            if i == candidate:
                number1 +=1
        for i in ls2:
            if i == candidate:
                number2 +=1
        for i in ls3:
            if i == candidate:
                number3 +=1
        final.append(number1)
        final.append(number2)
        final.append(number3)
        fp.close()
        return final
    except FileNotFoundError:
        return

def remove_candidate(csvfilein,csvfileout,candidate):
    '''
    Purpose: To remove a particular candidate from contention by removing their
    name from any votes and to return the number of votes that were affected. It
    will also create a new csv file that includes the same column headers as the
    original file but with the new votes after removal
    Parameter(s):
        csvfilein: File which contains the votes from simulated voters, in the
        format "number,name1,name2,name3"
        csvfileout: A new csv file that includes the same column headers as the
        original file but with the new votes after removal
        candidate: The name of the candidate to be removed from contention
    Return Value:
        count: The number of votes that were affected.
    '''
    ls = []
    fp = open(csvfilein)
    fp1 = open(csvfileout,'w')
    fp3 = fp.readlines()
    for i in fp3:
        u = i.strip().split(',')
        ls.append(u)
    count = 0
    for j in range(len(ls)):
        if candidate in ls[j]:
            count += 1
            ls[j].remove(candidate)
        if len(ls[j]) == 1:
            ls.remove(ls[j])
    for row in ls:
        for k in row:
            if k != row[-1]:
                fp1.write(str(k)+',')
            else:
                fp1.write(str(k))
        fp1.write('\n')

    fp.close()
    fp1.close()
    return count

def ranked_choice_full(csvfile, candidate_list):
    '''
    Purpose: To take  a csvfile name and a list of candidate names as parameters.
    The function will check each name of the list of candidates in the csvfile
    and check if any of them have more than 50% of the votes to be consider
    winner. If that is not true, the function will remove the candidate in the
    csvfile that has the least amount of votes and then check for 50% of the
    votes again. This will be continued until someone is chosen as the winner of
    the election.
    Parameter(s):
        csvfile: A csv file containing the votes of simulated voters in a
        simulated election
        candidate_list: The list of candidates to be checked for a winner of the
        election
    Return Value:
        winner: The winner of the election. the person that had 50% of the total
        votes
    '''

    fpnew = open(csvfile)
    fp2 = fpnew.readlines()
    counted_votes = len(fp2)
    fifty = (len(fp2)-1)/2
    for rounds in range(counted_votes):
        for i in candidate_list:
            x = count_votes(csvfile,i)
            if x[0] > fifty:
                winner = i
                return winner
            else:
                for j in candidate_list:
                    total_votes = len(fp2)
                    votes = count_votes(csvfile,j)
                    total_votes = votes[0]
                    if total_votes < counted_votes:
                        counted_votes = total_votes
                        store = j

        csvfileout = 'new_file'
        remove_candidate(csvfile,csvfileout,store)
        csvfile = csvfileout
    fpnew.close()
