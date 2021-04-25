import pandas as pd


def parse(filepath):
    df = pd.read_csv(filepath)
    df["Transaction Date"] = pd.to_datetime(df["Transaction Date"], format="%m/%d/%y")
    df = df[df["Transaction Amount"] < 0]
    report_data = []
    amount_groups = df.groupby("Transaction Amount")
    for amount, amount_group in amount_groups:
        desc_groups = amount_group.groupby("Transaction Description")
        for desc, desc_group in desc_groups:
            if len(desc_group) > 1:
                entry = {}
                entry["num_recurrence"] = len(desc_group)
                entry["amount"] = amount
                entry["desc"] = desc
                sort_by_date = desc_group.sort_values(by=["Transaction Date"], ascending=False)
                latest = sort_by_date.iloc[0]
                entry["latest_date"] = latest["Transaction Date"]
                report_data.append(entry)
    for entry in sorted(report_data, key=lambda x: (x["latest_date"], x["num_recurrence"], x["amount"]), reverse=True):
        print("Potential recurring transaction found.")
        print("Number of recurrences:", entry["num_recurrence"])
        print("Amount:", entry["amount"])
        print("Description:", entry["desc"])
        print("Latest date:", entry["latest_date"])
        print("\n")
    return None
