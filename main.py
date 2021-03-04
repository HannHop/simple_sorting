import random
import time
arr_int = [1, 10, 2, 34, 15, 8, 9]
arr_str = ['jania', 'becia', 'klaudia', 'asia', 'stacha']

rand_8k_int = random.sample(range(1, 20000), 8000)  # 'choice' instead of 'sample' for sampling with replacement
rand_16k_int = random.sample(range(1, 40000), 16000)
rand_32k_int = random.sample(range(1, 60000), 32000)
rand_64k_int = random.sample(range(1, 70000), 64000)
rand_128k_int = random.sample(range(1, 130000), 128000)

f = open("words.txt", "r")  # https://www.wordgamedictionary.com/english-word-list/download/english.txt
big_list = f.readlines()
big_list = [word[:-1] for word in big_list]

rand_2k_string = random.sample(big_list, 2000)
rand_4k_string = random.sample(big_list, 4000)
rand_8k_string = random.sample(big_list, 8000)
rand_16k_string = random.sample(big_list, 16000)
rand_32k_string = random.sample(big_list, 32000)


def check_is_sorted(arr):
    i = 1
    is_sorted = 1
    while i < len(arr)-1 and is_sorted:
        if arr[i - 1] > arr[i]:
            is_sorted = 0
            print("Array is UNSORTED!")
        i = i + 1
    if is_sorted:
        print("Array is SORTED :)")

def swap(var1, var2):
    temp = var1
    var1 = var2
    var2 = temp
    return var1, var2


def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(1, len(arr)):
            if arr[j-1] > arr[j]:
                arr[j], arr[j-1] = swap(arr[j], arr[j-1])


def selection_sort(arr):
    for i in range(len(arr)-1):
        index_min = i
        val_min = arr[i]
        for j in range(i + 1, len(arr)):
            if arr[j] < val_min:
                index_min = j
                val_min = arr[j]
        arr[i], arr[index_min] = swap(arr[i], arr[index_min])


def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j-1] > arr[j]: #search for smaller element than last element on left (sorted) sublist
            arr[j], arr[j - 1] = swap(arr[j], arr[j - 1])
            j = j - 1


# def binary_search(key, arr, left, right):  #??????????????????
#     if left == right:
#         if arr[left] > key:  # check where to position the key
#             # because it can be lower than left boundary of sorted interval
#             return left  # return left position
#         else:
#             return left + 1
#
#     if left > right:
#         return left
#     mid = (left + right)//2
#     if arr[mid] < key:
#         return binary_search(key, arr, mid + 1, right)
#     elif arr[mid] > key:
#         return binary_search(key, arr, left, mid - 1)
#     else:
#         return mid
#         #if arr[mid] == key:  #searched val is equal middle of the sorted interval
#         #    for i in range(k, mid, -1):  #?????????????????????????????????????? poprawic na pewno to, bo nie dziala
#         #        A[i] = A[i - 1]
#         #    A[i - 1] = key
#
#
# def binary_insertion_sort(arr):     # improved insertion sort (do it!)
#     for i in range(1, len(arr)):
#         key = arr[i]
#         j = binary_search(key, arr, 0, i - 1)
#         arr = arr[:j] + [key] + arr[j:i] + arr[i + 1:]
#     return arr


def binary_search(arr, key, left, right):
    if right <= left:
        if key > arr[left]:
            return left + 1
        else:
            return left
    mid = (left + right)//2
    if key == arr[mid]:
        return mid + 1
    if key > arr[mid]:
        return binary_search(arr, key, mid+1, right)
    return binary_search(arr, key, left, mid - 1)


def binary_insertion_sort(arr):
    for i in range(1, len(arr), 1):

        selected = arr[i]
        location = binary_search(arr, selected, 0, i - 1)
        j = i-1
        while j >= location:  # move everything j = i-1
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = selected


set_ = rand_64k_int
start = time.perf_counter()
binary_insertion_sort(set_)
stop = time.perf_counter()
print("insert extra 32k int has taken:", stop - start, "seconds")
check_is_sorted(set_)

set_ = rand_128k_int
start = time.perf_counter()
binary_insertion_sort(set_)
stop = time.perf_counter()
print("insert extra 32k int has taken:", stop - start, "seconds")
check_is_sorted(set_)

# set_ = rand_8k_string
# start = time.perf_counter()
# binary_insertion_sort(set_)
# stop = time.perf_counter()
# print("insert extra 32k int has taken:", stop - start, "seconds")
# check_is_sorted(set_)
#
# set_ = rand_16k_string
# start = time.perf_counter()
# binary_insertion_sort(set_)
# stop = time.perf_counter()
# print("insert extra 32k int has taken:", stop - start, "seconds")
# check_is_sorted(set_)
#
# set_ = rand_32k_string
# start = time.perf_counter()
# binary_insertion_sort(set_)
# stop = time.perf_counter()
# print("insert extra 32k int has taken:", stop - start, "seconds")
# check_is_sorted(set_)
