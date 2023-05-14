import csv

def get_data(file="static\Mapping_Police_Violence.csv") -> list[dict]:
    lst = []
    with open(file, mode="r", encoding="utf-8") as f:
        reader = csv.reader(f, delimiter=",")
        for row in reader:
            data = {
                "name": row[0] if len(row[3]) != 0 else "NA",
                "age": row[1] if len(row[3]) != 0 else "NA",
                "gender": row[2] if len(row[3]) != 0 else "NA",
                "race": row[3] if len(row[3]) != 0 else "NA",
                "date": row[5] if len(row[3]) != 0 else "NA",
                "city": row[7] if len(row[3]) != 0 else "NA",
                "state": row[8] if len(row[3]) != 0 else "NA",
                "county": row[10] if len(row[3]) != 0 else "NA",
                "agency_responsible": row[11] if len(row[3]) != 0 else "NA",
                "cause_of_death": row[13] if len(row[3]) != 0 else "NA",
                "circumstance": row[14] if len(row[3]) != 0 else "NA",
                "news_link": row[17]

            }
            lst.append(data)

    return lst[1:]


