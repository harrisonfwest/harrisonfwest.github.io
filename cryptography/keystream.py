init = [1, 0, 1, 0, 1]
count = 1
while True:
    print('   ', count, '&', init[0], '&', init[1], '&', init[2], '&', init[3], '&', init[4], '\\\\')
    temp = init
    init = [(temp[1] + temp[4])%2, temp[0], temp[1], temp[2], temp[3]]
    count += 1
    if init == [1, 0, 1, 0, 1]:
        print('   ', count, '&', init[0], '&', init[1], '&', init[2], '&', init[3], '&', init[4], '\\\\')
        input()