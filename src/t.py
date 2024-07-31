import math
from scipy.stats import norm

# Các tham số đầu vào
S0 = 100  # Giá cổ phiếu hiện tại
K = 105   # Giá thực hiện quyền chọn
T = 1     # Thời gian đến ngày đáo hạn (1 năm)
r = 0.02  # Lãi suất phi rủi ro cố định (2%)
sigma = 0.25 # Độ biến động của cổ phiếu

# Công thức Black-Scholes
d1 = (math.log(S0 / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * math.sqrt(T))
d2 = d1 - sigma * math.sqrt(T)

# Tính giá trị lý thuyết của quyền chọn mua (call option)
call_price = S0 * norm.cdf(d1) - K * math.exp(-r * T) * norm.cdf(d2)

print(f"Giá trị lý thuyết của quyền chọn mua: {call_price:.2f}")
