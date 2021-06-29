import threading
from threading import Event

class mark_student():
    def __init__(self, name_subject, date, mark) -> None:
        self.name_subject = name_subject
        self.date = date
        self.mark = mark
    
    def get_name_subject(self):
        return self.name_subject

    def set_name_subject(self, name):
        self.name_subject = name
    
    def get_date(self):
        return self.date
    
    def set_date(self, new_date):
        self.date = new_date
    
    def get_mark(self):
        return self.mark

    def set_mark(self, new_mark):
        self.mark = new_mark

class Student(mark_student):
    def __init__(self, name_subject, date, mark, name_student, classroom, event, list_marks = []) -> None:
        super().__init__(name_subject, date, mark)
        self.name_student = name_student
        self.classroom = classroom
        self.list_marks = []
        self.event = event
    
    def new_vote(self):
        self.list_marks.append(mark_student(self.name_subject, self.date, self.mark))
    
    def __repr__(self) -> str:
        # return self.name_subject, self.date, self.mark
        for dd in self.list_marks:
            print("[" + dd.get_name_subject() + " " + dd.get_date() + " " +  dd.get_mark() + "]")
 

if __name__ == "__main__":
    marks = []
    # new_vote1 = mark_student("diocane", "proc", 1241)
    event = threading.Event()
    new_obj = Student("tech", "diocane", "ooo", "4F", event, marks)
    new_obj.new_vote()
    new_obj.new_vote()
    print(len(new_obj.list_marks))
    # print(new_obj.show_all_marks())
    print(new_obj.__repr__())