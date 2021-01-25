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
        temp *= 0.75
        return temp
    else:
        temp = 4.5 - x
        temp = np.log(temp)
        temp *= -0.75
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

    speed_names = ['b_c', 'b_g', 'w_c', 'w_g', 'p_c', 'p_g']
    score_names = ['b_c_score', 'b_g_score', 'w_c_score', 'w_g_score', 'p_c_score', 'p_g_score']
    new_speeds = []

    for i in speed_names:
        vars()[str(i)] = []

    for i in score_names:
        vars()[str(i)] = []

    for line in speed_lines:
        if ('bottle' in line):
            if ('catching' in line):
                vars()['b_c'].append(int(line.split(', ')[1]))
            elif ('giving' in line):
                vars()['b_g'].append(int(line.split(', ')[1]))
        elif ('water' in line):
            if ('catching' in line):
                vars()['w_c'].append(int(line.split(', ')[1]))
            elif ('giving' in line):
                vars()['w_g'].append(int(line.split(', ')[1]))
        elif ('plate' in line):
            if ('catching' in line):
                vars()['p_c'].append(int(line.split(', ')[1]))
            elif ('giving' in line):
                vars()['p_g'].append(int(line.split(', ')[1]))

    for line in score_lines:
        if ('catching, bottle' in line):
            vars()['b_c_score'].append(float(line.split(', ')[-1].split(']')[0]))
        elif ('giving, bottle' in line):
            vars()['b_g_score'].append(float(line.split(', ')[-1].split(']')[0]))
        elif ('catching, water' in line):
            vars()['w_c_score'].append(float(line.split(', ')[-1].split(']')[0]))
        elif ('giving, water' in line):
            vars()['w_g_score'].append(float(line.split(', ')[-1].split(']')[0]))
        elif ('catching, plate' in line):
            vars()['p_c_score'].append(float(line.split(', ')[-1].split(']')[0]))
        elif ('giving, plate' in line):
            vars()['p_g_score'].append(float(line.split(', ')[-1].split(']')[0]))

    for i in speed_names:
        if (len(vars()[str(i)]) != 0):
            vars()['last_' + str(i)] = vars()[str(i)][-1]
        else:
            vars()['last_' + str(i)] = 300

    for i in score_names:
        if (len(vars()[str(i)]) != 0):
            vars()[str(i)] = vars()[str(i)][-1]
        else:
            vars()[str(i)] = 3.5
        print(str(i) + ' is', vars()[str(i)])

    for i in speed_names:
        temp_speed = vars()['last_' + str(i)] + round(150 * opt_log(vars()[str(i) + '_score']))
        vars()['new_' + str(i)] = int(np.median([150, 1500, temp_speed]))
        print('last_' + str(i) + ' is', vars()['last_' + str(i)], ', new_' + str(i) + ' is', vars()['new_' + str(i)])

    for i in speed_names:
        new_speeds.append(vars()['new_' + str(i)])

    return new_speeds

if __name__ == '__main__':
    speed_optimizer()