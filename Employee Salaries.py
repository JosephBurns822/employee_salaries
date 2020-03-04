'''
Exam 1
Joseph Burns
2/19/2020
Employee Salaries
Description - The main focus of the program is to be able to open a file of employee salaries. Then from there, the
program will read the data within the file and move it into an empty array. It will perform various
functions to perform arithmatic according to the labels. This program must be able to find the specific
file that is listed within the open method.
'''

# Let's begin by defining main function
def main():
    # We will declare our variable as an empty list to add all the data
    salaryList = []
    # This is where the file is opened with a with/as statement
    with open('EmployeeSalaries.txt') as openedFile:
        # The contents are read from the file
        contents = openedFile.readlines()
        # This for loop will append the contents to the list while also
        # stripping the next line characters
        for addToList in contents:
            salaryList.append(addToList.strip('\n'))
        # This for loop converts all of the data from the file to integers
        # from strings
        for intLoop in range(0, len(salaryList)):
            salaryList[intLoop] = int(salaryList[intLoop])
    # Let's print all the juicy data we need for the program by passing the list
    # into the functions below to return the values we need accordingly.
    print("The lowest employee salary made is: $"+str(format(lowestInList(salaryList),'.2f')))
    print("The highest employee salary made is: $"+str(format(highestInList(salaryList),'.2f')))
    print("The total of all employee salaries made is: $"+str(format(totalList(salaryList),'.2f')))
    print("The average of all employee salaries is: $"+str(format(averageList(salaryList),'.2f')))
    

# Every function below is all basic arithmetic to get the values of the
# according function. We would be able to use these functions anytime to get
# the value needed for any purpose.
def lowestInList(listLowest):
    lowestOfSalaries = min(listLowest)
    return lowestOfSalaries
def highestInList(listHighest):
    highestOfSalaries = max(listHighest)
    return highestOfSalaries
def totalList(listTotal):
    totalOfSalaries = sum(listTotal)
    return totalOfSalaries
def averageList(listAverage):
    averageOfSalaries = sum(listAverage) / len(listAverage)
    return averageOfSalaries

# Always got to call main function! Never forget!     
main()
