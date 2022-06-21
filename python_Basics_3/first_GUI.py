#GUI

freyJST_GUI = [
        [0,0,0,1,0,0,0],
        [0,0,1,1,1,0,0],
        [0,1,1,1,1,1,0],
        [1,1,1,1,1,1,1],
        [0,0,0,1,0,0,0],
        [0,0,0,1,0,0,0]
        ]


for photo in freyJST_GUI:
    for pic in photo:
        if (pic == 1):
            print('*', end='')
        else:
            print(' ', end ='')
    print('')
