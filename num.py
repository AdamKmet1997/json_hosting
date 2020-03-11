example = "B00"

inp = "B00095430"

if example in inp:
    cleaned = inp[3:]
    print(example + cleaned)