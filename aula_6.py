# Meta caracteres:
# ^ -> começa com
# $ -> termina com
# [^a-z] -> Negação

import re
from pprint import pprint


cpf = '147.852.964-12'
print(re.findall(r'^((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})$', cpf))
print(re.findall(r'[^0-9]+', cpf))





