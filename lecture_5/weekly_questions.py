def file_parser(filename):
    result = []
    with open(filename, 'r') as fileR:
        for line in fileR:
            nums = [int(num) for num in line.strip()[1:-1].split(',')]

            for num in nums:
                divide3 = num // 3
                remainder = num % 3
                result.append((num,divide3, remainder))

    with open('results.txt', 'w') as fileW:
        for r in result:
            fileW.write(f'{r[0]},{r[1]},{r[2]}\n')


def file_sensorer(filename):
    sensitive_names = ['JUHANI', 'TIMO', 'AAPO', 'SIMEONI', 'LAURI', 'EERO', 'TUOMAS']
    with open(filename, 'r') as f:
        data = f.read()

    for name in sensitive_names:
        data = data.replace(name, '*******')

        capitalized_name = name.capitalize()
        if capitalized_name != name:
            data = data.replace(capitalized_name,'*******')

    with open('data_sensored.txt', 'w') as f:
        f.write(data)