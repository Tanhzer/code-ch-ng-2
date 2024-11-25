import json
from collections import Counter
with open('company_data.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
ten_cty = data['company']['name']
dia_chi_cty = data['company']['address']
nhan_vien = data['employees']
tong_so_nv = len(nhan_vien)
thong_ke_nv = Counter([emp['department'] for emp in nhan_vien])
print(f"Tên công ty: {ten_cty}")
print(f"Địa chỉ: {dia_chi_cty}")
print("--- Thống kê nhân viên theo đơn vị ---")
for i, (don_vi, dem) in enumerate(thong_ke_nv.items(), 1):
    ty_le = (dem / tong_so_nv) * 100
    print(f"{i}./ Tên đơn vị: {don_vi}")
    print(f"   Số nhân viên: {dem}")
    print(f"   Tỷ lệ: {ty_le:.2f}%")