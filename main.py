import studytask as st

task = st.StudyTask("Vector Fields", difficulty=3)

json_string = task.to_json()
print(json_string)

task_from_json = st.StudyTask.from_json(json_string)
print(task_from_json)