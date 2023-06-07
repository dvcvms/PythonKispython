def parse_string1(input_string):
    print('res0  =  ' + input_string)

    result_dict = {}

    input_string = input_string\
        .replace('<block>','')\
        .replace('val', '')\
        .replace('</block>', '')\
        .replace('@', '')\
        .replace(':', '')\
        .replace('list(', '')\
        .replace(')', '')\
        .replace('#', '')\
        .replace(']]', '')\
        .replace('[[', '')

    print('res1  =  /' + input_string)

    input_list = input_string.split(';')

    print('res2  =  /' + input_string)

    input_list.remove(' ')

    print('res3  =  /' + input_string)

    print(input_list)
    for item in input_list:
        print('item=' + item)
        if item:
            entry = item.split('=')
            print(entry)
            key, values = entry[0], entry[1]
            print('key=' + key)
            print('values=' + values)
            result_dict[key.strip()] = [int(x) for x in values.split()]
            for x in values.split():
                print('x=' + x)
    return result_dict

# Пример использования
input_string = "[[<block>val @'reedti' := list( #1694 #-5580 #4239 );</block><block>val @'dimare' := list( #-3175#2160 #-4872 #6475); </block><block>val @'ener':= list( #3871 #-6114 #2694 #9778 ); </block><block>val @'rate_860' := list( #-1761 #-1380 #-4709); </block>]]"
# input_string = "[[<block>val @'reedti' := list( #1694 #-5580 #4239 );</block><block>val @'dimare' := list( #-3175#2160 #-4872 #6475); </block><block>val @'ener':= list( #3871 #-6114 #2694 #9778 ); </block><block>val @'rate_860' := list( #-1761 #-1380 #-4709); </block>]]"

result_dict = parse_string1(input_string)
print(result_dict) # {'reedti': [1694, -5580, 4239], 'dimare': [-3175, 2160, -4872, 6475], 'ener': [3871, -6114, 2694, 9778], 'rate_860': [-1761, -1380, -4709]}