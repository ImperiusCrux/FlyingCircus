import os
import pandas as pd


def readMachineToDate():

    #df = pd.read_csv('source/manufacturarer_mashines.csv', delimiter='|', usecols= [0, 4, 5, 6, 7, 18])

    df = pd.read_csv('source/machines.csv', delimiter=',')
    df = df.loc[df.iloc[:, 0].str.contains("BFL6.")]
    machines = df["$COLUMNS$MASCH_NR"].unique()

    for machine in machines:
        # filter by machines and write in csv
        is_machine = df['$COLUMNS$MASCH_NR'] == machine
        new_df = df[is_machine]
        if not os.path.isdir("source/machines/"):
            os.mkdir("source/machines/")
        new_df.to_csv('source/machines/' + machine + '.csv', sep=',', index=False,
                      encoding='utf-8')

    for machine in machines:
        df = pd.read_csv('source/machines/' + machine + ".csv", delimiter=',')
        date = df["BEGIN_DAT"].unique()
        for date in date:
            new_date = df["BEGIN_DAT"] == date
            nf = df[new_date]
            if not os.path.isdir("source/machinesByDate/"):
                os.mkdir("source/machinesByDate/")
            nf.to_csv('source/machinesByDate/' + machine + " " + date.replace("/", " ") + '.csv', sep=',', index=False,                      encoding='utf-8')

    #df = pd.read_csv('source/machinesByDate/', delimiter=',')
    #df.to_csv('source/machines.csv', sep=",", index=False)


def machinesWithDateToError():
    for file in os.listdir("source/machinesByDate/"):
        df = pd.read_csv("source/machinesByDate/" + file)
        out = ""
        prev = -1
        twoCounter = 0
        notTwoCounter = 0
        for row in df.index:

            if df["STOERTXT_NR"][row] != 2 and prev != 2 and prev == -1:
                notTwoCounter += 1

            if df["STOERTXT_NR"][row] == 2 and prev == 2 and prev != -1:
                twoCounter += 1

            if df["STOERTXT_NR"][row] == 2 and prev != 2 and prev != -1:
                #out += notTwoCounter
                #out += "|0, "
                out.append(notTwoCounter + "|0, ")
                notTwoCounter = 0
                twoCounter += 1

            if df["STOERTXT_NR"][row] != 2 and prev == 2 and prev != -1:
                out += twoCounter
                out += "|1, "
                #out.append(twoCounter + "|1, ")
                twoCounter = 0
                notTwoCounter += 1

            if df["STOERTXT_NR"][row] == 2 and prev != 2 and prev == -1:
                twoCounter += 1

            if df["STOERTXT_NR"][row] != 2 and prev != 2 and prev != -1:
                notTwoCounter += 1

            prev = df["STOERTXT_NR"][row]

        print(out)






