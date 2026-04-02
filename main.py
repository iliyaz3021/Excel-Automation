from src.data_cleaning import clean_data
from src.kpi import calculate_kpis
from src.visualization import create_charts
from src.report import generate_report

file = "../data/messy_sales_data.xlsx"

df = clean_data(file)

kpis = calculate_kpis(df)

create_charts(df)

generate_report(df, kpis)

print("Project Completed!")