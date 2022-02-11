def complement(dna):
    '''
    Purpose:
        To take a string containing a dna strand as its argument and
    returns the complement of that strand, using upper-case letters for its
    sequence.
    Parameter(s):
        dna: A string containing a single strand of dna to be used in order
        to find its complement strand.
    Return Value:
        new_base: The complement single strand dna of the dna given to the
        function.
    '''
    new_base = ''
    for ch in dna:
        if ch == 'C':
            new_base += 'G'
        if ch == 'G':
            new_base += 'C'
        if ch == 'A':
            new_base += 'T'
        if ch == 'T':
            new_base += 'A'
    return new_base
    #TODO - Fill out the documentation and write this function


def longest_common(first, second):
    '''
    Purpose:
        To take two DNA sequences and return the longest common substring
        within the two sequences.
    Parameter(s):
        first: DNA string number 1, to be compared with the second DNA string
        in order to find the longest common substring.
        second: DNA string number 2, to be compared with the first DNA string
        in order to find the longest common substring.
    Return Value:
        longest: The longest common substring when comparing DNA string number
        1 and DNA string number 2
    '''
    longest = ''
    for i in range(len(first)):
        for j in range(i, len(first)+1):
            if first[i:j] in second:
                if len(first[i:j]) > len(longest):
                    longest = first[i:j]
    return longest
    #TODO - Fill out the documentation and write this function


def spam_score(spam_file, not_file, word):
    '''
    Purpose:
        To check if a given word is a spam by counting how many times it appears
        in a file containing spam words and how many times it appears in a file
        containing non spam words and taking their difference.
    Parameter(s):
        spam_file: File containing spam emails
        not_file: File containing emails that are not spam
        word: Word to be used when comparing against the two file emails
    Return Value:
        number: number represents the spam score, The spam score is an integer
        representing the total number of times the target word occurs across all
         the spam emails, minus the total number of times the word occurs in
         not-spam emails.
    '''
    fp_spam = open(spam_file)
    spam = fp_spam.readlines()
    spam = [line.strip() for line in spam]
    fp_spam.close()
    fp_not = open(not_file)
    not_spam = fp_not.readlines()
    not_spam = [line.strip() for line in not_spam]
    fp_not.close()

    number = 0
    new_spam = ''
    for i in spam:
        new_spam = new_spam + i + ' '

    new_not_spam = ''
    for j in not_spam:
        new_not_spam = new_not_spam + j + ' '

    new_spam = new_spam.lower()
    new_not_spam = new_not_spam.lower()
    new_spam = new_spam.split()
    new_not_spam = new_not_spam.split()

    spam_times = 0
    for a in new_spam:
        if a == word:
            spam_times += 1

    not_spam_times = 0
    for b in new_not_spam:
        if b == word:
            not_spam_times += 1

    number = spam_times - not_spam_times
    return number
    #TODO - Fill out the documentation and finish this function


def spam_check(spam_file, not_file, email):
    '''
    Purpose:
        To take in an entire email and return the boolean value True if it is a
        spam and the boolean value False if it is not a spam.
    Parameter(s):
        spam_file: File containing spam emails
        not_file: File containing emails that are not spam
        Email: Email to be used when comparing against the two file emails
    Return Value:
        positive: positive will be the boolean value True if the email is a spam
        and False if the email is not n spam
    '''
    score = 0
    email_words = email.split()
    for i in email_words:
        i = i.lower()
        count_spam = spam_score(spam_file, not_file, i)
        score += count_spam

    if score > 0:
        positive = True
    else:
        positive = False

    return positive
    #TODO - Fill out the documentation and write this function
