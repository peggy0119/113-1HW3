def is_full(stack, top, capacity):
    """
    判斷堆疊是否已滿。
    :param stack: 堆疊
    :param top: 堆疊頂端的索引
    :param capacity: 堆疊的容量
    :return: 如果已滿返回 True，否則返回 False
    """
    return top == capacity - 1  # 如果頂端索引等於容量減一，則堆疊已滿

def is_empty(stack, top):
    """
    判斷堆疊是否為空。
    :param stack: 堆疊
    :param top: 堆疊頂端的索引
    :return: 如果為空返回 True，否則返回 False
    """
    return top == -1  # 如果頂端索引為 -1，則堆疊為空
