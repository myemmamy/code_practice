# https://www.hackerrank.com/challenges/minimum-time-required/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=search
#
# You are planning production for an order. You have a number of machines that each have a fixed number of days to produce an item.
# Given that all the machines operate simultaneously, determine the minimum number of days to produce the required order.
#
# For example, you have to produce goal=10 items. You have three machines that take machines=[2,3,2] days to produce an item.
# It takes 8 days to produce 10 items using these machines.

def minTime(machines, goal):
    from functools import reduce
    fday = int(goal / len(machines) * min(machines))
    sday = int(goal / len(machines) * max(machines))

    def binaryCheck(fday, sday):
        if sday == fday:
            return sday
        mday = (sday + fday) // 2
        if mday == fday: # in a case, sday is just 1 bigger than fday, then need to return sday to make sure all goal are produced.
            return sday
        arr = [int(mday / i) for i in machines]
        amount = sum(arr)
        if amount == goal:
            cday = mday #could be a few days without total amount change, so need to find the smallest one
            while True:
                if sum([int(cday/i) for i in machines]) == goal:
                    cday -= 1
                else:
                    return cday+1

        elif amount > goal:
            return binaryCheck(fday, mday)
        else:
            return binaryCheck(mday, sday)

    return binaryCheck(fday, sday)


if __name__ == '__main__':
    nGoal = input().split()

    n = int(nGoal[0])

    goal = int(nGoal[1])

    machines = list(map(int, input().rstrip().split()))
    arr=[int(304844592/i) for i in machines]

    print(sum(arr))

    ans = minTime(machines, goal)

    print(ans)
    narr=[int(ans/i) for i in machines]
    print(sum(narr))
