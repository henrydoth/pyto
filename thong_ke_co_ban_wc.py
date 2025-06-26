import statistics

# Dữ liệu mẫu
data = [12, 15, 14, 10, 60
, 15, 18, 20, 15, 14]

# Thống kê cơ bản
mean = round(statistics.mean(data), 2)
median = round(statistics.median(data), 2)
stdev = round(statistics.stdev(data), 2)
mode = statistics.mode(data)
minimum = min(data)
maximum = max(data)
variance = round(statistics.variance(data), 2)

# In kết quả
print("Trung bình:", mean)
print("Trung vị:", median)
print("Độ lệch chuẩn:", stdev)
print("Mode:", mode)
print("Giá trị nhỏ nhất:", minimum)
print("Giá trị lớn nhất:", maximum)
print("Phương sai:", variance)