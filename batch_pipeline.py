import pandas as pd
from datetime import datetime

# Define paths
product_path = r"C:\Users\katki\OneDrive\Data Glacier\Week_7_Deliverables\Product_Survey_Responses.csv"
service_path = r"C:\Users\katki\OneDrive\Data Glacier\Week_7_Deliverables\Service_Survey_Responses.csv"
master_path = r"C:\Users\katki\OneDrive\Data Glacier\Week_7_Deliverables\Master_Batch_Data.csv"

# Load new data
product_df = pd.read_csv(product_path)
product_df["Form Source"] = "Product Survey"

service_df = pd.read_csv(service_path)
service_df["Form Source"] = "Service Survey"

# Merge both
combined_df = pd.concat([product_df, service_df], ignore_index=True)

# Clean email
combined_df.columns = [col.strip() for col in combined_df.columns]
combined_df["Email Address"] = combined_df["Email Address"].str.strip().str.lower()

# Drop duplicates
dedup_df = combined_df.drop_duplicates(subset="Email Address")

# Add a timestamp column for audit purposes
dedup_df["Batch Timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Save/overwrite the master batch file
dedup_df.to_csv(master_path, index=False)

print("Batch job completed and master data updated.")

