# Code using libraries

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data = pd.read_csv(r#“ Enter your csv file .csv”)
#1.3 Bargraph of Total Allowance
plt.figure(figsize=(15,6))
plt.bar(data[“Employee Names”],data[“Total Allowance”])
plt.xlabel(“Employee Names”)
plt.ylabel(“Total Allowance”)
plt.title(“Total Allowance by Employee”)
plt.show()
#1.4 Pie Chart of Holidays Taken
total_holiday = data[“Holiday”].sum()
base_holiday_df = pd.DataFrame({“Employee Names”: data[“Employee Names”],
“Holiday”:data[“Holiday”]})
base_holiday_df[“Holiday”] = base_holiday_df[“Holiday”].apply(lambda x: x / total_holiday *100)
plt.figure(figsize=(8,6))
plt.pie(base_holiday_df[“Holiday”],label = base_holiday_df[“Emoloyee Names”], autopct =
“%1.1f%%” )
plt.axis(“equal”)
plt.title(“Holidays Taken by Employee Pie Chart”)
plt.show()
#1.5 Pie Chart of Sick Leaves Taken
total_sickness = data[“Sickness”].sum()
base_sickness_df = pd.DataFrame({“Employee Names”: data[“Employee
Names”],”Sickness”:data[“Sickness”]})
base_sickness_df[“Sickness”] = base_sickness_df[“Sickness”].apply(lambda x: x /
total_sickness*100)
plt.figure(figsize=(8,6))
plt.pie(base_sickness_df[“Sickness”],label = base_Sickness_df[“Emoloyee Names”], autopct =
“%1.1f%%” )
plt.axis(“equal”)
plt.title(“Sick Leaves Taken by Employee Pie Chart”)
plt.show()
