import requests
import time
import matplotlib.pyplot as plt

# Flask 서버의 URL
BASE_URL = "http://localhost:5000"

# 측정 데이터를 저장할 리스트
response_times = {'Create': [], 'Read': [], 'Update': [], 'Delete': []}

# Create
start_time = time.time()
response = requests.post(f"{BASE_URL}/item", json={"name": "New Item"})
response_times['Create'].append(time.time() - start_time)

# Read
item_id = response.json()['id']
start_time = time.time()
response = requests.get(f"{BASE_URL}/item/{item_id}")
response_times['Read'].append(time.time() - start_time)

# Update
start_time = time.time()
response = requests.put(f"{BASE_URL}/item/{item_id}", json={"name": "Updated Item"})
response_times['Update'].append(time.time() - start_time)

# Delete
start_time = time.time()
response = requests.delete(f"{BASE_URL}/item/{item_id}")
response_times['Delete'].append(time.time() - start_time)

# 결과 출력
print(response_times)

# 결과 시각화
labels, times = zip(*response_times.items())
plt.bar(labels, [sum(t)/len(t) for t in times], color=['blue', 'green', 'yellow', 'red'])
plt.xlabel('CRUD Operations')
plt.ylabel('Average Response Time (seconds)')
plt.title('CRUD Operations Performance')
plt.show()