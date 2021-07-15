import random

numbers = range(1,46)
#random.sample(seq,k) : seq 내의 고유데이터를 중복 없이 k개 무작위 표본추출한다

lotto = random.sample(numbers,7)

print('로또 번호는', lotto)
