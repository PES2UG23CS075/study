import requests
import time

# Example benchmarking using requests library
url = 'http://localhost:5000/generate'
prompt = {'prompt': 'Your prompt text here.'}

# Measure response time for multiple requests
num_requests = 10
start_time = time.time()
for _ in range(num_requests):
    response = requests.post(url, json=prompt)
    # Optionally print response or process data
total_time = time.time() - start_time
print(f'Total time for {num_requests} requests: {total_time} seconds')
print(f'Average time per request: {total_time / num_requests} seconds')
