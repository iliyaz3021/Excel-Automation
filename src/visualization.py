import matplotlib.pyplot as plt

def create_charts(df):

    # Category chart
    cat = df.groupby("category")["revenue"].sum()

    plt.figure()
    cat.plot(kind="bar")
    plt.title("Revenue by Category")
    plt.savefig("output/category.png")

    # Time chart
    time = df.groupby("date")["revenue"].sum()

    plt.figure()
    time.plot()
    plt.title("Revenue Over Time")
    plt.savefig("output/time.png")