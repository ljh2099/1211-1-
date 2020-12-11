information_list = input().split(',')

case_number = int(information_list[0])
budget = int(information_list[1])
risk_coefficient = int(information_list[2])

#第一行資料

price_list0 = input().split(',')
expected_revenue_list0 = input().split(',')

price_list = []
expected_revenue_list = []
for k in range(case_number):
    price_list.append(int(price_list0[k]))
    expected_revenue_list.append(int(expected_revenue_list0[k]))

#第二三行的資訊轉成整數清單

variance_covariance_matrix = []
for i in range(case_number):
    list_str = input().split(',')
    
    list_int = []
    for t in range(case_number):
        list_int.append(int(list_str[t]))
    
    variance_covariance_matrix.append(list_int)

#把變異數和共變數做成矩陣(variance_covariance_matrix)
bid_or_not = [0,1,0,1]
sum_expected_rev = 0

for j in range(case_number):    #目標式前半部取相加
    sum_expected_rev += expected_revenue_list[j]*bid_or_not[j]
            
for r in range(case_number):   #目標式後半相加
    for s in range(case_number):
        sum_expected_rev -= risk_coefficient*variance_covariance_matrix[r][s]*bid_or_not[r]*bid_or_not[s]
            
print(sum_expected_rev)