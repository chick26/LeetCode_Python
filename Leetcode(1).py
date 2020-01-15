import math
import numpy as np

#Two Sum
class Solution_TwoSum:
    def twoSum(self, nums, target):
        hashmap={}
        for i,num in enumerate(nums):
            if hashmap.get(target - num) is not None:
                print(nums[i],nums[hashmap.get(target - num)])
                return [i,hashmap.get(target - num)]
            hashmap[num] = i #这句不能放在if语句之前，解决list中有重复值或target-num=num的情况

#Decompress
class Solution_Decompress:
    def decompressRLElist(self,nums):
        list=[]
        for i in range(0,len(nums),2):
            for j in range(nums[i]):
                list.append(nums[i+1])
        return list
    def decompressUsingZip(self,nums):
        return sum( (a*[b] for a,b in zip(nums[::2],nums[1::2])), [])
    #SUM的写法3.7.1弃用

#Product&Sum
class Solution_ProductandSum:
    def subtractProductAndSum(self, n: int):
        _sum=0
        _product=1
        for i in str(n):
            _sum+=int(i)
            _product*=int(i)
        return _product-_sum

    def subtractProductAndSumUsingRemainder(self,n:int):
        _sum=0
        _product=1
        while n>0:
            digit=n%10
            n=int(n/10)
            _sum+=digit
            _product*=digit
        return _product-_sum

#Find Numbers with Even Number of Digits
class Solution_FindEvenDigit:
    def findNumbers(self, nums):
        Num_EvenNumber=0
        for num in nums:
            if len(str(num))%2==0:
                Num_EvenNumber+=1
        return Num_EvenNumber

    def findNumbersUsingLog(self, nums):
        Num_EvenNumber=0
        for num in nums:
            if int(math.log10(num)+1)%2==0:
                Num_EvenNumber+=1
        return Num_EvenNumber

#Jewels and Stones
class Solution_JewelsandStones:
    def numJewelsInStones(self, J: str, S: str):
        Num_Jewel=0
        for Stone in S:
            for Jewel in J:
                if Stone==Jewel:
                    Num_Jewel+=1
        return Num_Jewel
    
    def numJewelsInStonesUsingOneline(self, J: str, S: str):
        return sum([S.count(x) for x in J])

#Defanging an IP Address
class Solution_DefangingIP:
    def defangIPaddr(self, address: str):
        #str_list=list(address)
        pos=[]
        for i in range(len(address)):
            if address[i]=='.':
                pos.append(i)
        str_list=list(address)
        for i in range(3):
            str_list.insert(pos[i]+i*2,'[')
            str_list.insert(pos[i]+2+i*2,']')
        address=''.join(str_list)
        return address
    
    def defangIPaddrOnelineUsingReplace(self, address):
        return address.replace(".","[.]")
'''
    def defangIPaddrOnelineUsingSplit(self, address):
        return '[.]'.join(address.split("."))
'''

#Minimum Time Visiting All Points
class Solution_MinimumTimeVisitingAllPoints:
    def minTimeToVisitAllPoints(self, points):
        _time=0
        for current_point_index in range(len(points)-1):
            current_point=points[current_point_index]
            next_point=points[current_point_index+1]
            _x=abs(current_point[0]-next_point[0])
            _y=abs(current_point[1]-next_point[1])
            _time+=max(_x,_y)
        return _time

#Convert Binary Number in a Linked List to Integer
'''
输入：head = [1,0,1]
输出：5
解释：二进制数 (101) 转化为十进制数 (5)
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution_BinaryInLinkedList:
    def getDecimalValue(self, head: ListNode):
        rec = 0
        while head != None:  
            rec = rec * 2 + head.val # 相当于rec = rec<<1 | head.val
            head = head.next
        print(rec)
        return rec
'''
List=ListNode(1)
List.next=ListNode(0)
List.next.next=ListNode(1)
'''
#Delete Node in a Linked List
class Solution_DeleteNodeLinkedList:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        return 0

list=ListNode(1)
list.next=ListNode(0)
list.next.next=ListNode(1)
print(len(list))