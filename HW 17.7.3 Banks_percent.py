per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
percent_list = list(map(float, (per_cent.values())))
money = float(input("money = "))
max_deposit = (max(percent_list)) * money / 100
print("Максимальная сумма, которую вы можете заработать — " + str(round(max_deposit)))