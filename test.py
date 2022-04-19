# 製作排班表，先以簡單的1周班表安排
# 7天裡有分早晚班，當天班次不能有人出現兩次

staff_list = ["芬", "宜", "容", "蓉", "舒", "蓮", "惠"]
staff_nums = len(staff_list) # 工作人數

print("There are total {} staff".format(staff_nums))

# 隨機將staff_list洗牌
from random import shuffle
from random import sample # 挑選指定數量的東西出來
shuffle(staff_list)
order_list_morning = sample(staff_list, 7)
order_list_night = sample(staff_list, 7)

# 製作簡單的班表顯示表
week_list = ["日", "一", "二", "三", "四", "五", "六"]
morning_list = order_list_morning
night_list = order_list_night

# 測試: 在不斷生成班表時，讓程式判斷當天早晚班派同一人的狀況並且報錯
for i in range(7):
    if morning_list[i] == night_list[i]:
        print("重疊")
        # print(morning_list) # 隨機洗牌後的結果
        # print(night_list)
        break
    else:
        print(week_list)
        print(morning_list) # 隨機洗牌後的結果
        print(night_list)
        print("===" * 20)