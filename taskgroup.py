class TaskGroup:
    def __init__(self, title, task_buckets):
        self.title = title
        self.task_buckets = task_buckets
    
    def __str__(self):
        task_bucket_strings = [str(tb) for tb in self.task_buckets]
        return f"{self.title}:\n" + "\n".join(task_bucket_strings)
    
    def order_task_buckets(self):
        self.task_buckets.sort(key=lambda x: (x.bucket, x.difficulty, x.volume))