#
#creator:lvjunjie
#time:2020-04-05 AM 07:33
#
import os
file_Dir="test.txt"
input_Data=[]
data=open(file_Dir,"r",encoding='UTF-8')
input_Data=data.read()
print(input_Data,type(input_Data),len(input_Data))
input_Data_Length=len(input_Data)
print(input_Data_Length)
list1=[]
for line in input_Data:
   print(line.strip().split(','))
print(list1)
###########################################
data=open(file_Dir,"r",encoding="UTF-8")
#print(type(data),data)
lines=data.readlines()
print(lines,type(lines))
for line in lines:
    data=line.strip().split(',')
    print(data)
n1=input('请输入序列的长度:')
print("您输入的序列长度为",int(n1))
n2=input("请输入指定序列长度的数据")
n2=n2.split(",")
print("您输入的序列为:",n2)
# for i,m in enumerate(n2):
#     print(i,m)
for i in range(len(n2)-1):
    # print(n2[i])
    index_ex=abs(int(n2[i])-int(n2[i+1]))
    max=2**index_ex
    if(1<=max<=10000):
        print(max)


n=[4,1,2,5,3]
n2=[1,2,3,4,5]
n1=sorted(n)
# print(n)
# print(n1)
# print(n.pop(0))
# print(n)
for i in range(len(n)-1):
    minIndex=i
    j=i+1
    for j in range(len(n)):
        if(n[j]>n[minIndex]):#如果第i个位置不是最小值，则把第i个位置放置最后
            minIndex=j
            print(n[i])
            # n.append(n[i])#把n[i]最后位置添加一个元素
            # n.pop(0)  # 移除第一个元素
            print(n)
    # if (i != minIndex){
    #     swap(a[i], a[minIndex]);
    # }




# min=n[0]
# cishu=0
# for i in range(len(n)):
#     j=i+1
#     for j in range(len(n)):
#         if(n[i]>n[j]):



# n3=[]
# print(n2)
# for i in n2:
#     print(i)
#     n3.append(i)
# print(n3,type(n3))
# for i in range(int(n1)):
#     print(i)
# n = eval(input())
# a = list(map(int,input().split()))
# b = sorted(a)
n=5
a= [87, 3, 1, 6, 44, 10]
a1=[1, 3, 6, 10, 44, 87]
    # 1 3  87 10  44   6
    # 1 3  10 44   6   87
    # 1 3  44  6   87  10
    # 1 3   6  87  10  44
    # 1 3   6  10  44  87
    # 4 1 2 5 3
    # 1 2 3 4 5
n = int(input("输入数目").strip())
a = list(map(int, input("输入数组").strip().split()))
while(n!=len(a)):
    print("输入数目与输入数组不相等，请重新输入")
    n = int(input("输入数目").strip())
    a = list(map(int, input("输入数组").strip().split()))
b=sorted(a)
count = 0
print(a)
print(b)
for i in range(n):
    while a[i] != b[i]:#当数据不相等时，把当前值数据追加放入尾部，把当前值数据删除，知道相等。
            print(i,a[i],b[i])
            a.append(a[i])
            a.pop(i)
            count += 1
            print(a)
        # print(b)

print(count)
#
# def min_swaps(nums):
#     # mp记录排序后数值应在的正确位置
#     mp = {}
#     sort_nums = sorted(nums)
#     for i in range(len(sort_nums)):
#         mp[sort_nums[i]] = i
#
#     # 循环节个数
#     lops = 0
#     # 该位置的数是否被访问过
#     flags = []
#     for i in range(len(nums)):
#         flags.append(False)
#     for i in range(len(nums)):
#         if not flags[i]:
#             j = i
#             while not flags[j]:
#                 flags[j] = True
#                 # j是当前值应在的正确位置
#                 j = mp[nums[j]]
#             lops += 1
#     return len(nums) - lops
#
#
# case = int(input().strip())
# while case:
#     size = int(input("输入数目").strip())
#     nums = list(map(int, input("输入数组").strip().split()))
#     print(min_swaps(nums))
#     case -= 1
#
num=int(input("输入含有偶数的个数").strip())
data=list(map(int,input().strip().split()))
dataLength=len(data)
count=0
for i in range(dataLength):
        if data[i]%2==0:
           count+=1;
while(count<1):
    print("请输入至少一个偶数")
    num = int(input("输入含有偶数的个数").strip())
    data = list(map(int, input().strip().split()))
    dataLength = len(data)
    for i in range(dataLength):
        if data[i] % 2 == 0:
            count += 1;
result=[]
print(data)
for i in range(dataLength):
        if data[i]%2==0:
           result.append(data[i])

print(result)
list2=[str(i) for i in result]
print(list2)
print(" ".join(list2))






