import datetime
import time

tasks = []

def set_task():
    global tasks
    #get first task from user
    print "All tasks will have an hour long duration to begin with."
    print ""

    #Gets subsequent tasks from user. Maximum of 5 to begin with.
    task_count = 0
    while task_count < 6:
        task_adder = raw_input("Please set when your next task begins using this format: '2017/04/26 20:00:00' : ")
        correct = raw_input("Would you like to add another? Y/N: ").lower().strip()


        if correct[0] == "y":
            task_count += 1
            # converts user input to a format Python likes.
            stripper = datetime.datetime.strptime(task_adder, '%Y/%m/%d %H:%M:%S')
            #insert task 'stripper' at position 'task_count'
            tasks.insert(task_count, stripper)
            


        else:
            task_count = 5000
            # converts user input to a format Python likes.
            stripper = datetime.datetime.strptime(task_adder, '%Y/%m/%d %H:%M:%S')
            #insert task 'stripper' at position 'task_count'
            tasks.insert(task_count, stripper)



    print "Alrighty. I'll let you know when your next task is due."

    task_reminder()


def task_reminder():
    global tasks
    print tasks
    number_of_tasks = str(len(tasks))
    print number_of_tasks
    x = 0
    while number_of_tasks >= x:

        # waits for time of first task in list and then code continues
        while datetime.datetime.now() < tasks[0]:
            time.sleep(1)
        #the code below only runs if the time of the task is now.
        tasks.pop(0)
        x += 1

    next_batch = raw_input("Would you like to add more tasks? Y/N: ").lower().strip()
    if next_batch[0] == "y":
        tasks = []
        set_task()
    else:
        print "Goodbye"




set_task()