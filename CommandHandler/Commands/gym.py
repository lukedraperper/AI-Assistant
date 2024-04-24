import pandas as pd
def Exercise(command):
    try:

        df = pd.read_csv("gym.csv")

        Squats = str(df.loc[df['exercise'] == "squats"].iloc[0,1])
        BenchPress = str(df.loc[df['exercise'] == "benchpress"].iloc[0,1])
        ShoulderPress = str(df.loc[df['exercise'] == "shoulderpress"].iloc[0,1])
        Deadlifts = str(df.loc[df['exercise'] == "deadlifts"].iloc[0,1])
        BentOverRow = str(df.loc[df['exercise'] == "bentoverrow"].iloc[0,1])
        Day = str(df.loc[df['exercise'] == "day"].iloc[0,1])

        Day1 = f"Squats {Squats}, Bench Press {BenchPress}, Shoulder Press {ShoulderPress}"
        Day2 = f"Squats {Squats}, Deadlifts {Deadlifts}, Bent Over Row {BentOverRow}"

        if command == "Finished":
            if Day == "1":
                df.loc["squats","weight"] = 1
                # df.loc["benchpress","weight"] += 2.5
                # df.loc["shoulderpress","weight"] += 2.5
                # df.loc["day","weight"] += 1
                df.to_csv('gym.csv')
                print("Done.")
            else:
                df.loc["squats","weight"] += 2.5
                df.loc["deadlifts","weight"] += 2.5
                df.loc["bentoverrow","weight"] += 2.5
                df.loc["day","weight"] -= 1
                df.to_csv('gym.csv')
                print("Done.")
    except Exception as e:
        print(e)