import matplotlib.pyplot as plt

subjects = ['Math', 'Science', 'English', 'History']
marks = [80, 90, 70, 85]
# CHANGED
plt.bar(subjects, marks, color='skyblue')
plt.title("Marks by Subject")
plt.xlabel("Sub")
plt.ylabel("Mark")
plt.show()
