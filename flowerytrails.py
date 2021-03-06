import sys

sys.setrecursionlimit(3000)


def inp():
    first_line = input().split(" ")
    num_points, num_trails = int(first_line[0]), int(first_line[1])
    adj_lst = {i: set() for i in range(num_points)}
    trail_len = {}
    trail_len_duplicate_count = {}
    for i in range(num_trails):
        trail = input().split(" ")
        node1, node2, length = int(trail[0]), int(trail[1]), int(trail[2])
        if node1 != node2:
            adj_lst[node1].add(node2)
            adj_lst[node2].add(node1)
            key = frozenset((node1, node2))
            if key not in trail_len or length < trail_len[key]:
                trail_len[key] = length
                trail_len_duplicate_count[key] = 1
            elif length == trail_len.get(key):
                trail_len_duplicate_count[key] += 1
    return num_points, adj_lst, trail_len, trail_len_duplicate_count


def main():
    num_points, adj_lst, trail_len, trail_len_duplicate_count = inp()
    shortest_path = 0
    flower_path = set()

    def dfs_recur(current_node, path, length):
        # print(path)
        nonlocal shortest_path, flower_path
        if shortest_path and length > shortest_path:
            return
        if current_node == num_points - 1:
            edges = set(frozenset((path[i], path[i+1])) for i in range(len(path) - 1))
            if not shortest_path or length < shortest_path:
                flower_path = edges
                shortest_path = length
            elif length == shortest_path:
                flower_path |= edges
        else:
            for node in adj_lst[current_node]:
                edge_len = trail_len[frozenset((current_node, node))]
                if node not in path:
                    path.append(node)
                    dfs_recur(node, path, length + edge_len)
                    path.pop()

    dfs_recur(0, [0], 0)
    # print(flower_path)
    return sum(trail_len[path] * trail_len_duplicate_count[path] for path in flower_path) * 2

if __name__ == '__main__':
    # from time import clock
    # start_time = clock()
    print(main())
    # print("Time =  {:.4f}".format(clock() - start_time))
