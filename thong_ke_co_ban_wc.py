
import statistics

# Dữ liệu mẫu
data = [12, 15, 14, 10, 60
, 15, 18, 20, 15, 14]

# Thống kê cơ bản
mean = statistics.mean(data)
median = statistics.median(data)
stdev = statistics.stdev(data)

# In kết quả
print("Trung bình:", mean)
print("Trung vị:", median)
print("Độ lệch chuẩn:", stdev)