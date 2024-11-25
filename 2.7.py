import json
dulieu_json = '''
{
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
'''
data = json.loads(dulieu_json)
print(data)
print("Tên Cty:", data["company"]["name"])
for nhan_vien in data["company"]["staff"]:
    print("nhân viên ID:", nhan_vien["id"])
    print("tên nhân viên :", nhan_vien["name"])
    print("lương nhân viên:", nhan_vien["salary"])
    print()
