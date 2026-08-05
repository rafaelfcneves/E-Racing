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
- [Plotando Vetores](#plotando-vetores)
- [Materiais de Apoio e Aprofundamento](#materiais-de-apoio-e-aprofundamento)

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
É possível utilizar vetores para criar matrizes, por exemplo

    >> x = [1; 2];
    >> y = [3; 4];
    >> z = [x y]                      % Insere-se vetores coluna 2 x 1 para formar uma matriz 2 x 2

    z =

        1     3
        2     4

    >> a = [1, 2];
    >> b = [3, 4];                   % Insere-se vetores linha 1 x 2 para formar uma matriz 2 x 2
    >> c = [a; b]

    c =

        1     2
        3     4
    
### Criando e Manipulando Arrays com Funções
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

    >> [n, m] = size(z)                % Atribuindo as dimensões a variáveis

    n =

        6
    m =

        11
A função **max** e **min** no MATLAB serve para encontrar os valores máximo e mínimo em um vetor ou matriz. Além disso, é possível aplicar funções sobre uma matriz executando, assim, esssa função para cada um dos elementos de uma matriz ou vetor e obtendo uma nova matriz com os novos elementos calculados.

    >> xmax = max(V);                                                        % máximo do vetor V
    >> xmin = max(V);
    >> S = sin(M);                       % matriz cujos elementos são os senos dos elementos de M
    
    >> xmax = max(M);                    % Seja M uma matriz, essa função retorna um vetor linha
                                         % contendo os maiores elementos de cada coluna
### Operações Sobre Vetores
Adicionando um escalar a todos os elementos de um vetor

    >> x = [1, 2, 3];
    >> y = x + 2

    y

        3     4     5
Somar arrays requer que eles sejam de mesma ordem, ou seja, ambos devem ser de dimensões n x m. Para somar arrays então faz-se

    >> v1 = [1, 2, 3, 4, 5];                       % 1 x 5
    >> v2 = [6, 7, 8, 9, 10];                         % 1 x 5
    >> vs = v1 + v2

    vs =

        7     9     11     13     15
Multiplicar ou dividir um vetor por um escalar pedem as seguintes notações

    >> A = [4, 7, 3];
    >> B = 2*A

    B =

        8     14     6
    
    >> C = B/4

    C =

        2     3.50     1.50
O MATLAB suporta dois tipos de multiplicação entre matrizes. O primeiro é a forma tradicional e já formalizada na matemática, em que duas matrizes A e B suportam multiplicação entre si se forem de ordens n x m e m x p respectivamente. Esse processo resulta em uma matriz C de ordem n x p. A outra forma de multiplicar matrizes no MATLAB é multiplicar cada elemento a(ij) da matriz A(n x m) pelo elemento b(ij) da matriz B também n x m. O resultado dessa operação gera uma matriz C de ordem n x m tal que c(ij) = a(ij)*b(ij).

    >> A = [1, 2, 3; 4, 5, 6];                                                       % A(2 x 3)
    >> B = [9, 8, 7; 6, 5, 4; 3, 2, 1];                                                  % B(3 x 3)
    >> C = A * B

    C =                                                                                 % C(2 x 3)

        30     24     18
        84     69     54

    >> D = [6, 5, 4; 3, 2, 1];                                                          % D(2 x 3)
    >> E = A .* D                       % Utiliza-se o operador ".*" para o segundo tipo de multiplicação

    E =

        6    10    12
        12   10    6

## Consultando a Documentação de Funções
O método **doc** abre uma guia que contém a documentação da função seguida do comando doc. Algumas das funções mais utilizadas no MATLAB são: max, min, randi, plot, mean, det e size.

    >> doc plot

## Plotando Gráficos
### Plotando Vetores
Pode-se plotar vetores de mesma quantidade de elementos utilizando a função **plot**. Um dos vetores será responsável por atribuir as coordenadas x dos pontos do gráfico e outro pelas coordenadas y. Por fim, dois vetores se combinarão para formar um gráfico contínuo e, por consequência, talvez aproximados em alguns pontos.

    >> vx = [1, 2];
    >> vy = [2, 4];
    >> plot(vx, vy)                                 % Plotando uma reta de equação y = 2x
Plotar somente pontos no gráfico requer um parâmetro adicional na função plot, esse parâmetro indica a cor e o caractere que será exibido no ponto.

    >> plot(vx, vy, "r*")                       % Plota os pontos de vx e vy em forma de um asterisco 
                                                % (*) vermelho (r referente a red)
Caso seja preciso ligar esses pontos de uma forma que não seja por uma linha sólida, será preciso informar o tipo de tracejado

    >> plor(vx, vy, "r--*")                     % "--" informa o tipo de tracejado do gráfico
Para mais formas de estilização consulte [Line Specification](https://www.mathworks.com/help/matlab/ref/plot.html#btzitot_sep_mw_3a76f056-2882-44d7-8e73-c695c0c54ca8). \
Comparar gráficos é muitas vezes essencial e, portanto, o MATLAB possui recursos para plotar um gráficos em um mesmo plano com o comando **hold on**. O comando hold on plota todos os gráficos abaixo dele no mesmo plano do gráfico que vem logo antes do hold on. Para desativar essa sobreposição basta digitar **hold off**.

    >> plot(x1,y1)                              % Gráfico 1  
    >> hold on                                  % Plota o gráfico 2 sobre o gráfico 1
    >> plot(x2,y2)                              % Gráfico 2

## Materiais de Apoio e Aprofundamento
https://matlabacademy.mathworks.com/details/matlab-onramp/gettingstarted
https://www.ime.unicamp.br/~encpos/VIII_EnCPos/Apostila_Matlab.pdf \
https://www.ic.unicamp.br/~rdahab/cursos/matlab/#material_didatico \
https://mec.ita.br/~adade/Matlab/Web/introduz.htm#Ao%20leitor