## 덧셈, 뺄셈num1 = 1num2 = 2print('num1 + num2 = %d' % (num1 + num2))print('---------------------------')fnum1 = 3.14fnum2 = 0.12result = fnum1 + fnum2print('num1 + num2 = %.2f' % (fnum1 + fnum2))print(f'result: {result}')print('result: {}'.format(result))print('result: %.3f' % result)print('---------------------------')num1 = 9result = num1 + fnum2print(f'result: {result}')print('---------------------------')str1 = 'Good'str2 = ' 'str3 = 'Morning'result = str1 + str2 + str3print(f'result: {result}')print('---------------------------')korScore = int(input('국어 점수 : '))engScore = int(input('영어 점수 : '))mathScore = int(input('수학 점수 : '))totalScore = korScore + engScore + mathScoreprint('국어 점수 : {}'.format(korScore))print('영어 점수 : {}'.format(engScore))print('수학 점수 : {}'.format(mathScore))print('합계 : {}'.format(totalScore))print('---------------------------')partTimeMoney = int(input('알바비 : '))cardMoney = int(input('카드값 : '))result = partTimeMoney - cardMoneyprint('partTimeMoney: {}원'.format(partTimeMoney))print('cardMoney: {}원'.format(cardMoney))print('남는돈: {}'.format(result))print('---------------------------')## 곱셈, 나눗셈num1 = 20fNum1 = 3.14result = num1 * fNum1print('result : {}'.format(result))print('result : %.2f' % result)print('---------------------------')str1 = 'Hi 'result = str1 * 7print('result: {}'.format(result))print('---------------------------')num1 = 10num2 = 3result = num1 / num2print('num1 : {}, num2 : {}'.format(num1, num2))print('result: {}'.format(result))print('result : %.2f' % result)print('---------------------------')num1 = 0num2 = 3result = num1 / num2print('result : {}'.format(result))print('type of result : {}'.format(type(result)))result = int(num1 / num2)print('result : {}'.format(result))print('type of result : {}'.format(type(result)))print('---------------------------')kor = int(input('국어 점수 : '))eng = int(input('영어 점수 : '))mat = int(input('수학 점수 : '))total = kor + eng + matavg = total / 3print('국어 점수 : {}'.format(kor))print('영어 점수 : {}'.format(eng))print('수학 점수 : {}'.format(mat))print('합계 : {}'.format(total))print('평균 : {}'.format(avg))print('평균 : %.2f' % (total / 3))