def parse_string1(input_string):
    # print(input_string)
    result_dict = []

    input_string = input_string \
        .replace('<block> data', '') \
        .replace('</block>', '') \
        .replace('q(', '') \
        .replace(')', '') \
        .replace('.', '') \
        .replace('|', '') \
        .replace('}', '') \
        .replace('{', '') \
        .replace('<block>data', '') \

    # print(input_string)

    # input_string = input_string.strip()
    #
    # print(input_string)
    #
    input_list = input_string.split(';')
    # print(11111)
    # print(input_list)

    for item in input_list:
        # print('item=' + item)
        if item:
            # print(22222)
            # print(item.split('>'))
            kv = item.split('>')
            # print(33333)
            # print(kv)
            key, value = kv[0], kv[1]
            key = key.strip()
            # print('key:')
            # print(key)
            value = value.replace(" ", "")
            key = key.split(" ")
            newKey = []
            for y in key:
                # print(y)
                g = int(y)
                newKey.append(g)
            # print('newKey:')
            # print(newKey)
    #
    #         # key = map(int, key)
    #         # print("key:")
    #         # print(key)
    #         # print('value=' + value)
    #         # print(key)
    #         # print(newKey)
    #         # print(value)
            atuple = (value, newKey)
            # print('atuple:')
            # print(atuple)
            result_dict.append(atuple)
    print(result_dict)

# input_string = '<block> data{ -2042 -5445 9524} |>q(inesce). </block>;<block> data {8050 2809 -4550 -456}|> q(edbera). </block>;'
input_string = '<block> data{ -7846 2533 -3255 -1745 } |>q(tea). </block>;<block>data { 6506 9986 -657 } |> q(lelera). </block>; <block>data{ 5476 -7957 6270} |> q(atcece). </block>;'

parse_string1(input_string)
