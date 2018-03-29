import numpy as np

def simple_interest(inter_rate, n_of_payment, start_value):#单利终值计算
    print(' ')
    '''
    P = The starting value
    i = Interest rate
    n = Number of payments
    '''
    if start_value >= 0:
        P = start_value
    else: return 'Error in start_value, I want a digit number bigger than 0.'
    if n_of_payment >= 0:
        n = n_of_payment
    else: return 'Error in number_of_years, I want a digit number bigger than 0.'
    if inter_rate <= 0:
        return 'Error in interest_rate, I want a number bigger than 0 as percent value.'
    else:
        i = inter_rate
    return ('%.8f' %(P * (1 + i * n)))


def compound_interest(start_value, inter_rate, n_of_payments):#复利计算
    '''
    P = The starting value
    i = Interest rate
    n = Number of payments
    '''
    if start_value >= 0:
        P = start_value
    else: return print('Error in start_value, I want a digit number bigger than 0.')
    if n_of_payments >= 0:
        n = n_of_payments
    else: return print('Error in number_of_years, I want a digit number bigger than 0.')
    if inter_rate >= 1:
        i = inter_rate / 100.00
    elif inter_rate <=0:
        return print('Error in interest_rate, I want a number bigger than 0 as percent value.')
    else :
        i = inter_rate
    return P *(1 + i) ** n

def profit_index(inter_rate, cashflow):#项目盈利指标计算
    net_present_value = np.npv(inter_rate, cashflow)
    inner_rate_of_return = np.irr(cashflow)
    profitability_index = (net_present_value + abs(cashflow[0]))/abs(cashflow[0])
    result = [net_present_value, inner_rate_of_return, profitability_index]
    return result


def profit_index_input(t):
    t.set('请输入(利率, 期初投资, 第1期现金流, ..., 第n期现金流)：')
    return

def profit_index_parse(t):
    parameter = t.split(',')
    interest_rate = parameter[0]
    cashflow = parameter[1:]
    return profit_index(interest_rate, cashflow)



