import random
import time

def selection_sort(list):
    comp = 0
    for i in range(len(list)-1):
        smallest = list[i]
        smol_ind = i
        for j in range(i+1, len(list)):
            if list[j] < smallest:
                smallest = list[j]
                smol_ind = j
            comp += 1
        list[smol_ind] = list[i]
        list[i] = smallest
    return comp



def insertion_sort(list):
    comp = 0
    for i in range(1, len(list)):
        find = list[i]
        j = i-1
        while j >=0 and find < list[j]:
            comp += 1
            list[j+1] = list[j]
            j -= 1
        list[j+1] = find
    return comp


def main():
    # Code coverage NOT required for main
    # Give the random number generator a seed, so the same sequence of
    # random numbers is generated at each run
    random.seed(4327)

    # Generate 5000 random numbers from 0 to 999,999
    randoms_1 = random.sample(range(1000000), 32000)
    randoms_2 = random.sample(range(1000000), 32000)

    start_time_1 = time.time()
    comps_1 = selection_sort(randoms_1)
    stop_time_1= time.time()
    print('selection: ',comps_1, stop_time_1 - start_time_1)

    start_time_2 = time.time()
    comps_2 = insertion_sort(randoms_2)
    stop_time_2 = time.time()
    print('insertion: ',comps_2, stop_time_2 - start_time_2)

if __name__ == '__main__':
    main()
