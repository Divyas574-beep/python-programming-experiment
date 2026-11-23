#Data Cleaning and Exploratory Data Analysis Using Pandas

import pandas as pd

data = {
    "Name": ["Anitha", "Bala", "Chitra", "Dinesh", "Ezhil", "Fathima"],
    "Department": ["CSE", "CSE", "ECE", "CSE", "ECE", "CSE"],
    "Attendance": [92, 85, None, 88, 95, 90],
    "Mark": [86, 91, 78, None, 95, 82]
}
df = pd.DataFrame(data)
print("--- Original Dataset ---")
print(df)
print("\nMissing Values:")
print(df.isnull().sum())
