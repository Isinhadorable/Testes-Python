d_data1 = int(input('O dia da data 1 é: '))
m_data1 = int(input('O mês data 1 é: '))
a_data1 = int(input('O ano da data 1 é: '))
d_data2 = int(input('O dia da data 2 é: '))
m_data2 = int(input('O mês da data 2 é: ')) 
a_data2 = int(input('O ano da data 2 é: '))
if a_data1 < a_data2:
    print('A primeira data é: ', d_data1, '/', m_data1, '/', a_data1)
elif a_data2 < a_data1:
    print('A primeira data é: ', d_data2, '/', m_data2, '/', a_data2)
else:
    if m_data1 < m_data2:
        print('A primeira data é: ', d_data1, '/', m_data1, '/', a_data1)
    elif m_data1 > m_data2:
        print('A primeira data é: ', d_data2, '/', m_data2, '/', a_data2)
    else:
        if d_data1 > d_data2:
            print('A primeira data é: ', d_data2, '/', m_data2, '/', a_data2)
        elif d_data1 < d_data2:
            print('A primeira data é: ', d_data1, '/', m_data1, '/', a_data1)
        else:
            print('As datas são iguais')
        
 
