import string

def ways_to_encode(s):
    if s == '':
        return 1

    return (ways_to_encode(s[1:]) +
            (ways_to_encode(s[2:]) if len(s) > 1 and int(s[:2]) < 26 else 0))


def ways_to_encode2(s):
    print("ways to encode '{}'".format(s))
    if s == '':
        print('count 1')
        return 1

    print("A split: '{}' '{}' ".format(s[:1], s[1:]))
    a = ways_to_encode2(s[1:])

    print("B split: '{}' '{}' ".format(s[:2], s[2:]))
    b = 0
    if len(s) > 1 and int(s[:2]) < 26:
        b = ways_to_encode2(s[2:])
    else:
        print('ignored')

    return a + b


def encodings(s):
    if s == '':
        return ['']
    
    def split(h,t):
        return [string.ascii_lowercase[int(h)]+i for i in encodings(t)]
    
    return split(s[:1], s[1:]) + (split(s[:2], s[2:]) if len(s) > 1 and int(s[:2]) < 26 else [])
    
    # h, t = s[:1], s[1:]  
    # a = [string.ascii_lowercase[int(h)]+i for i in encodings(t)]

    # b = []
    # if len(s) > 1 and int(s[:2]) < 26:
    #     h, t = s[:2], s[2:]  
    #     b = [string.ascii_lowercase[int(h)]+i for i in encodings(t)]

    # return a + b

input_string = '1121'

print(ways_to_encode2(input_string))
print(encodings(input_string))


