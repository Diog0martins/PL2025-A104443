import re
import ply.lex as lex

tokens = (
    'VARIABLES',
    'PREFIX',
    'TYPE',
    'TYPEABREV',
    'LANGUAGE',
    'NUMBER',
    'DOT',
    'COLON',
    'AT',
    'WHERE',
    'SELECT',
    'LIMIT',
    'LCBRCKTS',
    'RCBRCKTS',
    'STRING'
)

t_VARIABLES = r'\?\w+'
t_PREFIX = r'\b\w+(?=:)' 
t_TYPE = r'(?<=:)\w+'
t_TYPEABREV = r'a'
t_LANGUAGE = r'(?<=@)\w+'
t_NUMBER = r'\d+'
t_DOT = r'\.'
t_COLON = r':'
t_AT = r'@'
t_WHERE = r'where'
t_SELECT = r'select'
t_LIMIT = r'LIMIT'
t_LCBRCKTS = r'\{'
t_RCBRCKTS = r'\}' 

t_ignore = ' \t\n'

def t_STRING(t):
    r'"([^"]+)"' 
    t.value = t.value[1:-1]
    return t    

def t_COMMENT(t):
    r'\#.*'
    pass

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

def main():

    data = '''
# DBPedia: obras de Chuck Berry
select ?nome ?desc where {
?s a dbo:MusicalArtist.
?s foaf:name "Chuck Berry"@en .
?w dbo:artist ?s.
?w foaf:name ?nome.
?w dbo:abstract ?desc
} LIMIT 1000
        '''

    lexer.input(data)

    for tok in lexer:
        print(tok)


if __name__ == '__main__':
        main()