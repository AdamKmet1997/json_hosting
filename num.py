import json , requests
example = "B00"

inp = "B00095430"
number = example + inp[3:]
day = "Wed"
response = requests.get('https://adamkmet1997.github.io/json_hosting/data.json')
data = json.loads(response.text)
print(number)

for v in data:
    if number in v['sNumber']:
        answer = v["subject"],v["time"],v["room"]
print(answer)

# if example in inp:
#     cleaned = inp[3:]
#     print(example + cleaned)

