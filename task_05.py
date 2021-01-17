# 1. Дан список строк. Отформатировать все строки в формате ‘{i} - {string}’,
#  где i это порядковый номер строки в списке. Использовать генератор списков.

list = ['some string', 'another string', 'last string in the list']

list = [f'{idx} - {items}' for idx, items in enumerate(list)]

print(list)

# new_list = []
# for idx, items in enumerate(list):
#     print(idx, items)
#     new_list.append(f'{idx} - {items}')
# print(new_list)
