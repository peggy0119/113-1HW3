def is_valid_move(x, y, N, visited):
    """
    檢查是否在棋盤內且該格子未被訪問。
    :param x: 當前位置的行座標
    :param y: 當前位置的列座標
    :param N: 棋盤大小
    :param visited: 記錄已訪問的棋盤格
    :return: 如果可以訪問返回 True，否則返回 False
    """
    return 0 <= x < N and 0 <= y < N and not visited[x][y]

def knight_tour(N, startX, startY):
    """
    使用深度優先搜尋 (DFS) 解決騎士巡邏問題。
    :param N: 棋盤大小
    :param startX: 起始位置的行座標
    :param startY: 起始位置的列座標
    :return: 如果存在解返回 True，否則返回 False
    """
    # 騎士的 8 個可能移動方向
    moves = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), 
             (1, -2), (1, 2), (2, -1), (2, 1)]
    visited = [[False] * N for _ in range(N)]  # 初始化棋盤訪問記錄

    def dfs(x, y, visited_count):
        """
        深度優先搜尋，用於嘗試每個可能的路徑。
        :param x: 當前位置的行座標
        :param y: 當前位置的列座標
        :param visited_count: 已訪問格子的數量
        :return: 如果找到解返回 True，否則返回 False
        """
        # 訪問當前格子
        visited[x][y] = True
        visited_count += 1

        # 如果所有格子都被訪問過，則成功
        if visited_count == N * N:
            return True

        # 嘗試所有可能的移動方向
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if is_valid_move(nx, ny, N, visited):
                if dfs(nx, ny, visited_count):
                    return True

        # 如果無法繼續，回溯
        visited[x][y] = False
        return False

    # 從起始位置開始搜尋
    return dfs(startX, startY, 0)

# 主程式入口
if __name__ == "__main__":
    N = int(input("輸入棋盤大小 N: "))  # 棋盤大小
    startX, startY = map(int, input("輸入起始位置 (startX startY): ").split())  # 起始位置

    if knight_tour(N, startX, startY):
        print("找到解：True")
    else:
        print("無解：False")
