def main():
    while (True):
        rlfdl = list(map(int, input().split()))

        if rlfdl[0] == 0 and rlfdl[1] == 0 and rlfdl[2] == 0:
            break

        rlfdl.sort()

        if rlfdl[0]**2 + rlfdl[1]**2 == rlfdl[2]**2:
            print('right')
        else:
            print('wrong')

if __name__ == '__main__':
    main()