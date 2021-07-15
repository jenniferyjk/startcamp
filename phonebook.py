#각 전화마다 식당을 매칭시키기

menu = ['한식','일식','중식','양식']
import random
lunch = random.choice(menu)
number = {'한식':'123-4568','일식':'444-2345','중식':'534-5675','양식':'567-1234'}

print('오늘의 점심은 {}입니다. 전화번호는 {}입니다.'.format(lunch,number[lunch]))
