from typing import List


class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        x = y = di = 0
        obstacleSet = set(map(tuple, obstacles))
        ans = 0
        for cmd in commands:
            if cmd == -2:  # left
                di = (di - 1) % 4
            elif cmd == -1:  # right
                di = (di + 1) % 4
            else:
                for k in range(cmd):
                    if (x+dx[di], y+dy[di]) not in obstacleSet:
                        x += dx[di]
                        y += dy[di]
        ans = max(ans, x*x + y*y)
        return ans
        def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            ans = x = y = di = 0
            obstacleSet = set(map(tuple, obstacles))
            for cmd in commands:
                if cmd == -2:
                    di = (di+3) % 4
                elif cmd == -1:
                    di = (di+1) % 4
                else:
                    for k in range(cmd):
                        if (x+directions[di][0], y + directions[di][1]) not in obstacleSet:
                            x += directions[di][0]
                            y += directions[di][1]
                            ans = max(ans, x*x+y*y
            return ans



if __name__ == "__main__":
    commands, obstacles = [4, -1, 4, -2, 4], [[2, 4]]
    print(Solution().robotSim(commands, obstacles))
