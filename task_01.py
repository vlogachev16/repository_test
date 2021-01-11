a = ['ten', 'nine', 'eight', 'seven', 'six', 'five', 'for', 'three', 'two','one', 'NO']
#b = ' green bottles hanging on the wall,'
#c = 'And if one green bottle should accidentally fall, There‛ll be...'
d = ''

for i in a:
    if i != a[-1]:
        song = str(i) + 'green bottles hanging on the wall,\n' + str(i) + 'green bottles hanging on the wall,\n' + 'And if one green bottle should accidentally fall, There‛ll be...\n' + d
        print(song)

    else:
        print('NO green bottles hanging on the wall!')


# Не получилось сделать перенос в Атоме, если делаю с помощью \n терминал выдает
# ошибку
