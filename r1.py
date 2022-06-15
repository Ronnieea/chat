def read_file(filename):
    lines = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            lines.append(line.strip())
    return lines

def convert(lines):
    new = []
    prson = None
    for line in lines:
        if line == '貪睡豬':
        	person = '貪睡豬'
        	continue
        elif line == '洪若寧':
        	person = '洪若寧'
        	continue
        if person:
            new.append(person + ': ' + line)
    return new

def write_file(filename, lines):
    with open(filename, 'w') as f:
        for line in lines:
            f.write(line + '\n')    

def main():
    lines = read_file('input.txt')
    lines = convert(lines)
    write_file('output.txt', lines)
main()
