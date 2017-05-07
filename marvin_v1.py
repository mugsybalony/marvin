import datetime
import time

task = datetime.datetime(2017, 04, 26, 20, 37, 50)
tasks_completed = 0

#this function takes user inputted time and converts it to a programmable format
def get_next_task(i):
    global task
    global task_begin
    task = datetime.datetime.strptime(i, '%Y/%m/%d %H:%M:%S')
    print task
    task_begin = 0
    task_tracker()



def task_tracker():
    global task
    global task_begin
    global tasks_completed
    while datetime.datetime.now() < task:   #waits for time of task and then code continues
        time.sleep(1)
    #the code below only runs if the time of the task is now.
    tasks_completed += 1
    if tasks_completed == 1:
        print str(tasks_completed) + " task completed"
    else:
        print str(tasks_completed) + " tasks completed"

    #Asks when the next task is due to be started
    task_begin = raw_input("Please set when your next task begins using this format: '2017/04/26 20:00:00' : ")
    hourly = raw_input("Will this task be repeated hourly? Y/N: ")


    #To track when to send the follow up email
    task_end = raw_input("Please set when your next task ends using this format: '2017/04/26 20:00:00' : ")



    get_next_task(task_begin)



task_tracker()




'''
set_next_task = datetime.datetime.strptime(next_task, '%Y/%m/%d %H:%M:%S')
Can't remember why I kept the above line.
'''