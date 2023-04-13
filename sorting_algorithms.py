import math
import time
import random

NUMBER_OF_ELEMENTS_IN_TEST_LIST = 200000
NUMBER_OF_TESTS = 10
RAND_MAX = 10000

def generate_list(number_of_elements):
    list_ = [0] * number_of_elements
    for index in range(number_of_elements):
        list_[index] = random.randint(-RAND_MAX, RAND_MAX)
    return list_


def BubbleSort(list_):
    swapped = True
    last_index = len(list_)
    while swapped:
        swapped = False
        for index in range(last_index - 1):
            if list_[index] > list_[index + 1]:
                list_[index], list_[index + 1] = list_[index + 1], list_[index]
                swapped = True
        last_index -= 1
    return list_

def InsertionSort(list_):
    sortedIndex = 0
    sortedList = [list_[0]]
    while sortedIndex < len(list_) - 1:
        insertion = list_[sortedIndex + 1]
        inserted = False
        for [i, e] in enumerate(sortedList):
            if e > insertion:
                sortedList.insert(i, insertion)
                inserted = True
                break
        if not inserted:
            sortedList.append(insertion)
        sortedIndex += 1
    return sortedList


def InsertionSortBin(list_):
    sortedIndex = 0
    sortedList = [list_[0]]
    while sortedIndex < len(list_) - 1:
        insertion = list_[sortedIndex + 1]
        ind = binary_search(sortedList, insertion)
        sortedList.insert(ind, insertion)
        sortedIndex += 1
    return sortedList


def sort_check(list_):
    for index in range(len(list_) - 1):
        if list_[index] > list_[index + 1]:
            return False
    return True

def test(func):
    total_timer = 0
    for test_number in range(NUMBER_OF_TESTS):
        test_list = generate_list(NUMBER_OF_ELEMENTS_IN_TEST_LIST)
        timer = time.time()
        test_list = func(test_list)
        timer = time.time() - timer
        total_timer += timer
        if sort_check(test_list):
            print("Required time in test №", test_number + 1, "is", timer, "seconds")
        else:
            print("Error in test №", test_number + 1)
    print("Required time for", NUMBER_OF_TESTS, "tests is", total_timer, "seconds")
    print("Average time for", NUMBER_OF_TESTS, "tests is", total_timer/NUMBER_OF_TESTS, "seconds")


def search_test(func):
    total_timer = 0
    for test_number in range(NUMBER_OF_TESTS):
        test_list = generate_list(NUMBER_OF_ELEMENTS_IN_TEST_LIST)
        timer = time.time()
        search_elem = random.randint(-RAND_MAX, RAND_MAX)
        answer = func(test_list, search_elem)
        timer = time.time() - timer
        total_timer += timer
        if search_check(test_list, search_elem, answer):
            print("Required time in test №", test_number + 1, "is", timer, "seconds")
        else:
            print("Error in test №", test_number + 1)
    print("Required time for", NUMBER_OF_TESTS, "tests is", total_timer, "seconds")
    print("Average time for", NUMBER_OF_TESTS, "tests is", total_timer/NUMBER_OF_TESTS, "seconds")


def lin_search(list_, search_elem):
    for index in range(len(list_)):
        if list_[index] == search_elem:
            return index
    return None


def search_check(list_, search_elem, answer):
    if answer is None:
        for index in range(len(list_)):
            if list_[index] == search_elem:
                return False
        return True
    else:
        if list_[answer] == search_elem:
            return True
        else:
            return False


def binary_search(list_, search_elem):
    left = 0
    right = len(list_) - 1

    while left < right:
        middle = (left + right) // 2
        if search_elem > list_[middle]:
            left = middle + 1
        elif search_elem < list_[middle]:
            right = middle - 1
        else:
            return middle

    if left == right:
        if search_elem > list_[left]:
            return left + 1
        else:
            return left
    elif left > right:
        return left


def merge(list1, list2):
    first = 0
    second = 0
    res = []
    while first < len(list1) or second < len(list2):
        if first < len(list1):
            if second < len(list2):
                if list1[first] > list2[second]:
                    res.append(list1[first])
                    first += 1
                else:
                    res.append(list2[second])
                    second += 1
            else:
                res.append(list1[first])
                first += 1
        else:
            res.append(list2[second])
            second += 1


def quickSort(list_):
    if len(list_) <= 1:
        return list_
    else:
        [less, eq, more] = part(list_)
        return quickSort(less) + eq + quickSort(more)


def part(list_):
    less = []
    eq = []
    more = []
    p = list_[0]
    for j in range(0, len(list_)):
        if list_[j] < p:
            less.append(list_[j])
        elif list_[j] > p:
            more.append(list_[j])
        else:
            eq.append(list_[j])

    return [less, eq, more]

test(quickSort)
    
