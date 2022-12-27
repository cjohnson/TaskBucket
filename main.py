import taskbucket as tb

task = tb.TaskBucket("Vector Fields", difficulty=3)

for i in range(5):
    print(task)
    task.study(True)