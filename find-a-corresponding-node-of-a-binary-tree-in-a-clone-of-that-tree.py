class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        if not original:
            return None
            
        stack = collections.deque([(original, cloned)])
        
        while stack:
            og, clone = stack.popleft()
            if og == target:
                return clone
            if og.left:
                stack.append((og.left, clone.left))
            if og.right:
                stack.append((og.right, clone.right))
                
        return None 