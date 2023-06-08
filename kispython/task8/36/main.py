def main(x):
    result = {}

    x = x.replace('{', '')
    x = x.replace('<%', '')
    x = x.replace('}', '')
    x = x.replace('\n', '')
    x = x.replace('(', '')
    x = x.replace(')', '')
    x = x.replace(' ', '')
    x = x.replace('##', '')


    x_list = x.split('%>.')
    for item in x_list:
        if item:
            value, key = item.split('|>')
            value = value.split('#')

            newValue = []
            for y in value:
                g = int(y)
                newValue.append(g)

            result[key] = newValue


    return result


n = '{ <% #( #-1093#-4285 ) |> tianis_859 %>.<%#(#9100 #9254 #-5074 #-3805\n) |> riladi_995 %>. <% #( #3984 #-2833 ) |>bier %>. <%#(#5906#2768 )\n|> isar %>. }'
print(main(n))
