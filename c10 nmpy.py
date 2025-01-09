import numpy as np
import pandas as pd

data = {'Name': ['Martin', 'Nora', 'Fred', 'David', 'Sara'],
        'Job': ['Doctor', 'Engineer', 'Teacher', 'Accountant', 'Nurse'],
        'Country': ['Australia', 'America', 'England', 'Italy', 'Canada'],
        'Age': [35, 20, 42, 28, 30]}

df = pd.DataFrame(data)

ages = np.array([20, 42])

# Correct filtering
filtered = df[df["Age"].isin(ages)]

print(filtered["Age"])