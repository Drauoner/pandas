import pandas as pd

grades = pd.Series([87, 100, 94])

print(grades)

grades = pd.Series(98.6, range(3))

print(grades)

a = grades[0]


print(a)

# Calling Series method describe that produces all these stats and more:
print(grades.describe())


grades = pd.Series([87, 100, 94], index=["Wally", "Eva", "Sam"])

print(grades)


# If you initialize a Series with a dictionary, its keys become the Series' indices, and
# its values become the Series' element values:

grades = pd.Series({"Wally": 87, "Eva": 100, "Sam": 94})

print(grades)

print(grades["Eva"])

# If the custom indices are strings that could represent valid Python indentifiers,
# pandas automatically adds them to the Series as attributes that you can access via a dot, as in:
print(grades.Wally)

# Series has built-in attributes, such as dtype attribute which returns underlyinga rray's element type:
print(grades.dtype)


#
print(grades.values)


# Series of Strings
hardware = pd.Series(["Hammer", "Saw", "Wrench"])
print(hardware)

# calling string methods apply to each element
print(hardware.str.contains("a"))

hardware_upper = hardware.str.upper()
print(hardware_upper)