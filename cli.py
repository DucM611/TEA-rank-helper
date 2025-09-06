import json

with open('faucets.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print('Danh sách Faucet / Campaign:')
for item in data:
    print(f"- {item['name']}: {item['url']}")
