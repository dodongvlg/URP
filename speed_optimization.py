import numpy as np
import write_log

def opt_sigmoid(x):
    temp = x - 3.5
    temp = 1 / (1 + np.exp(-2 * temp)) - 0.5
    temp *= 2
    return temp

def opt_tanh(x):
    temp = x - 3.5
    return np.tanh(temp)

def opt_ReLU(x):
    if x <= 1.5:
        return -1
    elif x >= 5.5:
        return 1
    else:
        return 0.5 * x - 1.75

def opt_linear(x):
    return 0.4 * x - 1.4

def opt_log(x):
    if x >= 3.5:
        temp = x - 2.5
        temp = np.log(temp)
        temp /= np.log(3.5)
        return temp
    else:
        temp = 4.5 - x
        temp = np.log(temp)
        temp /= -np.log(3.5)
        return temp

def opt_points(x):
    sign_num = x % 10
    amp_num = x // 10

    sign = 0
    amp = 0

    if sign_num == 1:
        sign = -1
    elif sign_num == 2:
        sign = 0
    elif sign_num == 3:
        sign = 1
    
    if amp_num == 1:
        amp = 200
    if amp_num == 2:
        amp = 50

    return sign * amp

def speed_optimizer():
    f = open(write_log.file_name)
    speed_lines = f.readlines()
    f.close()

    f = open(write_log.file_name.split('.')[0] + '_score.txt')
    score_lines = f.readlines()
    f.close()

    speed_names = ['e_c', 'e_g', 'f_c', 'f_g', 'c_c', 'c_g', 'e_c_p', 'e_g_p', 'f_c_p', 'f_g_p', 'c_c_p', 'c_g_p']
    score_names = ['e_c_score', 'e_g_score', 'f_c_score', 'f_g_score', 'c_c_score', 'c_g_score',
                    'e_c_p_score', 'e_g_p_score', 'f_c_p_score', 'f_g_p_score', 'c_c_p_score', 'c_g_p_score']
    new_speeds = []

    for i in speed_names:
        vars()[str(i)] = []

    for i in score_names:
        vars()[str(i)] = []

    for line in speed_lines:
        if ('empty' in line):
            if ('catching' in line) and ('push' in line):
                vars()['e_c_p'].append(int(line.split(', ')[1]))
            elif ('giving' in line) and ('push' in line):
                vars()['e_g_p'].append(int(line.split(', ')[1]))
            elif ('catching' in line):
                vars()['e_c'].append(int(line.split(', ')[1]))
            elif ('giving' in line):
                vars()['e_g'].append(int(line.split(', ')[1]))
        elif ('full' in line):
            if ('catching' in line) and ('push' in line):
                vars()['f_c_p'].append(int(line.split(', ')[1]))
            elif ('giving' in line) and ('push' in line):
                vars()['f_g_p'].append(int(line.split(', ')[1]))
            elif ('catching' in line):
                vars()['f_c'].append(int(line.split(', ')[1]))
            elif ('giving' in line):
                vars()['f_g'].append(int(line.split(', ')[1]))
        elif ('cookie' in line):
            if ('catching' in line) and ('push' in line):
                vars()['c_c_p'].append(int(line.split(', ')[1]))
            elif ('giving' in line) and ('push' in line):
                vars()['c_g_p'].append(int(line.split(', ')[1]))
            elif ('catching' in line):
                vars()['c_c'].append(int(line.split(', ')[1]))
            elif ('giving' in line):
                vars()['c_g'].append(int(line.split(', ')[1]))

    for line in score_lines:
        if ('catching, empty, hand' in line):
            vars()['e_c_score'].append(float(line.split(', ')[-1].split(']')[0]))
        elif ('giving, empty, hand' in line):
            vars()['e_g_score'].append(float(line.split(', ')[-1].split(']')[0]))
        elif ('catching, full, hand' in line):
            vars()['f_c_score'].append(float(line.split(', ')[-1].split(']')[0]))
        elif ('giving, full, hand' in line):
            vars()['f_g_score'].append(float(line.split(', ')[-1].split(']')[0]))
        elif ('catching, cookie, hand' in line):
            vars()['c_c_score'].append(float(line.split(', ')[-1].split(']')[0]))
        elif ('giving, cookie, hand' in line):
            vars()['c_g_score'].append(float(line.split(', ')[-1].split(']')[0]))
        elif ('catching, empty, push' in line):
            vars()['e_c_p_score'].append(float(line.split(', ')[-1].split(']')[0]))
        elif ('giving, empty, push' in line):
            vars()['e_g_p_score'].append(float(line.split(', ')[-1].split(']')[0]))
        elif ('catching, full, push' in line):
            vars()['f_c_p_score'].append(float(line.split(', ')[-1].split(']')[0]))
        elif ('giving, full, push' in line):
            vars()['f_g_p_score'].append(float(line.split(', ')[-1].split(']')[0]))
        elif ('catching, cookie, push' in line):
            vars()['c_c_p_score'].append(float(line.split(', ')[-1].split(']')[0]))
        elif ('giving, cookie, push' in line):
            vars()['c_g_p_score'].append(float(line.split(', ')[-1].split(']')[0]))

    for i in speed_names:
        if (len(vars()[str(i)]) != 0):
            vars()['last_' + str(i)] = vars()[str(i)][-1]
        else:
            vars()['last_' + str(i)] = 500

    for i in score_names:
        if (len(vars()[str(i)]) != 0):
            vars()[str(i)] = vars()[str(i)][-1]
        else:
            vars()[str(i)] = 3.5
        print(str(i) + ' is', vars()[str(i)])

    for i in speed_names:
        temp_speed = vars()['last_' + str(i)] + round(100 * opt_log(vars()[str(i) + '_score']))
        vars()['new_' + str(i)] = int(np.median([300, 700, temp_speed]))
        print('last_' + str(i) + ' is', vars()['last_' + str(i)], ', new_' + str(i) + ' is', vars()['new_' + str(i)])

    for i in speed_names:
        new_speeds.append(vars()['new_' + str(i)])

    return new_speeds

if __name__ == '__main__':
    for i in range (2, 13):
        t = float(i) / 2
        print(t)
        print(opt_log(t))