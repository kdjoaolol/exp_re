import re
from pprint import pprint

# os grupos sao o que queremos capturar no findall

texto = '''
ONLINE  192.168.0.1 GHIJK active
OFFLINE  192.168.0.2 GHIJK inactive
OFFLINE  192.168.0.3 GHIJK active
ONLINE  192.168.0.4 GHIJK active
ONLINE  192.168.0.5 GHIJK inactive
OFFLINE  192.168.0.6 GHIJK active
'''
# Positive lookahead so vai pegar o que for active como a linha diz abaixo
# pprint(re.findall(r'\w+\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+(?=active)', texto))

# Ngative lookahead so vai pegar o que for active como a linha diz abaixo
# pprint(re.findall(r'\w+\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+(?!active)', texto))

# Positive lookahead
# pprint(re.findall(r'(?=.*[^in]active).+', texto))

# Positive lookbehind seta "<" apontando pra tras
# pprint(re.findall(r'\w+(?<=ONLINE)\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+\w+', texto))
# Negative lookbehind
# pprint(re.findall(r'\w+(?<!ONLINE)\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+\w+', texto))

# Positive lookbehind seta "<" apontando pra tras
# pprint(re.findall(r'\w+(?<=OFFLINE)\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+\w+', texto))
# Negative lookbehind
pprint(re.findall(r'\w+(?<=OFFLINE)\s+\d+\.\d+\.\d+\.\d+\s+\w+\s+\w+', texto))
