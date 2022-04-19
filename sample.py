from random import shuffle
from random import sample
import numpy as np
import xlwt


name_list = ['田','兰','刘','杨','余','唐','于','莫','吴','乔','敏','童','杜','王','豆','黄','苹','磊','曼','陈','皱','谢','果','汪','麒']
name_list_size = len(name_list)

print("The are total {} people".format(name_list_size))

def get_matrix():
    while 1:
        row_1 = sample(name_list, 5)
        row_2 = sample(name_list, 5)
        row_3 = sample(name_list, 5)
        row_4 = sample(name_list, 5)
        row_5 = sample(name_list, 5)
        row_6 = sample(name_list, 5)
        row_7 = sample(name_list, 5)
        row_8 = sample(name_list, 5)
        row_9 = sample(name_list, 5)
        row_10 = sample(name_list, 5)

	#get a matrix for 10x5 array
        matrix = np.array([row_1,row_2,row_3,row_4,row_5,row_6,row_7,row_8,row_9,row_10])

        col_1 = matrix[:,0]
        col_2 = matrix[:,1]
        col_3 = matrix[:,2]
        col_4 = matrix[:,3]
        col_5 = matrix[:,4]

        set_col_1 = set(col_1)
        set_col_2 = set(col_2)
        set_col_3 = set(col_3)
        set_col_4 = set(col_4)
        set_col_5 = set(col_5)

        #check whether all people has been in the list
        unique_list = []
        for i in range(10):
            for j in range(5):
                if matrix[i][j] not in unique_list:
                    unique_list.append(matrix[i][j])

        #calculate repeated times for every member
        matrix_list_all_num = []
        for h in range(10):
            for k in range(5):
                matrix_list_all_num.append(matrix[h][k])

        dic = {}
        for item in unique_list:
            dic.update({item: matrix_list_all_num.count(item)})

        if len(unique_list) == len(name_list) and len(set_col_1) == len(col_1) and len(set_col_2) == len(col_2) and len(set_col_3) == len(col_3) and len(set_col_4) == len(col_4) and len(set_col_5) == len(col_5):
            #print("Totally calculate", i, "times\n")
            print("All people are scheduled\n")
            print(matrix)
            print("The repeat time for every member\n")
            print(dic)
            break
    return matrix

def data_write(file_path, datas):
	book = xlwt.Workbook()
	sheet = book.add_sheet('sheet1', cell_overwrite_ok=True)

	sheet.write(0, 0, '星期一')
	sheet.write(0, 1, '星期二')
	sheet.write(0, 2, '星期三')
	sheet.write(0, 3, '星期四')
	sheet.write(0, 4, '星期五')
	#sheet.write(0, 1, '星期六')


	i = 1
	for data in datas:
		for j in range(len(data)):
			sheet.write(i, j, data[j])
		i = i + 1

	book.save(file_path)

matrix_copy = get_matrix()
book_name_xls = 'schedule_shift.xls'

data_write(book_name_xls, matrix_copy)
