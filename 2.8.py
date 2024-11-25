import json
data = {
    "company": {
        "name": "GeeksForGeeks Company",
        "staff": [
            {
                "id": 1,
                "name": "Amar Pandey",
                "salary": "8.5 LPA"
            },
            {
                "id": 2,
                "name": "Akbhar Khan",
                "salary": "6.5 LPA"
            },
            {
                "id": 3,
                "name": "Anthony Walter",
                "salary": "3.2 LPA"
            }
        ]
    }
}
dulieu_json = json.dumps(data, indent=4)
print("JSON string:\n", dulieu_json)
print("\nAll:")
print("Tên Cty:", data["company"]["name"])
for staff in data["company"]["staff"]:
    print("nhân viên ID:", staff["id"])
    print("tên nhân viên:", staff["name"])
    print("lương nhân viên:", staff["salary"])
    print()
