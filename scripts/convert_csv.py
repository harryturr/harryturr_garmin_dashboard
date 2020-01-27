import pandas as pd
import numpy as np
import datetime as datetime
import os

df2 = pd.read_csv("activities_5_correct.csv")
df2 = df2.reindex(
    columns=[
        "Activity_Type",
        "Date",
        "Title",
        "Distance",
        "Calories",
        "Time",
        "Avg_HR",
        "Max_HR",
        "Avg_Pace",
        "Elev_Gain",
    ]
)
df2.Date.iloc[::-1]
date_df = df2.iloc[::-1].Date.to_numpy()

# Function to rename multiple files
def main():
    i = 0
    for filename in sorted(os.listdir("data")):
        src = "data/" + filename
        dst = "./data_rename/" + date_df[i] + ".gpx"
        print(src)
        os.rename(src, dst)
        i += 1


if __name__ == "__main__":
    main()
print("end")
