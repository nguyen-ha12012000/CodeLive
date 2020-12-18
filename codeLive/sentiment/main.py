def score_word():
    search_word = str((input()).lower())
    training_file = open("training.txt")
    # store names of film
    count_char = []
    # return a list containing each line in the file
    f = training_file.readline()

    # back to the first line of file to read
    training_file.seek(0)

    #count the times appearance of each char
    count_char = (training_file.readline()).strip().split()
    # count_char = ''.join(list(list(dict.fromkeys(training_file))))
    print(count_char)

    value = 0;
    for i in enumerate(count_char):
        value = count_char.count(i)
        if i == search_word:
            value += 1
    print(dict.fromkeys(count_char, value))

def average_score():
    training_file = open("training.txt")

    #store average score of each film
    score_file = []

    # return a list containing each line in the file
    f = (training_file.readline()).strip().split()
    print(f)

    print("Do you want to continue? Yes/No: ")
    choice = str(input())
    if choice == "No":
        highest_lowest_score()
    elif choice == "Yes":
        break


def highest_lowest_score():
    #highest scores
    highest_sorted = sorted(score_file, reverse=True)
    print(highest_score = highest_sorted[0])

    #lowest score
    lowest_sorted = sorted(score_file)
    print(lowest_score = lowest_sorted[0])

def sort_score():
    # highest scores
    highest_sorted = sorted(score_file, reverse=True)

    #lowest score
    lowest_sorted = sorted(score_file)
    print(lowest_score = lowest_sorted[0])

def main():
    while True:
        choice = str(input("Learning data file name? "
                           "\nWhat would you like to do?"
                           "\n1: Get the score of word"
                           "\n2: Get the average score of words in the file"
                           "\n3: Find the highest/lowest scoring words in a file"
                           "\n4: Sort the words into positive.txt and negative.txt"
                           "\n5: Exit the program"
                           "\nEnter a number 1 – 5:\t"))
        if choice == "1":
            score_word()
        elif choice == "2":
            average_score()
        elif choice == "3":
            highest_lowest_score()
        elif choice == "4":
            sort_score()
        elif choice == "5":
            break
main()