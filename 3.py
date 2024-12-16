def josephus(n, k):
    """
    解決約瑟夫問題，找出最後存活的人的編號。
    :param n: 總人數
    :param k: 每次刪除第 k 個人
    :return: 最後存活的人的編號
    """
    # 初始化所有人的編號，從 1 到 n
    people = list(range(1, n + 1))
    index = 0  # 記錄當前需要刪除的位置

    # 模擬過程，直到只剩下一個人
    while len(people) > 1:
        # 計算下一個被刪除的位置，考慮環狀列表
        index = (index + k - 1) % len(people)
        people.pop(index)  # 刪除該位置的人

    # 返回最後存活的人的編號
    return people[0]

# 主程式入口
if __name__ == "__main__":
    n, k = map(int, input("輸入總人數 n 和間隔數 k（以空格分隔）：").split())
    print(f"最後存活的人的編號是：{josephus(n, k)}")
