passScore = 80myScore = int(input('점수 입력 : '))if myScore >= passScore:    print('PASS!')else :    print('FAIL!')print('---------------------------')seniorAge = 65passengerAge = int(input('나이 입력 : '))if passengerAge >= seniorAge :    print('무료 대상 승객입니다.')else :    print('유효 대상 승객입니다.')print('---------------------------')floatNum = float(input('소수 입력 : '))if floatNum - int(floatNum) >= 0.5 :    print('올림 : {}'.format(int(floatNum) + 1))else :    print('버림 : {}'.format(int(floatNum)))print('---------------------------')## 연습문제 1번rainPercentage = int(input('비올 확률 : '))minRainPercentage = 55## 1. 조건식(삼항연산자)print('우산 챙기세요.') if rainPercentage >= minRainPercentage else print('양산 챙기세요.')print('---------------------------')## 2. if-elseif rainPercentage >= minRainPercentage :    print('우산 챙기세요.')else :    print('양산 챙기세요.')print('---------------------------')## 연습문제 2번minTemperature = int(input('최저 기온 : '))maxTemperature = int(input('최고 기온 : '))if maxTemperature - minTemperature >= 11 :    print('일교차 : {}'.format(maxTemperature - minTemperature))    print('감기 조심하세요.')else :    print('일교차 : {}'.format(maxTemperature - minTemperature))    print('산책하기 좋은 날씨 입니다.')