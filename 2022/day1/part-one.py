def fn():
    f = open("input.in","r")
    lines = f.readlines()
    currSum = 0
    maxSum = 0
    for line in lines:
        if line == '\n':
            maxSum = max(maxSum,currSum)
            currSum = 0
            continue
        currSum += int(line)

    print(max(maxSum,currSum))
fn()
