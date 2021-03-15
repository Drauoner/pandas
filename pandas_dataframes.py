import pandas as pd

grades_dict = {
    "Wally": [87, 96, 70],
    "Eva": [100, 87, 90],
    "Sam": [94, 77, 90],
    "Katie": [100, 81, 82],
    "Bob": [83, 65, 85],
}

grades = pd.DataFrame(grades_dict)

grades.index = ["Test1", "Test2", "Test3"]

print(grades)

print(grades["Eva"])

print(grades.Sam)

# loc, iloc, at, iat    <--- Use these methods, they are more efficient/faster.

print(grades.loc["Test1"])

print(grades.iloc[0])

# For consecutive rows

print(grades.loc["Test1":"Test2"])

print(grades.iloc[0:2])

# For non-consecutive rows

print(grades.loc[["Test1", "Test3"]])

print(grades.iloc[[0, 2]])

# View only Eva and Katie's grades for Test1 and Test2

print(grades.loc[:"Test2", ["Eva", "Katie"]])

# View only Sam through Bob's grades for Test1 and

print(grades.loc[["Test1", "Test3"], "Sam":"Bob"])

grades_A = grades[grades >= 90]

print(grades_A)

# Create a dataframe for everyone with a B grade

grades_B = grades[(grades >= 80) & (grades < 90)]
print(grades_B)

# Create a dataframe for everyone with an A or B grade

grades_A_or_B = grades[(grades >= 90) | (grades >= 80)]
print(grades_A_or_B)

# Describe method
pd.set_option("precision", 2)
# By student
print(grades.describe())
# By test
print(grades.T.describe())
