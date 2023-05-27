def fn():
    arr = []
    f = open("input.in","r")
    lines = f.readlines()
    currSum = 0
    maxSum = 0
    for line in lines:
        if line == '\n':
            arr.append(currSum)
            currSum = 0
            continue
        currSum += int(line)
    arr.append(currSum)
    arr.sort(reverse=True)
    ans = arr[0]+arr[1]+arr[2]
    print(ans)
fn()
