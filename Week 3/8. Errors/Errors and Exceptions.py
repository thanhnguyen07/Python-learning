def causeError():
    return 1/0

causeError()

def causeError():
    return 1/0

def callCauseError():
    return causeError()

callCauseError()

try:
    1/0
except Exception as e:
    print(type(e))