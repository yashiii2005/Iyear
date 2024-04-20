import pandas as pd

# 1. Create dictionaries for each subject
CompSc = {
    '101': 85,
    '102': 78,
    '103': 92,
    '104': 88,
    '105': 75,
    '106': 90,
    '107': 82,
    '108': 95,
    '109': 81,
    '110': 87
}

Mathematics = {
    '101': 75,
    '102': 82,
    '103': 90,
    '104': 88,
    '105': 79,
    '106': 85,
    '107': 92,
    '108': 78,
    '109': 84,
    '110': 89
}

Physics = {
    '101': 88,
    '102': 82,
    '103': 91,
    '104': 85,
    '105': 79,
    '106': 93,
    '107': 87,
    '108': 90,
    '109': 84,
    '110': 86
}

# 2. Create DataFrame 'Marks'
Marks = pd.DataFrame({'CS': CompSc, 'Maths': Mathematics, 'Physics': Physics})

# 3. Add marks of five more students to the dataframe
additional_data = {
    '111': {'CS': 82, 'Maths': 75, 'Physics': 84},
    '112': {'CS': 90, 'Maths': 88, 'Physics': 87},
    '113': {'CS': 85, 'Maths': 79, 'Physics': 92},
    '114': {'CS': 88, 'Maths': 82, 'Physics': 89},
    '115': {'CS': 92, 'Maths': 86, 'Physics': 83}
}

for roll, marks in additional_data.items():
    Marks.loc[roll] = marks

# 4. Create Series 'Names'
Names = pd.Series(['Alice', 'Bob', 'Charlie', 'David', 'Emily', 'Frank', 'Grace', 'Hannah', 'Isaac', 'Jack', 'Kate', 'Liam', 'Mary', 'Nathan', 'Olivia'], 
                  index=Marks.index)

# 5. Add column 'Names' to the dataframe
Marks['Names'] = Names

# 6. Add column 'English'
Marks['English'] = [75, 80, 85, 90, 70, 95, 88, 82, 79, 83, 76, 91, 86, 89, 72]

# 7. Create DataFrame 'EVS_DF'
EVS = {
    '101': 78,
    '102': 84,
    '103': 87,
    '104': 90,
    '105': 82,
    '106': 85,
    '107': 89,
    '108': 81,
    '109': 86,
    '110': 83,
    '111': 87,
    '112': 91,
    '113': 82,
    '114': 88,
    '115': 85
}

EVS_DF = pd.DataFrame({'EVS': EVS})

# 8. Merge 'EVS_DF' and 'Marks'
Marks = pd.merge(Marks, EVS_DF, left_index=True, right_index=True, how='outer')

# 9. Add column 'Percentage'
total_marks = Marks[['CS', 'Maths', 'Physics', 'English', 'EVS']].sum(axis=1)
max_marks = 100 * 5
Marks['Percentage'] = (total_marks / max_marks) * 100

# 10. Display column types
print("Column Types of 'Marks':")
print(Marks.dtypes)

# 11. Display row labels
print("\nRow Labels of 'Marks':")
print(Marks.index)

# 12. Add 'Min' and 'Max' rows
Marks.loc['Min'] = Marks.min()
Marks.loc['Max'] = Marks.max()

# 13. Add column 'Pass'
Marks['Pass'] = Marks['Percentage'] >= 60
passed_students = Marks[Marks['Pass']]
print("\nStudents who have passed:")
print(passed_students)

# 14. Display record of a particular student (roll number 112)
print("\nRecord of student with roll number 112:")
print(Marks.loc['112'])

# 15. Display record of a particular student (name 'Priti')
pritistudent = Marks.loc[Marks['Names'] == 'Priti']
print("\nRecord of student with name 'Priti':")
print(pritistudent)

# 16. Store contents in a text file
Marks.to_csv('Marks.csv')

# 17. Display dataframe with each student's data in separate column
print("\nDataFrame with data of each student in a separate column:")
for column in Marks.columns:
    print(column, "\n", Marks[column], "\n")

# 18. Name and roll number of student with maximum marks in CompSc
max_comp_marks_student = Marks.loc[Marks['CS'].idxmax()]
print("Student with maximum marks in CompSc:")
print("Name:", max_comp_marks_student['Names'])
print("Roll number:", max_comp_marks_student.name)

# 19. Details of student with minimum marks in Maths
min_maths_marks_student = Marks.loc[Marks['Maths'].idxmin()]
print("\nDetails of student with minimum marks in Maths:")
print(min_maths_marks_student)

# 20. Records of students with marks in CompSc in the range (80, 100)
comp_sc_range = Marks[(Marks['CS'] > 80) & (Marks['CS'] < 100)]
print("\nRecords of students with marks in CompSc in the range (80, 100):")
print(comp_sc_range)

# 21. Details of students with marks greater than 40 in English and EVS
greater_than_40 = Marks.where((Marks['English'] > 40) & (Marks['EVS'] > 40))
print("\nDetails of students with marks greater than 40 in English and EVS:")
print(greater_than_40)

# 22. Retrieve contents of Marks.csv to create 'NewMarks' dataframe
NewMarks = pd.read_csv('Marks.csv', index_col=0)

# 23. Add 5 to all marks of all students in 'NewMarks'
# Drop non-numeric columns (if any) before adding 5 to marks
numeric_marks = NewMarks.select_dtypes(include='number')
NewMarks[numeric_marks.columns] += 5

# 24. Shape and size of 'NewMarks' dataframe
print("\nShape of 'NewMarks' dataframe:", NewMarks.shape)
print("Size of 'NewMarks' dataframe:", NewMarks.size)

# 25. Sort 'NewMarks' dataframe in order of student names
NewMarks_sorted_names = NewMarks.sort_values(by='Names')
print("\nSorted 'NewMarks' dataframe by student names:")
print(NewMarks_sorted_names)

# 26. Sort 'NewMarks' dataframe in descending order of marks in CompSc
NewMarks_sorted_comp_sc = NewMarks.sort_values(by='CS', ascending=False)
print("\nSorted 'NewMarks' dataframe in descending order of marks in CompSc:")
print(NewMarks_sorted_comp_sc)
