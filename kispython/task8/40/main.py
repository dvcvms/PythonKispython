def main(x):
    # print(x)

    result = {}

    x = x.replace('<data>', '')
    x = x.replace('variable', '')
    x = x.replace('|', '')
    x = x.replace('#', '')
    x = x.replace('.', '')
    x = x.replace('</data>', '')
    x = x.replace(' ', '')

    # print(x)
    x_list = x.split(',')
    # print(x_list)

    for item in x_list:
        if item:
            # print('item=' + item)
            key, value = item.split('<==')

            # print('key=' + key)
            # print('value=' + value)

            result[key] = int(value)

    return result


n = '<data>|variable laa <== #-188. |, | variable rege <== #1210. |, \n|variable maeror<==#6716. |, | variable reedbi_391<== #9426. |, </data>'
print(main(n))

# 500