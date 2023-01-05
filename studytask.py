import datetime
import json

class StudyTask:
    def __init__(self, tag, difficulty, volume = 1):
        if difficulty > 5 or difficulty < 1:
            raise ValueError("Difficulty is from 1 to 5")
        
        self.tag = tag
        self.difficulty = difficulty
        self.volume = volume
        self.last_studied = None
    
    def __str__(self):
        return f"{self.tag}: [{self.volume}/{self.difficulty}]"

    def to_json(self):
        task_dict = {
            "tag": self.tag,
            "difficulty": self.difficulty,
            "volume": self.volume,
            "last_studied": self.last_studied.isoformat() if self.last_studied is not None else None,
        }

        return json.dumps(task_dict)
    
    @staticmethod
    def from_json(json_string):
        task_dict = json.loads(json_string)

        task = StudyTask(task_dict["tag"], task_dict["difficulty"], task_dict["volume"])
        task.last_studied = task_dict["last_studied"]

        return task

    def study(self, success):
        self.timer_check()
        self.last_studied = datetime.datetime.now()

        if not success:
            self.volume = 1
            return
        
        self.volume += 1
        
        if self.volume > self.difficulty:
            self.volume = 1