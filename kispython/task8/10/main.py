def parse_string1(input_string):
    print(input_string)
    result_dict = []

    input_string = input_string \
        .replace('<data>option', '') \
        .replace('</data>', '') \
        .replace('|', '') \
        .replace('<data>', '') \
        .replace('option', '') \
        .replace('"', '') \
        # .replace('#', '') \
        # .replace(']]', '') \
        # .replace('[[', '') \
        # .replace(']', '') \
        # .replace('[', '') \
        # .replace('end', '')

    # print(input_string)

    input_string = input_string \
        .replace(" ", "")
    input_string = input_string.strip()

    # print(input_string)

    input_list = input_string.split(';')
    # print(11111)
    # print(input_list)

    for item in input_list:
        # print('item=' + item)
        if item:
            # print(111111111)
            # print(item.split('>'))
            kv = item.split('>')
            # print(222222222)
            # print(kv)
            key, value = kv[0], kv[1]
            # print('key=' + key)
            # print('value=' + value)
            atuple = (value, key)
            # print(atuple)
            result_dict.append(atuple)
    print(result_dict)

input_string = '|<data> option"regeso_34"|> endi_370</data>; <data> option"tela_146"|> teat_945 </data>; <data> option"riedma_837" |> orso_307 </data>;<data> option "riin"|>isra_865 </data>;|'
parse_string1(input_string)
