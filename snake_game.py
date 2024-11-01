import math

print('123456')
original = '      \n.....:O\n    . '
print(original)

print('please move up, down, left or right:')

tail = 1
head = 7

x = input()

if (x == 'l'):
    head = max(0, head - 1)
elif (x == 'r'):
    head = min(18, head + 1)
elif (x == 'u'):
    head = max(0, head - 6)
else:
    head = min(18, head + 6)

col = math.floor(head / 6) + 1
row = math.floor(head % 6) + 1

print('col:', col, 'row', row)

def addDots(head, body):
    new_body = body.replace('\n', '')
    # print('head argument in addDots:', head)
    out = ''
    for j in range(len(new_body)):
        next_index = min(18, j + 1)
        prev_index = max(0, j - 1)
        if (j == max(0, head - 5)):
            for k in range(6):
                if (k != 6):
                    out += '.'
                else:
                    out += ':O'
                if (j + k % 6 == 0 and j + k != 0):
                    out += '\n'
                
        elif (new_body[j] == ' '):
            out += ' '
        elif (body[j] == '.'):
            out += '.'
        if (j % 6 == 0 and j != 0 and j != 18 and j != max(0, head - 5)):
            out += '\n'
    return out

print('addDots:')
print('123456')
print(addDots(head, original))

body = ''

length = len(original)
for i in range(length):
    current_pixel = i + 1
    if (current_pixel == head - 5):
        # add the trailing dots
        body += '.....:O'
    
    elif(original[i] == '.'):
        body += '.'
    else:
        body += ' '

    if (current_pixel % 6 == 0 and current_pixel != 0):
        body += '\n'

print('123456')
print(body)