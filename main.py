import re

addressToVerify ='29172-245'
match = re.match(r'^([0-9]{8}|[0-9]{5}-[0-9]{3})$', addressToVerify)

# VALIDAR EMAIL
# ^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$

# VALIDAR NOME COMPLETO
# ^([a-zA-Z]+ )+[a-zA-Z]+$

# VALIDAR CEP (BRASIL)
# ^([0-9]{8}|[0-9]{5}-[0-9]{3})$



print (match)
