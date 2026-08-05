# Tutorial de MATLAB

## Motivação
Este tutorial tem como objetivo explicar o que é MATLAB e suas aplicações, além de apresentar a sintaxe básica da linguagem juntamente com Simulink.

## O que é MATLAB e para que serve?
**MATLAB** (Matrix Laboratory) é uma plataforma de programação e computação numérica para aplicações de engenharia e científicas, tais como Aplicações de Álgebra Linear, Análise de Dados, Processamento de Sinais e Imagens e Sistemas Embarcados.
O MATLAB possui linguagem de programação própria de alto nível conhecida também como MATLAB. A linguagem é construída principalmente em cima de C, C++ e Java. Além disso, o MATLAB é a base do **Simulink**, um ambiente de diagramas de blocos para simulação de sistemas complexos de múltiplos domínios.

## Por que utilizar MATLAB?
O MATLAB é muito utilizado em muitas áreas da Engenharia pela sua alta versatilidade e eficiência em aplicações. Dentro do contexto de um **Fómula SAE**, o MATLAB pode ser muito útil para Modelagem e Simulação de Dinâmica Veicular, Sistemas de Controle e **Validação de Veículo Autônomo**.

## Glossário

- [Comandos Básicos](#comandos-básicos)
- [Operações Básicas](#operações-básicas)
- [Salvando e Carregando Variáveis](#salvando-e-carregando-variáveis)
- [Algumas Funções Matemáticas e Constantes](#algumas-funções-matemáticas-e-constantes)
- [Um Pouco Sobre o Editor MATLAB](#um-pouco-sobre-o-editor-matlab)
- [Vetores e Matrizes](#vetores-e-matrizes)

## Comandos Básicos
Para executar comandos básicos basta digitá-los na janela de comando e apertar **Enter**. Os prompts serão indicados por **>>**
## Operações Básicas
### Adição
Ao digitar 7 + 3 por exemplo, o programa retorna ans (answer) = 10

    >> 7 + 3

    ans =

        10
### Subtração
Para subtração vale a mesma lógica

    >> 7 - 3

    ans =

        4
### Multiplicação

    >> 3 * 5

    ans =

        15
### Divisão

    >> 8 / 4

    ans =

        2
### Atribuição
O operador de atribuição é o **=** e ele guarda o valor da expressão na direita na variável do lado esquerdo

    >> x = 9 - 4

    x = 

        5
É possível incrementar uma variável com ela própria ou até realizar a atribuição e omitir seu valor no final
    
    >> x = x + 5;                      % Forma Clássica
    >> x += 2;                         % Operador Composto, equivalente a x = x + 2
    >> x++;                            % Operador de incremento único, equivalente a x = x + 1
A notação ponto-e-vírgula é a responsável por omitir o valor da variável a cada operação enquanto o caractere **%** permite realizar comentários como o **#** em Python ou **//** em C++. Além disso é possível buscar comandos recentes apertando a tecla de **seta para cima**, experimente!

**Atençao!** Em casos que uma atribuição de uma variável depende de outra, ao alterar a variável independente, será neecessário recalcular a dependente de novo.

    >> x = 4;
    >> y = x / 2;                                 % y = 2
    >> x = 6;                                   % modifica-se a variável independente
    >> y

    y = 
                                                % y = 2 se mantém mesmo após x = 6;
        2

    >> y = x / 2                                % atualização da variável dependente

    y =

        3

## Salvando e Carregando Variáveis
No MATLAB, é possível salvar variáveis no Workspace digitando **save** seguido do nome do arquivo

    >> save nome_arquivo.mat

O comando **clear** remove todas as variáveis salvas no workspace

    >> clear

Para carregar as variáveis de novo no Workspace basta digitar **load** seguido do nome do arquivo

    >> load meu_arquivo.mat
Relembrando que para verificar o valor de uma variável basta digitar seu nome na janela de comando!

Com o comando **clc** é possível limpar a janela de comando

    >> clc
Para carregar uma variável específica basta digitar **load** seguido do nome do arquivo com o nome da variável acompanhando. Já para salvar estas variáveis específicas em um novo arquivo .mat basta digitar **save** seguido do nome do arquivo com o nome da variável acompanhando.

    >> load meu_arquivo1 x                % a extensão .mat não acompanha os comandos desta vez!
    >> save meu_arquivo2 x

## Algumas Funções Matemáticas e Constantes
O MATLAB apresenta suporte para algumas funções e constantes matemáticas como:

    >> sqrt(2);                                   % Raíz Quadrada
    >> abs(-9);                                   % Valor Absoluto
    >> exp(x);                                    % Função Exponencial Natural
    >> sin(-1);                                   % Função Seno
    >> cos(5);                                    % Função Cosseno
    >> tan(3/2);                                  % Função Tangente
    >> log(y);                                    % Função Logaritmo Natural
    >> logb(a);                                   % Função Log de a na base b
    >> round(p);                                  % Arredonda para o inteiro mais próximo
    >> floor(p);                                  % Função Piso
    >> ceil(t);                                   % Função Teto
    >> i;                                         % Unidade Básica Imaginária
    >> pi;                                        % Constante Pi (3,1415...)
    >> Inf;                                       % Infinito

## Um Pouco Sobre o Editor MATLAB

### Executando o programa
Na janela de comando do MATLAB é possível separar scripts nas caixas/blocos de comando cinzas. No botão **RUN**, é possível executar todos os scripts de forma coletiva na ordem em que eles estão no programa. Porém é possível rodar cada bloco de código de forma independente selecionando-os e depois exeutando **RUN SECTION**. É importante ressaltar que o bloco de comando só atualiza o valor de uma variável declarada acima dele se o bloco de comando anterior que contém essa variável for executado antes.

### Manipulando Seções
Para criar uma seção no **Live Editor** utiliza-se o botão **Section Break**. Após a criação da seção é possível escrever texto e blocos de código. Para escrever textos basta clicar no botão **Text** para ativar o modo de edição de texto, já para criar um bloco de código deve-se clicar no botão **Code**.

### Debuggando o Código
O Debbuger do MATLAB avisa com um tracejado em vermelho além do caractere "!" (também em vermelho) onde está o erro de sintaxe do seu código. Já os aviso em amarelo são mensagens de cuidado, não necessariamente essa mensagem indica que o código está completamente errado, mas definitivamente não é um aviso para ser ignorado.

## Vetores e Matrizes
Um único número em MATLAB é um escalar, ele representa um array de dimensão 1x1
### Arrays
Arrays podem ser declarados da seguinte forma

    >> y = [7 9]

    y =

        7     9
Ao separar os números com espaço o MATLAB cria um vetor em forma de matriz linha. Para criar um vetor em forma de matriz coluna é necessário adicionar ponto-e-vírgula entre os números.

    >> v = [5; 3]

    v =


        5
        3
Criar uma matriz exige combinar os dois tipos de vetores. Para criar uma matriz de N linhas é necessário seguir este modelo

    >> M = [linha1; linha2; ...; linhaN]

    M =


        linha1
        linha2
        ...
        linhaN
É possível realizar operações nos elementos da matriz na hora de declará-la. Além disso, pode-se utilizar vírgula para separar os elementos de um linha ou até espaçamento com vírgula. Fica a cargo do leitor a melhor maneira de se declarar uma matriz.

    >> A = [3^2, 5/2, 8];
    >> B=[6,11,4.5,1];

### Métodos para Criação de Vetores
Para criar um vetor linha que começa em um número n e vai até p de um em um basta utilizar o operador ":"

    >> V = 1 : 3                                      % Colchetes não são necessários aqui!

    V =

        1     2     3
Também é possível alterar a razão do espaçamento entre os números do vetor, a sintaxe para isso é

    >> U = 20 : 2 :26                                    % primeiro elemento:razão:último elemento

    U =

        20     22     24     26
A função **linspace** (linearly spaced) permite criar um vetor cujo tamanho já é conhecido

    >> w = linspace(0,1,5)                % primeiro elemento,último elemento,quantidade de elementos

    w = 

        0     0.250     0.500     0.750     1.000
A **Transposição de Matrizes** pode ser combinada com os métodos ":" e linspace para a criação de um vetor coluna linearmente espaçado. O operador de transposição é o " ' " (uma aspa simples).

    >> x = 1 : 3

    x =

        1     2     3

    x = x'

    x =

        1
        2
        3
É possível otimizar esse processo realizando

    >> t = (3:2:9)'

    t =

        3
        5
        7
        9
### Criando Arrays com Funções
Para criar uma matriz quadrada de dimensões n x n de números aleatórios utiliza-se o método **rand**

    >> x = rand(2);
O método **rand** também existe para matrizes de dimensões n x m

    >> y = rand(n, m)                                     % rand(linhas, colunas)
Uma matriz nula pode ser criada a partir de uma função parecida com rand, **zeros**. Já uma matriz cujos números são todos 1, pode ser criada com a função **ones**

    >> z = zeros(2, 3);
    >> o = ones(6, 11);
Para obter as dimensões de uma matriz pode ser útil aplicar o método **size**. Levando em conta a matriz z do exemplo anterior,

    >> size(z)

    ans =

          6     11
