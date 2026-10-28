
import pandas as pd
import matplotlib.pyplot as plt

print("Student Performance Analysis Started!")

data = {
    "Student": ["Aman", "Priya", "Rahul", "Sneha", "Anshul",
                "Neha", "Rohit", "Karan"],
    "Maths": [78, 92, 65, 88, 81, 73, 59, 95],
    "Science": [85, 89, 70, 91, 76, 80, 62, 94],
    "English": [80, 95, 68, 84, 90, 75, 64, 88]
}

df = pd.DataFrame(data)

subjects = ["Maths", "Science", "English"]
df["Total"] = df[subjects].sum(axis=1)
df["Average"] = df[subjects].mean(axis=1).round(2)

print("\nSTUDENT PERFORMANCE ANALYSIS")
print(df.to_string(index=False))

top_student = df.loc[df["Average"].idxmax()]

print("\nTop Performing Student:", top_student["Student"])
print("Average Marks:", top_student["Average"])

df.to_csv("student_performance_results.csv", index=False)

print("\nResults saved successfully!")


# Student Performance Visualization

df.set_index("Student")[subjects].plot(
    kind="bar", figsize=(10, 6)
)

plt.title("Student Performance by Subject")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.ylim(0, 100)
plt.legend(title="Subjects")
plt.tight_layout()
plt.savefig("student_performance_chart.png")
plt.show()

print("Chart saved successfully!")
