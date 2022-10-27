import pandas
import matplotlib.pyplot as plot
import seaborn as sns


def printFlowers():
    df = pandas.read_csv(".\\source\\iris.csv", delimiter= ';')
    sns.set_style("whitegrid")
    sns.pairplot(df, hue="Species")

    plot.show()


def printAirport():
    df = pandas.read_csv('.\\source\\airports.csv', delimiter=',')
    sns.set_style("whitegrid")
    sns.pairplot(df, hue="state", height= 20)

    plot.show()


def printCrossFlowers():
    df = pandas.read_csv(".\\source\\iris.csv", delimiter=';')
    print(df)
    df.drop(["ID", "Species"], axis=1)
    print(df)
    print("----------------------------------------------------------------------")
    print(df.corr())
    print("----------------------------------------------------------------------")
    print(df.cov())


'''
x = df["Sepal.Length"].values
    y = df["Sepal.Width"].values
    fig = plot.figure()
    ax1 = fig.add_subplot(211)
    ax1.xcorr(x, y, usevlines=True, maxlags=5, normed=True, lw=2)
    ax1.grid(True)
    ax1.axhline(0, color='blue', lw=2)
    plot.show()

'''

