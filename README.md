Student Learning Portal
A simple, menu-driven Python application for managing learner records and tracking course progress. This project was developed for the PROG211 — Object-Oriented Programming 1 assignment and demonstrates object-oriented programming in an education-focused example.
Table of Contents
- Project Overview
- Objectives
- Features
- Technologies Used
- Project Structure
- Requirements
- Installation and Setup
- How to Run
- How to Use
- Sample Run
- Object-Oriented Programming Concepts
- Data Storage
- Digital Public Goods Principles
- Privacy and Limitations
- Testing
- GitHub Submission Checklist
- License
- Author
Project Overview
The Student Learning Portal allows a user to add learner records, display records, search for a learner by code, and update a learner's course progress. It is a beginner-friendly demonstration of classes, objects, attributes, methods, and a collection of objects.
Objectives
- Demonstrate fundamental object-oriented programming concepts in Python.
- Create and manage multiple learner records.
- Update and display course progress.
- Use one primary data structure to store multiple objects.
- Demonstrate instance, class, and static methods.
- Present an accessible, privacy-conscious educational software example.
Features
- Add a learner record.
- View all learner records saved during the current run.
- Search for a learner by learner code.
- Update a learner's progress percentage.
- Validate learner codes and progress values.
- Reject duplicate learner codes.
- Display helpful messages for invalid input.
- Run through a terminal-based menu.
Technologies Used
- Language: Python 3
- Standard library: datetime
- Interface: Command-line menu
- External dependencies: None
Project Structure
student-learning-portal/
├── student_learning_portal.py
└── README.md
Keep the Python source file and this README in the same project folder. Rename this document to README.md before uploading it to GitHub.
Requirements
- Python 3.8 or newer is recommended.
- A terminal or command prompt.
- No additional packages are required.
Check your Python installation:
python --version
On some systems, use:
python3 --version
Installation and Setup
1. Create a project folder named student-learning-portal.
2. Copy student_learning_portal.py and this README into that folder.
3. Open a terminal or command prompt in the project folder.
4. Confirm that Python is installed by running python --version or python3 --version.
How to Run
Windows
python student_learning_portal.py
If that command is not recognised, try:
py student_learning_portal.py
macOS or Linux
python3 student_learning_portal.py
How to Use
Follow the menu displayed in the terminal. You can add a learner by entering a learner code, display name, course, and progress percentage; view all records; search by learner code; update progress; or exit the program.
Enter progress as a number from 0 to 100. Use a unique learner code for each learner. Records are held in memory and are cleared when the program exits.
Sample Run
The exact wording may vary slightly depending on the current program version.
WELCOME TO THE STUDENT LEARNING PORTAL

MAIN MENU
1. Add learner
2. View all learners
3. Search learner by code
4. Update course progress
5. Exit

Choose an option (1-5): 1
Enter learner code: L001
Enter display name: Sample Learner
Enter course: Python Fundamentals
Enter progress percentage (0-100): 35

Learner added successfully.
The values above are examples only. Use fictional information for demonstrations.
Object-Oriented Programming Concepts
Classes and Objects
- Student represents a learner and stores that learner's attributes.
- StudentLearningPortal manages learner objects and menu operations.
- Each learner record is an instance of the Student class.
Attributes
The Student class includes attributes such as learner code, display name, course, progress percentage, and last-updated information. It also uses a class-level school name.
Instance Methods
Instance methods work with a particular learner object. Examples include methods for updating progress and displaying learner information.
Class Method
The class method provides a way to create a learner object from user input.
Static Method
The static method validates the format of a learner code without needing a particular learner object.
Object Interaction
The portal creates and manages Student objects, searches for them, displays their details, and requests updates to their progress.
Data Storage
The program uses one primary data structure: a dictionary that maps each learner code to a Student object. This supports multiple records and straightforward lookup by learner code.
Data is stored only in memory. The program does not write records to a database or file, so records disappear when the program closes.
Digital Public Goods Principles
This project is a small educational example that can be shared and improved publicly. To strengthen its alignment with Digital Public Goods principles:
- Open source: Publish the source code in a public GitHub repository and add an appropriate open-source licence.
- Inclusive access: Keep the interface clear and usable without specialised hardware.
- Privacy: Avoid collecting unnecessary personal or sensitive information.
- Modularity: Keep learner data and portal operations organised in separate classes.
- Reuse: Allow others to study, adapt, and extend the project for educational purposes.
A public GitHub repository alone does not automatically establish that a project meets every Digital Public Goods standard. Review it against the criteria required by the assignment.
Privacy and Limitations
- Use fictional learner information when demonstrating the program.
- Do not enter passwords, national identification numbers, medical details, or other sensitive information.
- Records are not persistent and are not backed up.
- The program is a learning prototype, not a production student information system.
- Authentication, role-based permissions, persistent storage, and a graphical interface are not included.
Testing
Manually check the following cases:
- Add a learner with valid information.
- Try to add a duplicate learner code.
- Search for an existing learner.
- Search for a learner code that does not exist.
- Update progress with a valid value between 0 and 100.
- Enter a progress value below 0 or above 100.
- Enter blank required fields.
- View all learner records.
- Exit the program using the menu.
Record actual test outcomes if your lecturer requires screenshots or a test report. Do not claim a test passed unless you have run it.
GitHub Submission Checklist
- [ ] Upload student_learning_portal.py.
- [ ] Save this document as README.md.
- [ ] Add an appropriate open-source licence if required.
- [ ] Include genuine screenshots of the program running.
- [ ] Verify that the README's run commands work on your computer.
- [ ] Add your lecturer as a repository collaborator if required by the assignment.
- [ ] Check the assignment brief for additional submission requirements.
License
No licence is applied by this README. Before publishing the project, select and add an appropriate open-source licence if your assignment requires one. Do not claim a licence has been applied until its licence file is present in the repository.
