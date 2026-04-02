import pandas as pd

def clean_data(file_path = "../data/messy_sales_data.xlsx"):

    df = pd.read_excel(file_path = "../data/messy_sales_data.xlsx")

    print("Before:", df.shape)

    # 1. Validate columns
    required_cols = ["date", "product", "category", "price", "quantity"]

    for col in required_cols:
        if col not in df.columns:
            raise Exception(f"Missing column: {col}")

    # 2. Remove duplicates
    df = df.drop_duplicates()

    # 3. Handle missing values
    df["price"] = df["price"].fillna(df["price"].median())
    df["quantity"] = df["quantity"].fillna(1)

    # 4. Convert types
    df["date"] = pd.to_datetime(df["date"])

    # 5. Remove invalid rows
    df = df[df["price"] > 0]

    # 6. Feature Engineering
    df["revenue"] = df["price"] * df["quantity"]

    print("After:", df.shape)

    return df