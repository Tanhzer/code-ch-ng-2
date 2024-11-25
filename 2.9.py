import json
data = {
    "company": {
        "name": "GeeksForGeeks Company",
        "location": "India",
        "staff": [
            {
                "id": 3,
                "name": "Anthony Walter",
                "salary": "3.2 LPA"
            },
            {
                "id": 1,
                "name": "Amar Pandey",
                "salary": "8.5 LPA"
            },
            {
                "id": 2,
                "name": "Akbhar Khan",
                "salary": "6.5 LPA"
            }
        ]
    }
}
dulieu_json = json.dumps(data, sort_keys=True, indent=4)
print("JSON string:\n", dulieu_json)
