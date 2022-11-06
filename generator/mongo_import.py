import pandas as pd
from db.db import posts
import json

def mongoimport(csv_path, collection):
    data = pd.read_csv(csv_path)
    payload = json.loads(data.to_json(orient='records'))
    collection.insert_many(payload)


if __name__ == '__main__':
    mongoimport('posts.csv', posts)
