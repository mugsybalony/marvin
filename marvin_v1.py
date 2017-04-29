import datetime
import time

task = datetime.datetime(2017, 04, 26, 20, 37, 50)
tasks_completed = 0

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
    while datetime.datetime.now() < task:
        time.sleep(1)
    tasks_completed += 1
    if tasks_completed == 1:
        print str(tasks_completed) + " task completed"
    else:
        print str(tasks_completed) + " tasks completed"

    task_begin = raw_input("Please set when your next task begins using this format: '2017/04/26 20:00:00' : ")
    task_end = raw_input("Please set when your next task ends using this format: '2017/04/26 20:00:00' : ")
    get_next_task(task_begin)



task_tracker()





set_next_task = datetime.datetime.strptime(next_task, '%Y/%m/%d %H:%M:%S')

