import pymongo
from datetime import datetime


def record_metrics():
    try:
        client = pymongo.MongoClient("mongodb:27017")
        db = client["flask"]
        column = db["metrics"]

        today = str(datetime.today().date())

        metrics = {"date": today, "count": 1}

        try:
            result = column.find({"date": today})
            new_count = str(int(result[0]["count"]) + 1)
            query = {"date": today}
            new_values = {"$set": {"count": new_count}}
            column.update_one(query, new_values)
        except IndexError:
            column.insert_one(metrics)

    except Exception as e:
        print(e)

    finally:
        client.close()
