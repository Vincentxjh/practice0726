phonebill_list = ['0分钟', '50分钟', '100分钟', '300分钟', '不限量']
flow_list = ['0M', '500M', '1G', '5G', '不限量']
message_list = ['0条', '50条', '100条']
print("定制自己的手机套餐：")

print("A请设置通话时长：")
for index,value in enumerate(phonebill_list):
    print(index+1,value)
mealset = int(input("输入选择的通话时长编号："))
mealselect = phonebill_list[mealset-1]

print("\nB请设置流量包：")
for index,value in enumerate(flow_list):
    print(index+1,value)
flowset = int(input("输入选择的通话时长编号："))
flowselect = flow_list[flowset-1]

print("\nC请设置短信条数：")
for index,value in enumerate(message_list):
    print(index+1,value)
messageset = int(input("输入选择的通话时长编号："))
messageselect = message_list[messageset-1]

print("\n你的手机套餐定制成功，免费通话时长为" + mealselect + "/月，流量为"
      + flowselect + "/月，短信条数为" + messageselect + "/月")