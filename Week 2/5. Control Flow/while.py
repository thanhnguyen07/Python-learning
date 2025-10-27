from datetime import datetime

# now() hiển thị giờ, now().second hiển thị giây hiện tại
print(datetime.now().second)
print(datetime.now().second + 2)

wait_until = (datetime.now().second + 2) % 60
while datetime.now().second != wait_until:
    # print("still_wating")
    pass
print(f"We are at {wait_until} second!")

# Break
while True:
    if datetime.now().second == wait_until:
        print(f"We are at {wait_until} second!")
        break

# Continue
while datetime.now().second != wait_until:
    continue
    print("still_wating")
print(f"We are at {wait_until} second!")