def calculate_kpis(df):

    total_revenue = df["revenue"].sum()
    total_orders = len(df)
    avg_order_value = total_revenue / total_orders

    top_product = df.groupby("product")["revenue"].sum().idxmax()
    top_category = df.groupby("category")["revenue"].sum().idxmax()

    return {
        "Total Revenue": round(total_revenue, 2),
        "Total Orders": total_orders,
        "Avg Order Value": round(avg_order_value, 2),
        "Top Product": top_product,
        "Top Category": top_category
    }