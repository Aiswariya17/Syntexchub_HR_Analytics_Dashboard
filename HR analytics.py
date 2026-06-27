import pandas as pd
df=pd.read_csv(r"C:\Users\acer\OneDrive\Documents\HR_Analytics.csv")
df.head()
print(df.info())
print()
print(df.head(10))
print()
print(df.isnull().sum())
print()
print(df.duplicated().sum())
print()
print("Dataset Shape:",df.shape)
print()
print(df.columns)
print()
print(df.describe())
print()
print(df["Department"].value_counts())
print()
print(df["Gender"].value_counts())
print()
print(df["Attrition"].value_counts())
print()
print("Average Salary:",df["MonthlyIncome"].mean())
print()
print("Average Age:",df["Age"].mean())
print()
#Bar chart - Employees by department
import matplotlib.pyplot as plt

df["Department"].value_counts().plot(kind="bar", figsize=(8,5))

plt.title("Employees by Department")
plt.xlabel("Department")
plt.ylabel("Number of Employees")
plt.xticks(rotation=45)
plt.show()

#Pie Chart - Attrition
df["Attrition"].value_counts().plot(
    kind="pie",
    autopct="%1.1f%%",
    figsize=(6,6)
)

plt.title("Employee Attrition")
plt.ylabel("")
plt.show()

#Histogram - Age distribution
plt.figure(figsize=(8,5))

plt.hist(df["Age"], bins=10)

plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()

#Box plot - Monthly Income
plt.figure(figsize=(8,5))

plt.boxplot(df["MonthlyIncome"])

plt.title("Monthly Income Distribution")
plt.ylabel("Monthly Income")
plt.show()

#Correlation Heatmap
import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(16,12))

numeric_df = df.select_dtypes(include="number")

sns.heatmap(
    numeric_df.corr(),
    annot=True,
    fmt=".2f",
    cmap="coolwarm",
    linewidths=0.5
)

plt.title("Correlation Heatmap", fontsize=18)
plt.xticks(rotation=45, ha="right")
plt.yticks(rotation=0)
plt.tight_layout()

plt.show()

total_employees = len(df)
active_employees = len(df[df["Attrition"] == "No"])
employees_left = len(df[df["Attrition"] == "Yes"])

attrition_rate = (employees_left / total_employees) * 100
retention_rate = (active_employees / total_employees) * 100

average_age = df["Age"].mean()
average_salary = df["MonthlyIncome"].mean()

print("Total Employees:", total_employees)
print("Active Employees:", active_employees)
print("Employees Left:", employees_left)
print("Attrition Rate: {:.2f}%".format(attrition_rate))
print("Retention Rate: {:.2f}%".format(retention_rate))
print("Average Age:", round(average_age, 2))
print("Average Salary:", round(average_salary, 2))
print()
df.to_csv("HR_Analytics_Cleaned.csv", index=False)
print("Dataset saved successfully!")
