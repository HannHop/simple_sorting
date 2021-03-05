# Hanna Hopkowicz macro sem 6
# import random
import time

# block of code responsible for randomizing data that is then put into file, so that later I can use the same datasets
# for each sorting function:

# rand_8k_int = random.sample(range(1, 20000), 8000)  # could be 'choice' instead of 'sample' for repl. sampling
# rand_16k_int = random.sample(range(1, 40000), 16000)
# rand_32k_int = random.sample(range(1, 60000), 32000)
# rand_64k_int = random.sample(range(1, 70000), 64000)
# rand_128k_int = random.sample(range(1, 130000), 128000)
#
# with open('8k_int.txt', 'w') as f:
#     for number in rand_8k_int:
#         f.write('%s\n' % number)
#
# with open('16k_int.txt', 'w') as f:
#     for number in rand_16k_int:
#         f.write('%s\n' % number)
#
# with open('32k_int.txt', 'w') as f:
#     for number in rand_32k_int:
#         f.write('%s\n' % number)
#
# with open('64k_int.txt', 'w') as f:
#     for number in rand_64k_int:
#         f.write('%s\n' % number)
#
# with open('128k_int.txt', 'w') as f:
#     for number in rand_128k_int:
#         f.write('%s\n' % number)


# same thing as previously but this time for strings
# f = open("words.txt", "r")  # https://www.wordgamedictionary.com/english-word-list/download/english.txt
# big_list = f.readlines()
# big_list = [word[:-1] for word in big_list]  # remove '\n' from each line
# f.close()
#
# rand_2k_string = random.sample(big_list, 2000)
# rand_4k_string = random.sample(big_list, 4000)
# rand_8k_string = random.sample(big_list, 8000)
# rand_16k_string = random.sample(big_list, 16000)
# rand_32k_string = random.sample(big_list, 32000)
#
# with open("2k_str.txt", 'w') as f:
#     for word in rand_2k_string:
#         f.write('%s\n' % word)
#
# with open("4k_str.txt", 'w') as f:
#     for word in rand_4k_string:
#         f.write('%s\n' % word)
#
# with open("8k_str.txt", 'w') as f:
#     for word in rand_8k_string:
#         f.write('%s\n' % word)
#
# with open("16k_str.txt", 'w') as f:
#     for word in rand_16k_string:
#         f.write('%s\n' % word)
#
# with open("32k_str.txt", 'w') as f:
#     for word in rand_32k_string:
#         f.write('%s\n' % word)

# part responsible for taking the content of txt files
f = open("2k_str.txt", "r")
rand_2k_str = f.readlines()
rand_2k_str = [word[:-1] for word in rand_2k_str]  # remove '\n' from each line
f.close()

f = open("4k_str.txt", "r")
rand_4k_str = f.readlines()
rand_4k_str = [word[:-1] for word in rand_4k_str]  # remove '\n' from each line
f.close()

f = open("8k_str.txt", "r")
rand_8k_str = f.readlines()
rand_8k_str = [word[:-1] for word in rand_8k_str]  # remove '\n' from each line
f.close()

f = open("16k_str.txt", "r")
rand_16k_str = f.readlines()
rand_16k_str = [word[:-1] for word in rand_16k_str]  # remove '\n' from each line
f.close()

f = open("32k_str.txt", "r")
rand_32k_str = f.readlines()
rand_32k_str = [word[:-1] for word in rand_32k_str]  # remove '\n' from each line
f.close()

f = open("8k_int.txt", "r")
rand_8k_int = f.readlines()
rand_8k_int = [int(word[:-1]) for word in rand_8k_int]  # remove '\n' from each line
f.close()

f = open("16k_int.txt", "r")
rand_16k_int = f.readlines()
rand_16k_int = [int(word[:-1]) for word in rand_16k_int]  # remove '\n' from each line
f.close()

f = open("32k_int.txt", "r")
rand_32k_int = f.readlines()
rand_32k_int = [int(word[:-1]) for word in rand_32k_int]  # remove '\n' from each line
f.close()

f = open("64k_int.txt", "r")
rand_64k_int = f.readlines()
rand_64k_int = [int(word[:-1]) for word in rand_64k_int]  # remove '\n' from each line
f.close()

f = open("128k_int.txt", "r")
rand_128k_int = f.readlines()
rand_128k_int = [int(word[:-1]) for word in rand_128k_int]  # remove '\n' from each line
f.close()


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
            if arr[j-1] > arr[j]:  # swap if wrong order
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
        while j > 0 and arr[j-1] > arr[j]:  # search for smaller element than last element on left (sorted) sublist
            arr[j], arr[j - 1] = swap(arr[j], arr[j - 1])
            j = j - 1


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
        location = binary_search(arr, selected, 0, i - 1)  # selected val will act as a 'key'
        j = i-1
        while j >= location:  # move everything j = i-1
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = selected


def cocktail_sort(arr):
    n = len(arr)
    swap_flag = True
    left = 0
    right = n - 1
    while (swap_flag == True):
        swap_flag = False

        # left -> right
        for i in range(left, right):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swap_flag = True

        # if no changes -> it's sorted
        if swap_flag == False:
            break

        swap_flag = False

        # move right back by one
        right = right - 1

        # right -> left
        for i in range(right - 1, left - 1, -1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swap_flag = True

        # move left by one
        left = left + 1


def bubble_v2(arr):  # if it is already sorted -> do nothing
    for i in range(len(arr) - 1):
        swap_flag = 0
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swap_flag = 1
        if not swap_flag:
            break


# here is the 'testing' section, I've tried each combination there
#set_ = rand_2k_str
set_ = rand_4k_str
# set_ = rand_8k_str
# set_ = rand_16k_str
# set_ = rand_32k_str
start = time.perf_counter()
cocktail_sort(set_)
stop = time.perf_counter()
print(cocktail_sort.__name__+" has taken:", stop - start, "seconds")
check_is_sorted(set_)

# set_ = rand_128k_int
# start = time.perf_counter()
# bubble_v2(set_)
# stop = time.perf_counter()
# print(bubble_v2.__name__+" has taken:", stop - start, "seconds")
# check_is_sorted(set_)
