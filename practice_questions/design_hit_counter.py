"""
URL: https://leetcode.com/problems/design-hit-counter/
"""


class HitCounter:

    def __init__(self):
        self.hit_counter = {}

    def hit(self, timestamp: int) -> None:
        self.hit_counter[timestamp] = self.hit_counter.get(timestamp, 0) + 1

    def getHits(self, timestamp: int) -> int:
        if len(self.hit_counter) == 0:
            return 0
        total_hits = 0
        current_time = timestamp
        while current_time >= 0 and timestamp - current_time < 300:
            total_hits += self.hit_counter.get(current_time, 0)
            current_time -= 1
        return total_hits


if __name__ == '__main__':
    # Your HitCounter object will be instantiated and called as such:
    counter = HitCounter()
    counter.hit(1)
    counter.hit(2)
    counter.hit(3)
    print(f'Should be 3: {counter.getHits(4)}')
    counter.hit(300)
    print(f'Should be 4: {counter.getHits(300)}')
    print(f'Should be 3: {counter.getHits(301)}')
