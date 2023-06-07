def parse_string1(input_string):
    # print(input_string)
    result_dict = {}

    input_string = input_string \
        .replace('begin', '') \
        .replace('.do', '') \
        .replace('decl', '') \
        .replace('end;', '') \
        .replace('<', '') \
        .replace('.', '') \
        .replace('#', '') \
        .replace(']]', '') \
        .replace('[[', '') \
        .replace(']', '') \
        .replace('[', '') \
        .replace('end', '')

    # print(input_string)

    input_string = input_string \
        .replace(" ", "")
    # input_string = input_string.strip()

    # print(input_string)

    input_list = input_string.split(';')
    # print(11111)
    # print(input_list)

    for item in input_list:
        # print('item=' + item)
        if item:
            entry = item.split('|')
            # print(entry)
            key, values = entry[0], entry[1]
            # print('key=' + key)
            # print('values=' + values)
            # for x in values.split(','):
                # print('x=' + x)
            result_dict[key.strip()] = [int(x) for x in values.split(',')]
            # print('===========')
            # print(result_dict)
    return result_dict
# Пример использования
# input_string = "begin .do decl 'enteve_531'<|[ 3461 , -7505];.end; .do decl 'ansoan'<| [ -8819 , -2828 ];.end; .do decl 'zaen'<| [9944 ,-8482 , 4545 ];.end; .do decl'erus_2' <| [ 9932 , -5489 ];.end; end"
input_string = "begin .do decl 'anat'<|[-7347 , -3504, -4564 ];.end; .do decl'eranre'<| [-5176 , 2854 ]; .end;end"
result_dict = parse_string1(input_string)
print(result_dict)
