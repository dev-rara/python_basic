## andprint('{} and {} : {}'.format(True, True, (True and True)))print('{} and {} : {}'.format(False, True, (False and True)))print('{} and {} : {}'.format(True, False, (True and False)))print('{} and {} : {}'.format(False, False, (False and False)))print('---------------------------')## orprint('{} or {} : {}'.format(True, True, (True or True)))print('{} or {} : {}'.format(False, True, (False or True)))print('{} or {} : {}'.format(True, False, (True or False)))print('{} or {} : {}'.format(False, False, (False or False)))print('---------------------------')## notprint('not {} : {}'.format(True, (not True)))print('not {} : {}'.format(False, (not False)))print('---------------------------')age = int(input('나이 입력: '))vaccine = (age < 20) or (age >= 65)print('age : {}, vaccine : {}'.format(age, vaccine))print('---------------------------')kor = int(input('국어 점수 : '))eng = int(input('영어 점수 : '))mat = int(input('수학 점수 : '))avg = (kor + eng + mat) / 3avgCheck = avg >= 70korCheck = kor >= 60engCheck = eng >= 60matCheck = mat >= 60print('평균 : {}, 결과 : {}'.format(avg, avgCheck))print('국어 : {}, 결과 : {}'.format(kor, korCheck))print('영어 : {}, 결과 : {}'.format(eng, engCheck))print('수학 : {}, 결과 : {}'.format(mat, matCheck))print('과락 결과 : {}'.format((korCheck and engCheck and matCheck)))print('최종 결과 : {}'.format((korCheck and engCheck and matCheck and avgCheck)))print('---------------------------')