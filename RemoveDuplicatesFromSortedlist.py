# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head 
        temp_lst = []   
        
        while temp:
            temp_lst.append(temp.val)
            temp = temp.next
        
        count = Counter(temp_lst)
    
        res_lst = [k for k, v in count.items() if v == 1]        
        dum = ListNode()
        cur = dum   
        
        for i in res_lst:
            cur.next = ListNode(i)
            cur = cur.next  
        return dum.next
                
            
