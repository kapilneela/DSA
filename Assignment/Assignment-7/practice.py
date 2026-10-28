import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

filename = input("Enter CSV filename: ")
df = pd.read_csv(filename)

print("\nDataset:")
print(df)

print("\nAverage Maths Marks:", df["Maths"].mean())
print("Average Python Marks:", df["Python"].mean())
print("Average Attendance:", df["Attendance"].mean())

plt.figure(figsize=(7, 4.5))
plt.plot(df["Student"], df["Python"], marker="o")
plt.title("Python Marks of Students")
plt.xlabel("Student")
plt.ylabel("Python Marks")
plt.grid(True)
plt.tight_layout()
plt.show()

plt.figure(figsize=(7, 4.5))
plt.bar(df["Student"], df["Maths"])
plt.title("Maths Marks of Students")
plt.xlabel("Student")
plt.ylabel("Maths Marks")
plt.tight_layout()
plt.show()

plt.figure(figsize=(7, 4.5))
plt.scatter(df["Maths"], df["Python"], s=70)
plt.title("Maths vs Python Marks")
plt.xlabel("Maths Marks")
plt.ylabel("Python Marks")
plt.grid(True)
plt.tight_layout()
plt.show()

correlation = df[["Maths", "Python", "Attendance"]].corr()
print("\nCorrelation Matrix:")
print(correlation)

plt.figure(figsize=(6.5, 5))
sns.heatmap(
    correlation,
    annot=True,
    cmap="Blues",
    vmin=-1,
    vmax=1
)
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.show()

plt.figure(figsize=(7, 4.5))
plt.hist(df["Python"], bins=5, edgecolor="black")
plt.title("Distribution of Python Marks")
plt.xlabel("Python Marks")
plt.ylabel("Number of Students")
plt.tight_layout()
plt.show()

plt.figure(figsize=(7, 4.5))
sns.boxplot(data=df[["Maths", "Python"]])
plt.title("Box Plot of Maths and Python Marks")
plt.ylabel("Marks")
plt.tight_layout()
plt.show()

city_counts = df["City"].value_counts()
plt.figure(figsize=(6, 6))
plt.pie(
    city_counts,
    labels=city_counts.index,
    autopct="%1.1f%%",
    startangle=90
)
plt.title("Students from Each City")
plt.tight_layout()
plt.show()

print("\nAll plots generated successfully.")
