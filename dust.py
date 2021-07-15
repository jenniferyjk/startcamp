
dust =int(input('Enter the concentration:'))

if dust <= 30 :
    print('좋음')
elif 30<dust<=80 :
    print('보통')
elif 80<dust<=150 :
    print('나쁨')
else :
    print('매우나쁨')

# if는 필수, else는 선택(elif도 혼자서는 쓸 수 없음) -> if는 혼자쓰기 가능!

