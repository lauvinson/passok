from datetime import datetime
t = datetime.now()  # 获取当前时间
ten = int(t.replace(t.year, t.month, t.day, 10, 0, 0, 539).timestamp() * 1000) + 339

dates = {
    '2022-06-15': {'checkinDate': '2022-06-15',
                   'houseType': '1',
                   't': str(ten),
                   's': 'fa89f4813675e89a3673eee6ae5c81f3'},
    '2022-06-16': {'checkinDate': '2022-06-16',
                   'houseType': '1',
                   't': str(ten),
                   's': 'a6f5cfb43b9c4a80364eb7ed33c7a28d'},
    '2022-06-17': {'checkinDate': '2022-06-17',
                   'houseType': '1',
                   't': str(ten),
                   's': '9237aad47964e258ca3f75c613bd4efd'},
    '2022-06-18': {'checkinDate': '2022-06-18',
                   'houseType': '1',
                   't': str(ten),
                   's': '6bd6c84b00c7f47da77670f8af2f9f1f'}
}