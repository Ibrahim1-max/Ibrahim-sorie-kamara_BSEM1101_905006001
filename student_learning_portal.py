from datetime import datetime

class Student:
    school_name = 'Student Learning Portal'

    def __init__(self, learner_code, display_name, course, progress_percent=0):
        self.learner_code = learner_code.strip().upper()
        self.display_name = display_name.strip()
        self.course = course.strip()
        self.progress_percent = progress_percent
        self.last_updated = datetime.now().strftime('%Y-%m-%d %H:%M')

    def update_progress(self, new_progress):
        if not 0 <= new_progress <= 100:
            raise ValueError('Progress must be between 0 and 100.')
        self.progress_percent = new_progress
        self.last_updated = datetime.now().strftime('%Y-%m-%d %H:%M')

    def display_info(self):
        return f'Learner code : {self.learner_code}\nDisplay name : {self.display_name}\nCourse       : {self.course}\nProgress     : {self.progress_percent}%\nLast updated : {self.last_updated}'

    @classmethod
    def create_from_input(cls, learner_code, display_name, course, progress_percent=0):
        return cls(learner_code, display_name, course, progress_percent)

    @staticmethod
    def is_valid_learner_code(learner_code):
        code = learner_code.strip()
        return len(code) >= 3 and code.replace('-', '').replace('_', '').isalnum()

class StudentLearningPortal:

    def __init__(self):
        self.students = {}

    def add_student(self, student):
        code = student.learner_code
        if code in self.students:
            print('A learner with that code already exists.')
            return False
        self.students[code] = student
        print('Learner record added successfully.')
        return True

    def find_student(self, learner_code):
        return self.students.get(learner_code.strip().upper())

    def update_student_progress(self, learner_code, new_progress):
        student = self.find_student(learner_code)
        if student is None:
            print('No learner was found with that code.')
            return False
        try:
            student.update_progress(new_progress)
        except ValueError as error:
            print(f'Update failed: {error}')
            return False
        print('Learning progress updated successfully.')
        return True

    def display_all_students(self):
        if not self.students:
            print('No learner records have been added yet.')
            return
        print('\n' + '=' * 45)
        print('LEARNER RECORDS')
        print('=' * 45)
        for student in self.students.values():
            print(student.display_info())
            print('-' * 45)

    def run(self):
        print('=' * 45)
        print('WELCOME TO THE STUDENT LEARNING PORTAL')
        print('Demo only: records are kept in memory during this run.')
        print('Do not enter passwords, financial details, or other sensitive data.')
        print('=' * 45)
        while True:
            print('\nMAIN MENU')
            print('1. Add learner')
            print('2. View all learners')
            print('3. Search learner by code')
            print('4. Update course progress')
            print('5. Exit')
            choice = input('Choose an option (1-5): ').strip()
            if choice == '1':
                learner_code = input('Enter a learner code (e.g., STU-101): ').strip()
                if not Student.is_valid_learner_code(learner_code):
                    print('Invalid code. Use at least 3 letters/numbers; hyphens and underscores are allowed.')
                    continue
                display_name = input('Enter display name: ').strip()
                course = input('Enter course or learning module: ').strip()
                if not display_name or not course:
                    print('Display name and course cannot be empty.')
                    continue
                try:
                    progress = int(input('Enter course progress (0-100): ').strip())
                except ValueError:
                    print('Progress must be a whole number.')
                    continue
                if not 0 <= progress <= 100:
                    print('Progress must be between 0 and 100.')
                    continue
                student = Student.create_from_input(learner_code, display_name, course, progress)
                self.add_student(student)
            elif choice == '2':
                self.display_all_students()
            elif choice == '3':
                learner_code = input('Enter learner code to search: ').strip()
                student = self.find_student(learner_code)
                if student:
                    print('\n' + student.display_info())
                else:
                    print('No learner was found with that code.')
            elif choice == '4':
                learner_code = input('Enter learner code: ').strip()
                try:
                    progress = int(input('Enter new progress (0-100): ').strip())
                except ValueError:
                    print('Progress must be a whole number.')
                    continue
                self.update_student_progress(learner_code, progress)
            elif choice == '5':
                print('Thank you for using the Student Learning Portal.')
                print('Reminder: this demo does not save records after exit.')
                break
            else:
                print('Invalid option. Please choose a number from 1 to 5.')
if __name__ == '__main__':
    portal = StudentLearningPortal()
    portal.run()
