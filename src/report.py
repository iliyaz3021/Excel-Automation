import pandas as pd

def generate_report(df, kpis):

    with pd.ExcelWriter("output/report.xlsx") as writer:

        df.to_excel(writer, sheet_name="Cleaned Data", index=False)

        kpi_df = pd.DataFrame(list(kpis.items()), columns=["Metric", "Value"])
        kpi_df.to_excel(writer, sheet_name="KPIs", index=False)