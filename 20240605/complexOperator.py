num1 = 10num2 = 3print(num1)print(num2)print('---------------------------')num1 += num2print('덧셈 연산 후 할당 : {}'.format(num1))print('---------------------------')num1 = 10num1 -= num2print('뺄셈 연산 후 할당 : {}'.format(num1))print('---------------------------')num1 = 10num1 *= num2print('곱셈 연산 후 할당 : {}'.format(num1))print('---------------------------')num1 = 10num1 /= num2print('나눗셈 연산 후 할당 : {}'.format(num1))print('---------------------------')num1 = 10num1 %= num2print('나머지 연산 후 할당 : {}'.format(num1))print('---------------------------')num1 = 10num1 //= num2print('몫 연산 후 할당 : {}'.format(num1))print('---------------------------')num1 = 10num1 **= num2print('거듭제곱 연산 후 할당 : {}'.format(num1))print('---------------------------')accumValue = 0accumValue = 30print('1월 누적 강수량 : %dmm' % accumValue)accumValue += 45print('2월 누적 강수량 : %dmm' % accumValue)accumValue += 47print('3월 누적 강수량 : %dmm' % accumValue)accumValue += 55print('4월 누적 강수량 : %dmm' % accumValue)accumValue += 65print('5월 누적 강수량 : %dmm' % accumValue)accumValue += 100print('6월 누적 강수량 : %dmm' % accumValue)accumValue += 128print('7월 누적 강수량 : %dmm' % accumValue)accumValue += 209print('8월 누적 강수량 : %dmm' % accumValue)accumValue += 204print('9월 누적 강수량 : %dmm' % accumValue)accumValue += 186print('10월 누적 강수량 : {}mm'.format(format(accumValue, ',')))accumValue += 67print('11월 누적 강수량 : {}mm'.format(format(accumValue, ',')))accumValue += 25print('12월 누적 강수량 : {}mm'.format(format(accumValue, ',')))print('---------------------------')print('연간 누적 강수량 : {}mm'.format(format(accumValue, ',')))print('---------------------------')print('연간 누적 강수량 : %.2fmm' % (accumValue / 12))