def rangeSumBST(root, l, r):
    ans = 0
    def dfs(node, ans):
        if node:
            if l <= node.val <= r:
                ans += node.val
            if l < node.val:
                dfs(node.left, ans)
            if node.val < r:
                dfs(node.right, ans)

    dfs(root)
    return ans
