filenames = ['doc.txt', 'report.txt', 'presentation.txt']

for a in filenames:
    with open(a,'r') as file:
        b = file.read()
    print(b)
