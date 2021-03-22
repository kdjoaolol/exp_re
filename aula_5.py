# Meta caracteres: ^ $
# ()     \1
# () ()  \1 \2
# (())()   \1 \2 \3
# ?: NAO SALVA O GRUPO
# ?P<nome_do_grupo> \/?P=nome_do_grupo <- nomeando grupo e acessando o mesmo
import re
from pprint import pprint

texto = '''
<p>Frase 1</p> <p>Frase 2</p> <p>FRASE GRANDE EUTRA</p> <div>1</div> 

'''

# cpf = '147.852.964-12'
# print(re.findall(r'((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})', cpf))

#tags = re.findall(r'<([pdiv]{1,3})>(?:.+?)<\/\1>', texto)

# tags = re.findall(r'<(?P<tag>[pdiv]{1,3})>(.+?)<\/(?P=tag)>', texto)
# pprint(tags)

# for tag in tags:
#       x, y , z = tag
#       print(z)

print(re.sub(r'(<(.+?)>)(.+?)(<\/\2>)', r'\1"\3"\4', texto))




