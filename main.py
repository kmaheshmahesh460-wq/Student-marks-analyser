import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#variables
student_name = ["John Doe", "Jane Smith", "Alice Johnson", "Bob Brown"]
student_marks = [85, 92, 78, 96]
#numpy array
student_marks_array = np.array(student_marks)
average_marks = np.mean(student_marks_array)
highest_marks = np.max(student_marks_array)
lowest_marks = np.min(student_marks_array)


print("-----Student Marks Analysis-----")
print(f"Average Marks: {average_marks}")
print(f"Highest Marks: {highest_marks}")
print(f"Lowest Marks: {lowest_marks}")  
#pandas DataFrame
df = pd.DataFrame({
    "Student Name": student_name,
    "Marks": student_marks
})  

#matplotlib bar chart
plt.bar(df["Student Name"], df["Marks"], color='skyblue')
plt.title("Student Marks")
plt.xlabel("Student Name")
plt.ylabel("Marks")
plt.show()