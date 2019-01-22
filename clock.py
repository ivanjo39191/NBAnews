import os
from apscheduler.schedulers.blocking import BlockingScheduler
sched = BlockingScheduler()

@sched.scheduled_job('interval', seconds=10)

def cr():
    print('do crawler')
    os.system("python crawler.py")

sched.start()