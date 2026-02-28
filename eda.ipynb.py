import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('../data/students.csv')

plt.scatter(df['study_hours'], df['final_score'])
plt.xlabel("Study Hours")
plt.ylabel("Final Score")
plt.title("Study Hours vs Score")
plt.show()