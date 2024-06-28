%{
#include "y.tab.h"
%}

%option noyywrap

%{
#define INDENT  1
#define DEDENT  2
int indent_level = 0;
%}

%%

"def"           { return DEF; }
"if"            { return IF; }
"else"          { return ELSE; }
"for"           { return FOR; }
"while"         { return WHILE; }
"return"        { return RETURN; }
"print"         { return PRINT; }
"int"           { return INT; }   /* Java keyword */
"float"         { return FLOAT; } /* Java keyword */
"String"        { return STRING; }/* Java keyword */
"void"          { return VOID; }  /* Java keyword */
"true"|"false"  { return BOOLEAN; } /* Java keyword */

[0-9]+          { yylval = atoi(yytext); return NUMBER; }
[a-zA-Z_][a-zA-Z0-9_]*  { yylval = strdup(yytext); return ID; }

"("             { return '('; }
")"             { return ')'; }
":"             { return ':'; }
","             { return ','; }
"="             { return '='; }
"+"             { return '+'; }
"-"             { return '-'; }
"*"             { return '*'; }
"/"             { return '/'; }
"=="            { return EQ; }
"!="            { return NEQ; }
"<"             { return '<'; }
"<="            { return LE; }
">"             { return '>'; }
">="            { return GE; }
"{"             { indent_level++; return '{'; }
"}"             { indent_level--; return '}'; }
"\n"            {
                    if (indent_level > 0)
                        return '\n';
                    else if (indent_level < 0)
                        yyerror("Mismatched braces");
                }

[ \t]+          ; /* Ignore whitespace */

.               { yyerror("Invalid character"); }

%%

int yywrap() {
    return 1;
}
