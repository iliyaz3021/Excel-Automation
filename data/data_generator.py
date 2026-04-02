import pandas as pd
import random

def generate_data(rows=2000):

    products = ["Phone", "Laptop", "Shirt", "Shoes", "Watch"]

    data = []

    for _ in range(rows):

        product = random.choice(products)

        if product in ["Phone", "Laptop"]:
            category = "Electronics"
            price = random.choice([30000, 50000, None])
        else:
            category = "Fashion"
            price = random.choice([1000, 2000, None])

        quantity = random.choice([1, 2, 5, None])

        date = pd.to_datetime("2024-01-01") + pd.to_timedelta(random.randint(0, 30), unit="D")

        data.append([date, product, category, price, quantity])

    df = pd.DataFrame(data, columns=["date", "product", "category", "price", "quantity"])

    # Add duplicates
    df = pd.concat([df, df.sample(100)])

    df = df.sample(frac=1)

    df.to_csv("data/messy_sales_data.csv", index=False)

    print("Messy data created!")

if __name__ == "__main__":
    generate_data()