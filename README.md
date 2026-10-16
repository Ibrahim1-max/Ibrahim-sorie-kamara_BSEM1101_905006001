# Ibrahim-sorie-kamara_BSEM1101_905006001
Student Learning Portal — PROG211 OOP1
Problem and domain
This console application is an educational-domain example of a simple Student Learning Portal. It allows a user to add learner records, display records, search by learner code, and update course progress.
Files
- student_learning_portal.py — complete Python source code.
How to run
1. Install Python 3.8 or newer.
2. Save student_learning_portal.py.
3. Open a terminal in the same folder.
4. Run: python student_learning_portal.py
No external packages are required.
Example usage
Example input sequence:
- Choose 1
- Learner code: STU-101
- Display name: Mariam K.
- Course: Introduction to Communication
- Progress: 40
- Choose 2 to view records
- Choose 4, enter STU-101, then enter 65 to update progress
- Choose 5 to exit
Illustrative output:
Learner record added successfully.

LEARNER RECORDS
Learner code : STU-101
Display name : Mariam K.
Course       : Introduction to Communication
Progress     : 40%
...
Learning progress updated successfully.
OOP and assignment requirements
- Classes and objects: Student and StudentLearningPortal classes; the portal creates and manages Student objects.
- Attributes: learner code, display name, course, progress, and last-updated timestamp.
- Methods: update_progress(), display_info(), add_student(), find_student(), update_student_progress(), display_all_students(), and run().
- Object creation and interaction: the portal creates a Student object and stores it in the portal.
- One data structure: one dictionary, self.students, stores multiple Student objects using learner code as the key.
- Simple add/display functions: add_student() and display_all_students().
- Instance method: update_progress() and display_info().
- Class method: Student.create_from_input().
- Static method: Student.is_valid_learner_code().
- Validation: prevents empty required fields, duplicate learner codes, invalid progress, and malformed menu inputs.
Digital Public Goods (DPG) alignment
- Open source: the code can be published in a public GitHub repository with a suitable open-source licence selected by the student or course.
- Inclusive and accessible: simple text menu, clear prompts, no colour-only instructions, and straightforward error messages.
- Privacy-respecting: asks for a display name, course and a learner code only; it warns users not to enter sensitive information.
- Modular and reusable: separate classes with clearly named methods.
Important limitations
- Records exist only in memory and are erased when the program exits.
- This is a learning prototype, not a production student-information system.
- Do not use real sensitive student records. A production system would need authentication, authorisation, secure persistence, backups, privacy review, and institutional approval.
Suggested GitHub submission checklist
- Upload student_learning_portal.py and this README.
- Choose and include an appropriate open-source licence if permitted by the course.
- Run the program and capture screenshots showing adding, listing, searching and updating a learner.
- Add the lecturer as a collaborator to the repository, as directed in the assignment brief.
- Print the required hardcopy with execution screenshots.
