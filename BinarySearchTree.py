import random, sort
from timeit import default_timer as timer

#start_time = timer()

trial_n = [1000, 2*1000, 4*1000, 8*1000, 16*1000, 32*1000, 64*1000, 128*1000, 126053]#powers of 2, insertion sort number for last question
n_runs = 3

for n in trial_n:

    sum_time = 0

    for run in range(n_runs):
        data = []
        for i in range(0,n):
            data.append(random.random() )

        #print("Starting...")
        start_time = timer()


        #sort.sort_insertion(data)
        #sort.sort_selection(data)
        sort.sort_quick_nr(data)

        #data.sort()

        delta_time = timer() - start_time

    # print( n, run, delta_time)

    sum_time += delta_time

    avg_time = sum_time/ n_runs


    print(n, delta_time)
