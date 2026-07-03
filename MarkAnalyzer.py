import numpy as np

# Generate a 2D array (10 students × 5 subjects) with marks between 30 and 100
marks = np.random.randint(30, 101, size=(10, 5))

print("Student Marks (10x5 Matrix):",marks)

# Calculate total marks for each student (row-wise sum)
total_marks = np.sum(marks, axis=1)

# Calculate average marks for each student
average_marks = np.mean(marks, axis=1)

print("Total Marks of Each Student:",total_marks)

print("Average Marks of Each Student:",average_marks)

# Find student with highest and lowest total marks
highest_index = np.argmax(total_marks)
lowest_index = np.argmin(total_marks)

print("Student with Highest Total Marks: Student", highest_index)
print("Student with Lowest Total Marks: Student", lowest_index)

# Calculate overall class mean and standard deviation
class_mean = np.mean(marks)
class_std = np.std(marks)

print("Class Mean:", class_mean)
print("Class Standard Deviation:", class_std)

# Get indices of top 3 students based on total marks
top3_indices = np.argsort(total_marks)[-3:]   # last 3 = highest

# Reverse to get highest first
top3_indices = top3_indices[::-1]
print("Top 3 Students by index:", top3_indices)
print("Marks of Top 3 Students:")
top3_marks = marks[top3_indices]   # indexing
print(top3_marks)

# (Optional) Demonstrating reshape (flatten and reshape back)
reshaped = marks.reshape(5, 10)
print("Reshaped Array (5x10):")
print(reshaped)