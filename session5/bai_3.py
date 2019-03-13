def remove_dollar_sign(n):
    s_without_dollar = n.replace("$","")
    return s_without_dollar
a = input('nhập 1 chuỗi có ký tự $: ')
print('Chuỗi sau khi xóa $:',remove_dollar_sign(a))
# ------------------------------------------------------------------------------------
# string_with_no_dollars = remove_dollar_sign("$80% percent of $life is to show $up")
# if string_with_no_dollars == "80% percent of life is to show up":
#     print("Your function is correct")
# else:
#     print("Oops, there's a bug")