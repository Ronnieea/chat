def read_file(filename):
    lines = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            lines.append(line.strip())
    return lines


def convert(lines):
    prson = None
    貪睡_word_count = 0
    貪睡_sticker_count = 0
    貪睡_image_count = 0
    老爸_word_count = 0
    老爸_sticker_count = 0
    老爸_image_count = 0
    for line in lines:
        s = line.split(' ')
        time = s[0]
        name = s[1]
        if name == '貪睡':
            if s[2] == '貼圖':
                貪睡_sticker_count += 1
            elif s[2] == '圖片':
                貪睡_image_count +=1
            else:    
                for m in s[2:]:
                    貪睡_word_count += len(m)
        elif name == '老爸':
            if s[2] == '貼圖':
                老爸_sticker_count += 1
            elif s[2] == '圖片':
                老爸_image_count += 1
            else:
                for m in s[2:]:
                    老爸_word_count += len(m)
    print('貪睡說了', 貪睡_word_count)
    print('貪睡傳了', 貪睡_sticker_count, '個貼圖')
    print('貪睡傳了', 貪睡_image_count, '張圖片')
    
    print('老爸說了', 老爸_word_count)
    print('老爸傳了', 老爸_sticker_count, '個貼圖')
    print('老爸傳了', 老爸_image_count, '張圖片')

    
def write_file(filename, lines):
    with open(filename, 'w') as f:
        for line in lines:
            f.write(line + '\n')    


def main():
    lines = read_file('input1.txt')
    lines = convert(lines)
    #write_file('output.txt', lines)


main()
