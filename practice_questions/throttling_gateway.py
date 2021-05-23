"""
The gateway has the following limits:

The number of transactions in any given second cannot exceed 3.
The number of transactions in any given 10 second period cannot exceed 20. A ten-second period includes all requests arriving from any time max(1, T-9) to T (inclusive of both) for any valid time T.
The number of transactions in any given minute cannot exceed 60. Similar to above, 1 minute is from max(1, T-59) to T.
Any request that exceeds any of the above limits will be dropped by the gateway. Given the times at which different requests arrive sorted ascending, find how many requests will be dropped.

Note: Even if a request is dropped it is still considered for future calculations. Although, if a request is to be dropped due to multiple violations, it is still counted only once.

Example
n = 27
requestTime = [1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 7, 11, 11, 11, 11 ]
Request 1 - Not Dropped.
Request 1 - Not Dropped.
Request 1 - Not Dropped.
Request 1 - Dropped. At most 3 requests are allowed in one second.
No request will be dropped till 6 as all comes at an allowed rate of 3 requests per second and the 10-second clause is also not violated.
Request 7 - Not Dropped. The total number of requests has reached 20 now.
Request 7 - Dropped. At most 20 requests are allowed in ten seconds.
Request 7 - Dropped. At most 20 requests are allowed in ten seconds.
Request 7 - Dropped. At most 20 requests are allowed in ten seconds. Note that the 1-second limit is also violated here.
Request 11 - Not Dropped. The 10-second window has now become 2 to 11. Hence the total number of requests in this window is 20 now.
Request 11 - Dropped. At most 20 requests are allowed in ten seconds.
Request 11 - Dropped. At most 20 requests are allowed in ten seconds.
Request 11 - Dropped. At most 20 requests are allowed in ten seconds. Also, at most 3 requests are allowed per second.
Hence, a total of 7 requests are dropped.

Function Description
Complete the droppedRequests function in the editor below.
droppedRequests has the following parameter(s):
int requestTime[n]: an ordered array of integers that represent the times of various requests
Returns
int: the total number of dropped requests
Constraints
1 ≤ n ≤ 106
1 ≤ requestTime[i] ≤ 109
Input Format For Custom Testing
Sample Case 0
Sample Input For Custom Testing
STDIN Function
----- --------
5 → requestTime[] size n = 5
1 → requestTime = [ 1, 1, 1, 1, 2 ]
1
1
1
2
Sample Output
1
Explanation
There are 4 requests that arrive at second 1. This exceeds the per second limit so one packet is dropped. No other limits are exceeded.
"""

from collections import Counter, defaultdict


def dropped_requests(requests_times):
    total_dropped = 0
    count = Counter(requests_times)
    for index, time in enumerate(requests_times):
        if count[time] > 3:
            difference = count[time] - 3
            count[time] = 3
            total_dropped += difference
        num_transactions_past_ten_seconds = num_transactions(count, 10, time)
        if num_transactions_past_ten_seconds > 20:
            difference = count[time] - (num_transactions_past_ten_seconds - 20)
            count[time] = count[time] - difference
            total_dropped += difference
        num_transactions_past_sixty_seconds = num_transactions(count, 60, time)
        if num_transactions_past_sixty_seconds > 60:
            difference = count[time] - (num_transactions_past_sixty_seconds - 60)
            count[time] = count[time] - difference
            total_dropped += difference
    return total_dropped


def num_transactions(count, past_seconds, current_time):
    total = 0
    remaining_request_times = sorted(count.keys())
    starting_time = current_time - past_seconds
    if starting_time < 0:
        starting_time = 0
    for time in remaining_request_times:
        if time < starting_time or time > current_time:
            continue
        total += count[time]
    return total


def droppedRequests(requestTime):
    if len(requestTime) <= 3: return 0
    count = Counter(requestTime)
    lookup = defaultdict(int)
    for i in range(requestTime[0], requestTime[-1] + 1):
        lookup[i] = lookup[i - 1] + count[i]
    for i in range(3, len(requestTime)):
        temp1, temp2 = 0, 0
        if requestTime[i] - 10 in lookup: temp1 = lookup[requestTime[i] - 10]
        if requestTime[i] - 60 in lookup: temp2 = lookup[requestTime[i] - 60]
        if requestTime[i - 3] == requestTime[i]:
            requestTime[i - 3] = '$'
        elif i + 1 - temp1 > 20:
            requestTime[i] = '$'
        elif i + 1 - temp2 > 60:
            requestTime[i] = '$'
    return requestTime.count('$')


if __name__ == '__main__':
    request_times = [1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 7, 11, 11, 11, 11]
    # # dropped_requests(request_times)
    # print(droppedRequests(request_times))
    print(dropped_requests(request_times))
