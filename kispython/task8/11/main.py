def main(x):
    result = []
    input_string = x

    # print(input_string)
    input_string = input_string\
        .replace('do store', '')\
        .replace('[', '') \
        .replace(']', '') \
        .replace('q(', '') \
        .replace(')', '') \
        .replace('done', '') \

    # print(input_string)

    input_list = input_string.split(';')

    # print(input_list)

    for item in input_list:
        item = item.replace(' ', '')
        if item:
            # print('item='+ item)
            value, key = item.split('to')
            # print(value)
            # print(key)

            atuple = (key, int(value))
            result.append(atuple)

    print(result)

n = '[ do store 9195 to q(rebien) done; do store -6393 to q(geries_168)done;do store -3463 to q(onbege_650) done; do store 5587 to q(onarar)done; ]'
main(n)