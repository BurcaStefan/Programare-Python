def CamilCaseToSnakeCase (str):
    snakecase=''
    for ch in str:
        if ch.isupper() and snakecase:
            snakecase+="_"
        snakecase+=ch.lower()
            
    return snakecase

camelcase=input()
print(CamilCaseToSnakeCase(camelcase))