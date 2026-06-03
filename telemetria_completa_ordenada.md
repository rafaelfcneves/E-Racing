# Implementacao do frontend

Este documento descreve como o frontend de telemetria esta implementado hoje,
quais sao seus modulos principais e onde alterar cada tipo de comportamento.

## 1. Stack

- SolidJS para UI reativa
- Vite para build e dev server
- Web Worker para ingestao e preparo da telemetria
- uPlot para os graficos
- Canvas 2D para os gauges do cockpit

## 2. Estrutura geral

Entradas principais:

- [src/index.jsx](/Users/joaogabriel/Documents/TelemetriaV2.0/telemetry-server/static/src/index.jsx)
- [src/App.jsx](/Users/joaogabriel/Documents/TelemetriaV2.0/telemetry-server/static/src/App.jsx)

Areas principais da aplicacao:

1. autenticacao e sessao
2. store reativo + worker
3. superficie de analise
4. superficie de cockpit

## 3. Fluxo de dados

O fluxo principal hoje e este:

1. usuario faz login;
2. frontend recebe token;
3. `store.js` abre WebSocket autenticado;
4. `worker.js` recebe frames binarios CAN;
5. worker decodifica sinais e popula buffers;
6. worker envia ultimo valor de cada sinal para a UI;
7. componentes reativos atualizam cards, gauges, selector e graficos.

Resumo visual:

```text
Login -> token -> WebSocket -> worker -> store reativo -> componentes
```

## 4. Modulos principais

### 4.1 App e navegacao

Arquivo:

- [App.jsx](/Users/joaogabriel/Documents/TelemetriaV2.0/telemetry-server/static/src/App.jsx)

Responsabilidades:

- restaurar sessao;
- login/logout;
- alternar abas `analise` e `cockpit`;
- manter `selectedSignals`;
- manter `windowSeconds`.

O `App` funciona como orquestrador de alto nivel. A logica especifica fica
delegada aos componentes e utils especializados.

### 4.2 Store e worker

Arquivos:

- [store.js](/Users/joaogabriel/Documents/TelemetriaV2.0/telemetry-server/static/src/store.js)
- [worker.js](/Users/joaogabriel/Documents/TelemetriaV2.0/telemetry-server/static/src/workers/worker.js)

Responsabilidades do `store.js`:

- manter `signals` e `status`;
- conectar/desconectar do worker;
- expor `requestBuffer()` para os graficos;
- expor `requestLatest()` para snapshots.

Responsabilidades do `worker.js`:

- abrir WebSocket;
- receber frames binarios;
- decodificar sinais CAN;
- manter buffers circulares;
- responder requests de historico.

Arquivos de apoio:

- [circularBuffer.js](/Users/joaogabriel/Documents/TelemetriaV2.0/telemetry-server/static/src/utils/circularBuffer.js)
- [lttb.js](/Users/joaogabriel/Documents/TelemetriaV2.0/telemetry-server/static/src/utils/lttb.js)
- [canDecode.js](/Users/joaogabriel/Documents/TelemetriaV2.0/telemetry-server/static/src/utils/canDecode.js)

### 4.3 Configuracao

Arquivos:

- [serverConfig.js](/Users/joaogabriel/Documents/TelemetriaV2.0/telemetry-server/static/src/config/serverConfig.js)
- [dashboardConfig.js](/Users/joaogabriel/Documents/TelemetriaV2.0/telemetry-server/static/src/config/dashboardConfig.js)
- [brandConfig.js](/Users/joaogabriel/Documents/TelemetriaV2.0/telemetry-server/static/src/config/brandConfig.js)

Uso:

- `serverConfig.js`: origem HTTP/WS
- `dashboardConfig.js`: sinais fixos, gauges, layouts default
- `brandConfig.js`: logo e identidade basica da equipe

### 4.4 Superficie de analise

Componentes:

- [StatusBar.jsx](/Users/joaogabriel/Documents/TelemetriaV2.0/telemetry-server/static/src/components/StatusBar/StatusBar.jsx)
- [SignalSelector.jsx](/Users/joaogabriel/Documents/TelemetriaV2.0/telemetry-server/static/src/components/SignalSelector/SignalSelector.jsx)
- [TimeWindowControl.jsx](/Users/joaogabriel/Documents/TelemetriaV2.0/telemetry-server/static/src/components/TimeWindowControl/TimeWindowControl.jsx)
- [MotecChart.jsx](/Users/joaogabriel/Documents/TelemetriaV2.0/telemetry-server/static/src/components/MotecChart/MotecChart.jsx)

#### StatusBar

Mostra sinais fixos e estatisticas simples.

Arquivos de apoio:

- [SignalCard.jsx](/Users/joaogabriel/Documents/TelemetriaV2.0/telemetry-server/static/src/components/StatusBar/SignalCard.jsx)
- [useSignalStats.js](/Users/joaogabriel/Documents/TelemetriaV2.0/telemetry-server/static/src/components/StatusBar/useSignalStats.js)

#### SignalSelector

Lista sinais recebidos, permite busca, agrupamento e selecao para grafico
customizado.

Arquivo de apoio:

- [signalGrouping.js](/Users/joaogabriel/Documents/TelemetriaV2.0/telemetry-server/static/src/utils/signalGrouping.js)

#### MotecChart

Orquestra o uPlot.

Arquivos de apoio:

- [useChartData.js](/Users/joaogabriel/Documents/TelemetriaV2.0/telemetry-server/static/src/components/MotecChart/useChartData.js)
- [chartOptions.js](/Users/joaogabriel/Documents/TelemetriaV2.0/telemetry-server/static/src/components/MotecChart/chartOptions.js)
- [chartHelpers.js](/Users/joaogabriel/Documents/TelemetriaV2.0/telemetry-server/static/src/utils/chartHelpers.js)
- [telemetryUtils.js](/Users/joaogabriel/Documents/TelemetriaV2.0/telemetry-server/static/src/utils/telemetryUtils.js)

## 5. Superficie de cockpit

Componentes:

- [Cockpit.jsx](/Users/joaogabriel/Documents/TelemetriaV2.0/telemetry-server/static/src/components/Cockpit/Cockpit.jsx)
- [CockpitGauge.jsx](/Users/joaogabriel/Documents/TelemetriaV2.0/telemetry-server/static/src/components/Cockpit/CockpitGauge.jsx)
- [RaceVideoPanel.jsx](/Users/joaogabriel/Documents/TelemetriaV2.0/telemetry-server/static/src/components/Cockpit/RaceVideoPanel.jsx)
- [TrackMapPanel.jsx](/Users/joaogabriel/Documents/TelemetriaV2.0/telemetry-server/static/src/components/Cockpit/TrackMapPanel.jsx)
- [trackMapMetrics.js](/Users/joaogabriel/Documents/TelemetriaV2.0/telemetry-server/static/src/components/Cockpit/trackMapMetrics.js)

O cockpit hoje ja entrega:

- gauges operacionais;
- painel de onboard;
- painel de mapa.

Os dois ultimos ainda dependem de dados/feeds reais do backend.

### 5.1 Track map: enriquecimento e sincronia com coleta

Mudancas recentes no mapa de pista:

1. o marcador do carro foi mantido no mesmo `svg` da polilinha para evitar drift por proporcao;
2. com coleta pausada, a posicao do carro fica congelada (nao continua rastreando novos `track_pose`);
3. foi incluido marcador fixo do ponto de inicio da volta;
4. o rodape do mapa passou a exibir metricas operacionais.

Metricas exibidas hoje:

- comprimento da pista (`track.length_m`);
- distancia restante para completar a volta;
- progresso percentual da volta;
- velocidade instantanea;
- rumo (heading).

Calculo da distancia restante:

- prioridade para projecao geometrica do carro sobre a polilinha da pista;
- fallback para `vehicle.distance_m` quando necessario.

Essa logica foi modularizada no arquivo `trackMapMetrics.js` para manter
`TrackMapPanel.jsx` focado em renderizacao e estado de exibicao.

## 6. Sistema de gauges

Arquivos:

- [Gauge.jsx](/Users/joaogabriel/Documents/TelemetriaV2.0/telemetry-server/static/src/components/Gauge/Gauge.jsx)
- [gaugeCanvas.js](/Users/joaogabriel/Documents/TelemetriaV2.0/telemetry-server/static/src/components/Gauge/gaugeCanvas.js)
- [gaugeUtils.js](/Users/joaogabriel/Documents/TelemetriaV2.0/telemetry-server/static/src/components/Gauge/gaugeUtils.js)

Separacao atual:

- `Gauge.jsx`: lifecycle e leitura reativa do sinal
- `gaugeCanvas.js`: desenho do gauge
- `gaugeUtils.js`: geometria, formatacao e regras puras

Essa divisao esta boa e ja evita acoplamento desnecessario entre UI e canvas.

## 7. Estilo

Arquivos:

- [index.css](/Users/joaogabriel/Documents/TelemetriaV2.0/telemetry-server/static/src/index.css)
- [components.css](/Users/joaogabriel/Documents/TelemetriaV2.0/telemetry-server/static/src/styles/components.css)

Regra atual:

- tokens globais em `index.css`;
- estilos compartilhados em `components.css`;
- estilos especificos ao lado dos componentes.

## 8. O que ainda vale modularizar?

No estado atual, eu nao vejo uma modularizacao obrigatoria pendente. A maioria
das responsabilidades ja esta em fronteiras razoaveis.

Os candidatos possiveis seriam:

1. extrair o `CAN_MAP` do worker para um modulo proprio;
2. extrair configuracoes de dominio/limites para um modulo semantico separado;
3. criar uma camada de "view models" para selector, status bar e cockpit.

### Avaliacao

#### 8.1 Extrair `CAN_MAP`

Pode fazer sentido quando:

- backend e frontend passarem a compartilhar uma fonte unica de verdade;
- o mapa crescer muito;
- o time quiser testar a decodificacao isoladamente.

Hoje isso e uma modularizacao razoavel, mas nao urgente.

#### 8.2 Extrair limites semanticos

Pode fazer sentido se:

- o numero de familias de sinais crescer;
- houver muito ajuste fino de faixa operacional.

Hoje `dashboardConfig.js` + `telemetryUtils.js` ainda dao conta bem.

#### 8.3 Criar camada adicional de view model

Hoje isso seria over-engineering.

Os componentes ja sao relativamente focados, e inserir mais uma camada agora
provavelmente aumentaria atrito sem ganho claro.

## 9. Veredito sobre modularizacao

Minha leitura e:

- ha espaco para extrair `CAN_MAP` no futuro;
- ha espaco para consolidar limites semanticos se a matriz de sinais crescer;
- qualquer modularizacao alem disso, agora, tende a ser over-engineering.

Ou seja: o front esta num ponto bom de estrutura. O valor maior agora esta em
integrar com dados reais e estabilizar contrato com o backend, nao em abrir mais
camadas.

## 10. Como rodar

Instalacao:

```bash
pnpm install
```

Desenvolvimento:

```bash
pnpm dev
```

Mock backend:

```bash
pnpm mock:backend
```

Teste do cockpit com mapa/tracking:

```bash
pnpm test:cockpit-map
```

Esse teste usa `scripts/test-cockpit-map.mjs` para iniciar o Vite e o mock backend juntos.
O mock aceita `admin` como administrador e `member`/`membro` como membro,
envia frames CAN binários e também mensagens JSON
`track_status`, `track_map` e `track_pose` pelo mesmo WebSocket.

Passo a passo:

1. abrir `http://localhost:5173/`;
2. fazer login com `admin` para testar controle de coleta ou `member` para
   testar consumo sem start/stop;
3. clicar em `Iniciar coleta`;
4. abrir a aba `Cockpit`;
5. aguardar o estado mudar de `aprendendo primeira volta` para `tracking`.

Para ajustar o tempo da primeira volta simulada:

```bash
MOCK_TRACK_LAP_SEC=10 pnpm test:cockpit-map
```

Build:

```bash
pnpm build
```

## 11. Documentos relacionados

- [frontend-telemetry-decisions.md](/Users/joaogabriel/Documents/TelemetriaV2.0/telemetry-server/static/docs/frontend-telemetry-decisions.md)
- [backend-integration-guide.md](/Users/joaogabriel/Documents/TelemetriaV2.0/telemetry-server/static/docs/backend-integration-guide.md)


# Decisoes pendentes de telemetria no frontend

Este documento registra as decisoes que ainda dependem do que o time quer
extrair da telemetria real e onde os limites minimos/maximos importam no
frontend.

O objetivo e evitar que valores de UI sejam tratados como "verdade tecnica"
quando na pratica eles sao apenas defaults de operacao.

## Estado atual

Hoje o frontend ja consome:

- stream WebSocket binario com frames CAN;
- login HTTP simples para obter token;
- buffers historicos sob demanda via `requestBuffer()` no worker local;
- snapshot do ultimo valor por sinal para cards, gauges e lista de sinais.

Os pontos abaixo ainda precisam de definicao funcional e/ou validacao com dado
real continuo.

## 1. Quais sinais devem ir para cada superficie

Nem todo sinal disponivel no CAN precisa aparecer em todo lugar. Hoje a tela
esta organizada em quatro superficies:

1. `StatusBar`
2. `SignalSelector`
3. `MotecChart`
4. `Cockpit`

### 1.1 StatusBar

Arquivo base:

- [dashboardConfig.js](/Users/joaogabriel/Documents/TelemetriaV2.0/telemetry-server/static/src/config/dashboardConfig.js)

Decisao pendente:

- definir exatamente quais sinais sao "pinned";
- decidir se o criterio e operacional, diagnostico ou visibilidade para piloto;
- decidir se max/min/media devem valer por sessao inteira ou por janela movel.

Hoje os cards acumulam estatisticas desde que o sinal comecou a chegar no front.
Se a leitura desejada for "estatistica da ultima volta", "do stint atual" ou
"dos ultimos 30s", o comportamento precisa mudar.

### 1.2 SignalSelector

Arquivos base:

- [SignalSelector.jsx](/Users/joaogabriel/Documents/TelemetriaV2.0/telemetry-server/static/src/components/SignalSelector/SignalSelector.jsx)
- [signalGrouping.js](/Users/joaogabriel/Documents/TelemetriaV2.0/telemetry-server/static/src/utils/signalGrouping.js)

Decisao pendente:

- revisar a taxonomia dos grupos;
- decidir aliases mais amigaveis para sinais crus;
- definir se alguns sinais nao devem aparecer para o operador final.

Hoje o agrupamento e heuristico, baseado no nome do sinal.

### 1.3 Graficos

Arquivos base:

- [dashboardConfig.js](/Users/joaogabriel/Documents/TelemetriaV2.0/telemetry-server/static/src/config/dashboardConfig.js)
- [telemetryUtils.js](/Users/joaogabriel/Documents/TelemetriaV2.0/telemetry-server/static/src/utils/telemetryUtils.js)

Decisao pendente:

- definir quais layouts default devem sempre existir;
- decidir quando usar dominio fixo e quando usar dominio dinamico;
- decidir se sinais diferentes podem coexistir no mesmo eixo Y.

Hoje o frontend assume dominio fixo para familias conhecidas e dinamico para o
resto.

### 1.4 Cockpit

Arquivos base:

- [dashboardConfig.js](/Users/joaogabriel/Documents/TelemetriaV2.0/telemetry-server/static/src/config/dashboardConfig.js)
- [Cockpit.jsx](/Users/joaogabriel/Documents/TelemetriaV2.0/telemetry-server/static/src/components/Cockpit/Cockpit.jsx)

Decisao pendente:

- quais gauges precisam existir no cockpit;
- se os gauges devem representar valor instantaneo, filtrado ou suavizado;
- quais limites operacionais devem ser mostrados como normal, alerta e critico.

## 2. Onde minimos e maximos importam

Nem todo min/max tem o mesmo significado. Hoje existem pelo menos quatro tipos.

### 2.1 Escala visual do gauge

Exemplo:

- RPM A0 e RPM B0 usam `min`, `max`, `warnMax`, `critMax` em `GAUGE_CONFIG`.

Esses valores impactam:

- angulo do ponteiro;
- labels dos ticks;
- cor da faixa de alerta/critico;
- percepcao visual de "saturacao".

Definicao que o time precisa fechar:

- faixa operacional real por sinal;
- se a escala deve ser simetrica ou nao;
- se valores negativos fazem sentido visualmente no cockpit.

Hoje RPM esta com:

- `min: 0`
- `max: 10000`
- `warnMax: 8500`
- `critMax: 9500`

Esses numeros sao defaults de interface e devem ser validados com o time tecnico.

### 2.2 Dominio do eixo Y dos graficos

Arquivo base:

- [telemetryUtils.js](/Users/joaogabriel/Documents/TelemetriaV2.0/telemetry-server/static/src/utils/telemetryUtils.js)

Esses limites impactam:

- legibilidade da serie;
- espaco util do grafico;
- comparacao entre sessoes;
- risco de "achatar" a curva por causa de um dominio excessivo.

Definicao que o time precisa fechar:

- quais familias de sinal merecem dominio fixo;
- quais devem sempre autoajustar;
- se o dominio deve ser o mesmo no cockpit e na analise.

Hoje os defaults sao:

- rpm: `0..10000`
- acceleration: `-15..15`
- temperature: `0..120`
- voltage: `0..500`
- power: `-100..100`

### 2.3 Estatisticas dos cards

Arquivos base:

- [SignalCard.jsx](/Users/joaogabriel/Documents/TelemetriaV2.0/telemetry-server/static/src/components/StatusBar/SignalCard.jsx)
- [useSignalStats.js](/Users/joaogabriel/Documents/TelemetriaV2.0/telemetry-server/static/src/components/StatusBar/useSignalStats.js)

Os valores max/min/media podem significar:

- max/min/media da sessao;
- max/min/media desde o ultimo reset da UI;
- max/min/media de uma janela movel;
- max/min/media por volta.

Hoje o significado e:

- acumulado desde o inicio da sessao na UI.

Se isso nao refletir o que a equipe quer ler na operacao, esse ponto deve ser
mudado antes de considerar a superficie final.

### 2.4 Validacao de sanidade

Alguns sinais podem precisar de clamp, filtro ou deteccao de outlier antes de
virarem UI.

Isso e importante especialmente para:

- RPM
- temperatura
- tensao
- potencia
- aceleracao

Definicao que o time precisa fechar:

- quais sinais aceitam valor negativo;
- quais sinais devem ser filtrados;
- quais limites caracterizam erro de leitura e devem ser ignorados.

## 3. Perguntas que o time precisa responder

Antes de consolidar os valores definitivos no front, estas perguntas deveriam
ser respondidas:

1. Quais sinais sao prioridade operacional?
2. Quais sinais sao prioridade diagnostica?
3. O cockpit deve mostrar valores crus ou suavizados?
4. Max/min/media sao por sessao, por volta ou por janela?
5. RPM deve aceitar valores negativos em algum contexto visual?
6. Quais limites merecem faixa de alerta e critico?
7. Existem sinais que nao devem aparecer no selector final?
8. O dominio dos graficos deve ser padronizado entre eventos?

## 4. Onde editar no frontend quando essas decisoes forem fechadas

### Sinais fixos da StatusBar

- [dashboardConfig.js](/Users/joaogabriel/Documents/TelemetriaV2.0/telemetry-server/static/src/config/dashboardConfig.js)

### Gauges do cockpit e seus limites

- [dashboardConfig.js](/Users/joaogabriel/Documents/TelemetriaV2.0/telemetry-server/static/src/config/dashboardConfig.js)

### Dominio fixo dos graficos

- [telemetryUtils.js](/Users/joaogabriel/Documents/TelemetriaV2.0/telemetry-server/static/src/utils/telemetryUtils.js)

### Regras de agrupamento dos sinais

- [signalGrouping.js](/Users/joaogabriel/Documents/TelemetriaV2.0/telemetry-server/static/src/utils/signalGrouping.js)

### Semantica de max/min/media

- [useSignalStats.js](/Users/joaogabriel/Documents/TelemetriaV2.0/telemetry-server/static/src/components/StatusBar/useSignalStats.js)

## 5. Recomendacao pratica

Antes de congelar a UI, vale fazer uma rodada curta com o time tecnico para
preencher uma tabela com:

- nome do sinal;
- unidade;
- faixa esperada;
- aceita negativo? sim/nao;
- usar no cockpit? sim/nao;
- usar em card fixo? sim/nao;
- usar dominio fixo no grafico? sim/nao;
- alerta em;
- critico em.

Essa tabela pode virar a origem de verdade para os arquivos de configuracao do
frontend.


# Grafico padrao de historico relativo por RPM

## Objetivo

Criar uma superficie de analise em que o RPM seja o sinal de referencia para
todo o historico capturado na sessao. O eixo X deixa de representar horario real
e passa a representar tempo relativo:

- `00:00.000` = primeiro frame valido recebido pela telemetria na sessao;
- `stop` = ultimo frame valido disponivel no buffer local;
- a janela selecionada no historico vira o contexto para consultar outros
  sinais naquele mesmo instante de analise.

## Comportamento esperado

1. Exibir um grafico padrao fixo no topo da aba `Analise`.
2. Plotar os sinais de RPM como referencia:
   - `act_Speed_A0`
   - `act_Speed_B0`
   - `act_Speed_A13`
   - `act_Speed_B13`
3. Converter o eixo X de timestamp Unix para segundos relativos ao boot da
   sessao.
4. Permitir arrastar uma janela no grafico para marcar o trecho de interesse.
5. Usar o cursor/janela selecionada para consultar os valores dos sinais
   selecionados no `SignalSelector`.
6. Calcular resumo da janela selecionada por sinal: minimo, media, maximo e
   quantidade de amostras.
7. Plotar um grafico detalhado dos sinais selecionados recortado na janela
   arrastada.
8. Permitir inicio/fim da coleta pelo frontend sem encerrar a sessao autenticada.
9. Manter os graficos existentes por janela movel para nao quebrar a operacao
   atual.

## Passo a passo de implementacao

### 1. Base de dados

- Reutilizar os buffers historicos ja mantidos pelo worker.
- Buscar o historico completo usando `requestBuffer(name, threshold, null)`.
- Calcular `boot` como o menor timestamp inicial entre os sinais carregados.
- Calcular `stop` como o maior timestamp final entre os sinais carregados.
- Converter o eixo X para `timestamp - boot`.

### 2. Grafico de referencia

- Criar `HistoryReferenceChart`.
- Reutilizar `uPlot` e a configuracao visual existente.
- Adicionar suporte a eixo X relativo em `buildUPlotOptions`.
- Registrar `setCursor` para obter o tempo relativo sob o cursor.
- Registrar `setSelect` para obter a janela arrastada pelo usuario.

### 3. Leitura contextual de sinais

- Carregar, alem dos RPMs, os sinais selecionados pelo usuario.
- Para cada sinal selecionado, buscar a amostra mais proxima do timestamp
  absoluto equivalente ao cursor.
- Mostrar valor, unidade e tempo relativo da amostra encontrada.

### 4. Integracao inicial

- Inserir o novo grafico como primeiro bloco da `chart-area`.
- Manter `TimeWindowControl` controlando apenas os graficos moveis atuais.
- Usar a selecao do `SignalSelector` como lista de sinais de comparacao.
- Expor `Iniciar coleta` / `Encerrar coleta` na `TopBar`.
- Enquanto a coleta esta em tempo real, mostrar apenas graficos moveis padrao.
- Durante a coleta, todos os graficos usam tempo relativo ao boot da sessao,
  nao horario absoluto.
- Quando a coleta e encerrada, congelar os buffers locais e mostrar o grafico
  historico relativo por RPM.

### 5. Estados da tela

- `idle`: usuario autenticado e conexao pronta, mas nenhuma coleta ativa.
- `live`: coleta em tempo real; foco em operacao, cards e graficos moveis.
- `stopped`: coleta encerrada; foco em historico, selecao de janela e analise.

Nesta primeira versao, o frontend congela a coleta no worker local sem fechar o
WebSocket. Quando o backend tiver contrato proprio para iniciar/pausar envio, o
mesmo botao deve chamar esse comando em vez de apenas controlar a coleta local.

### 6. Armazenamento e logs para analise posterior

Objetivo: cada periodo entre `Iniciar coleta` e `Encerrar coleta` deve virar uma
sessao historica consultavel depois.

Modelo recomendado:

- `telemetry_sessions`
  - `id`
  - `started_at`
  - `stopped_at`
  - `driver` ou `operator`
  - `car_id`
  - `notes`
  - `status`: `recording`, `closed`, `archived`
- `telemetry_samples`
  - `session_id`
  - `timestamp_abs`
  - `timestamp_rel`
  - `can_id`
  - `signal_name`
  - `value`
  - `unit`

Fluxo recomendado:

1. `Iniciar coleta` cria uma nova sessao no backend.
2. Backend continua recebendo frames do carro e grava cada amostra com
   `session_id`.
3. `timestamp_rel` e calculado como `timestamp_abs - started_at`.
4. `Encerrar coleta` marca `stopped_at` e fecha a sessao.
5. O frontend pode carregar a sessao fechada por id e reconstruir o grafico de
   RPM completo, sem depender do buffer local.

Para performance:

- manter dados brutos completos para auditoria;
- gerar downsample/cache por sessao para graficos longos;
- permitir consulta por faixa relativa: `session_id + start_seconds + end_seconds`;
- retornar estatisticas agregadas da janela quando o usuario arrastar um trecho.

### 7. Evolucoes recomendadas

- Persistir sessoes historicas no backend para analisar stints antigos, nao
  apenas o buffer local em memoria.
- Criar zoom por janela selecionada, com graficos derivados mostrando apenas o
  trecho marcado.
- Adicionar estatisticas da janela: min, max, media e delta por sinal.
- Permitir escolher qual RPM e o canal de referencia principal.
- Marcar eventos de boot/stop, falhas e voltas quando esses metadados existirem.

## Estado da primeira entrega

Implementado:

- componente `HistoryReferenceChart`;
- componentes dedicados para grafico de RPM, grafico da janela e tabela de
  estatisticas;
- eixo X relativo em `chartOptions`;
- helpers para limites de historico e busca de amostra mais proxima;
- integracao na aba `Analise`;
- exibicao de cursor, janela selecionada e valores dos sinais selecionados.
- resumo da janela selecionada com min, media, max e quantidade de amostras.
- grafico detalhado dos sinais selecionados dentro da janela arrastada.
- fluxo de tela `idle` / `live` / `stopped`.
- botao `Iniciar coleta` / `Encerrar coleta`, sem logout e sem fechar o
  WebSocket.
- eixo relativo tambem nos graficos ao vivo, usando a primeira amostra da coleta
  como boot.

Ainda nao implementado:

- persistencia backend de sessoes historicas;
- contrato backend para iniciar/pausar envio real por sessao;
- zoom/subgraficos sincronizados pela janela selecionada.


# Plano de feature: Downloads de logs e perfis de acesso

Este documento planeja a implementacao de uma nova aba de downloads na
telemetria e a separacao entre dois perfis de usuario:

- `admin`: pode iniciar coleta, encerrar coleta e consumir dados/logs.
- `member`: pode consumir dados/logs, mas nao pode iniciar nem encerrar coleta.

O objetivo e deixar a arquitetura pronta para o backend definir os formatos
finais dos arquivos de log, sem amarrar o frontend a CSV, JSON, binario, MoTeC
ou qualquer outro formato especifico.

## 1. Contexto atual

Arquivos principais ja existentes:

- [src/App.jsx](/Users/joaogabriel/Documents/TelemetriaV2.0/telemetry-server/static/src/App.jsx)
- [src/components/TopBar/TopBar.jsx](/Users/joaogabriel/Documents/TelemetriaV2.0/telemetry-server/static/src/components/TopBar/TopBar.jsx)
- [src/components/TabBar/TabBar.jsx](/Users/joaogabriel/Documents/TelemetriaV2.0/telemetry-server/static/src/components/TabBar/TabBar.jsx)
- [src/utils/auth.js](/Users/joaogabriel/Documents/TelemetriaV2.0/telemetry-server/static/src/utils/auth.js)
- [src/services/telemetryCollection.js](/Users/joaogabriel/Documents/TelemetriaV2.0/telemetry-server/static/src/services/telemetryCollection.js)
- [src/config/serverConfig.js](/Users/joaogabriel/Documents/TelemetriaV2.0/telemetry-server/static/src/config/serverConfig.js)

Hoje:

- `App.jsx` controla sessao, aba ativa e modo de telemetria.
- `TopBar.jsx` renderiza o botao de iniciar/encerrar coleta.
- `TabBar.jsx` recebe uma lista estatica de abas.
- `auth.js` guarda apenas o token e valida expiracao.
- A coleta e habilitada localmente via worker com `setTelemetryCollectionEnabled`.
- Start/stop e persistencia dos limites da coleta passam por
  `telemetryCollection.js` antes de sincronizar o estado local.

## 2. Escopo funcional

### 2.1 Nova aba `Downloads`

A nova aba deve permitir:

1. listar logs disponiveis;
2. filtrar logs por periodo, tipo/formato, status e texto;
3. visualizar metadados basicos de cada log;
4. baixar cada log no formato entregue pelo backend;
5. atualizar manualmente a lista;
6. indicar estados de carregamento, erro, lista vazia e download em andamento.

O frontend nao deve converter o arquivo no MVP. Ele deve respeitar:

- `download_url`, quando o backend entregar URL direta;
- ou endpoint de download autenticado, quando o backend exigir header
  `Authorization`.

### 2.2 Perfis de acesso

Perfis:

| Perfil | Iniciar coleta | Encerrar coleta | Ver analise | Ver cockpit | Ver downloads | Baixar logs |
| --- | --- | --- | --- | --- | --- | --- |
| `admin` | Sim | Sim | Sim | Sim | Sim | Sim |
| `member` | Nao | Nao | Sim | Sim | Sim | Sim |

Regras de produto:

- O membro deve conseguir acompanhar telemetria e consumir logs.
- O membro nao deve ver comandos que parecam acionaveis para iniciar/encerrar
  coleta.
- Mesmo que a UI esconda o botao, o backend precisa bloquear essas operacoes
  para usuarios sem permissao.

## 3. Arquitetura proposta

### 3.1 Modelo de sessao no frontend

Expandir a sessao atual de:

```js
{ token, username, mode: 'live' }
```

para:

```js
{
  token: string,
  username: string,
  role: 'admin' | 'member',
  permissions: string[],
  mode: 'live'
}
```

Permissoes recomendadas:

```js
const PERMISSIONS = {
  telemetryStart: 'telemetry:start',
  telemetryStop: 'telemetry:stop',
  logsRead: 'logs:read',
  logsDownload: 'logs:download',
}
```

O frontend pode derivar `canStartTelemetry`, `canStopTelemetry`,
`canReadLogs` e `canDownloadLogs` a partir de `permissions`.

### 3.2 Autenticacao e claims

O backend deve retornar o perfil no login. Existem duas opcoes aceitaveis:

Opcao A, resposta explicita:

```json
{
  "ok": true,
  "token": "jwt",
  "user": {
    "username": "joao",
    "role": "admin",
    "permissions": [
      "telemetry:start",
      "telemetry:stop",
      "logs:read",
      "logs:download"
    ]
  }
}
```

Opcao B, claims dentro do JWT:

```json
{
  "sub": "joao",
  "role": "admin",
  "permissions": [
    "telemetry:start",
    "telemetry:stop",
    "logs:read",
    "logs:download"
  ],
  "exp": 1780000000
}
```

Recomendacao: usar as duas abordagens quando possivel. A resposta explicita
facilita a UI; o JWT continua sendo a fonte de verdade para autorizacao no
backend.

### 3.3 Navegacao

Adicionar uma terceira aba em `App.jsx`:

```js
const TABS = [
  { id: 'analise', label: 'Analise' },
  { id: 'cockpit', label: 'Cockpit' },
  { id: 'downloads', label: 'Downloads' },
]
```

Renderizacao esperada:

- `analise`: fluxo atual de graficos e historico.
- `cockpit`: fluxo atual do cockpit.
- `downloads`: novo componente `DownloadsPage`.

### 3.4 Controle de coleta

Alterar `TopBar` para receber permissao:

```jsx
<TopBar
  canControlTelemetry={canControlTelemetry()}
  ...
/>
```

Comportamento:

- `admin`: mostra controle de coleta normalmente.
- `member`: mostra somente status da coleta/conexao, sem botao de iniciar ou
  encerrar.

Opcional para uma segunda etapa:

- Mostrar tooltip ou texto curto no hover: `Controle restrito a administradores`.
- Nao colocar esse texto como explicacao permanente na UI principal.

### 3.5 Modulos novos

Criar:

```text
src/components/Downloads/DownloadsPage.jsx
src/components/Downloads/DownloadsPage.css
src/components/Downloads/DownloadFilters.jsx
src/components/Downloads/DownloadLogTable.jsx
src/components/Downloads/DownloadStatusBadge.jsx
src/services/logDownloads.js
src/utils/permissions.js
```

Responsabilidades:

- `DownloadsPage.jsx`: orquestra filtros, carregamento e download.
- `DownloadFilters.jsx`: filtros de busca/periodo/tipo/status.
- `DownloadLogTable.jsx`: lista os logs e botoes de download.
- `DownloadStatusBadge.jsx`: padroniza estados como `ready`, `processing`,
  `failed` e `expired`.
- `logDownloads.js`: encapsula `fetch` dos endpoints de logs.
- `permissions.js`: centraliza nomes de permissoes e helpers `hasPermission`.

## 4. Contrato backend proposto

### 4.1 Listar logs

Endpoint:

```http
GET /telemetry/logs
Authorization: Bearer <token>
```

Query params opcionais:

```text
from=<unix_seconds_or_iso>
to=<unix_seconds_or_iso>
type=<raw|csv|json|motec|other>
status=<ready|processing|failed|expired>
q=<texto>
limit=50
cursor=<cursor>
```

Resposta:

```json
{
  "ok": true,
  "items": [
    {
      "id": "log_2026_05_26_001",
      "name": "Treino 1 - stint 3",
      "created_at": "2026-05-26T18:12:00Z",
      "started_at": "2026-05-26T18:01:22Z",
      "ended_at": "2026-05-26T18:10:55Z",
      "duration_seconds": 573,
      "format": "csv",
      "content_type": "text/csv",
      "size_bytes": 1843200,
      "status": "ready",
      "download_url": null,
      "metadata": {
        "vehicle": "EV",
        "driver": "Piloto",
        "source": "telemetry-server"
      }
    }
  ],
  "next_cursor": null
}
```

Observacoes:

- `format` e `content_type` sao metadados; o frontend nao deve presumir
  extensao fixa.
- `download_url` pode ser `null` se o download exigir rota autenticada.
- `metadata` e livre para o backend evoluir sem quebrar a UI.

### 4.2 Baixar log autenticado

Endpoint:

```http
GET /telemetry/logs/:id/download
Authorization: Bearer <token>
```

Resposta:

- corpo binario ou texto do arquivo;
- `Content-Type` real do arquivo;
- `Content-Disposition: attachment; filename="nome.ext"`.

O frontend deve usar `Blob` e criar um link temporario para download quando
precisar enviar headers. Se `download_url` ja vier pronto, pode abrir a URL
diretamente.

### 4.3 Criacao do log ao encerrar coleta

O frontend envia os limites da coleta por `telemetryCollection.js` depois que o
backend aceita o encerramento administrativo e o worker local retorna os bounds.

Endpoint recomendado:

```http
POST /telemetry/log-session-bounds
Authorization: Bearer <token>
Content-Type: application/json
```

Body:

```json
{
  "log_start_unix": 1780000000.12,
  "log_stop_unix": 1780000573.44
}
```

Resposta:

```json
{
  "ok": true,
  "id": "log_2026_05_26_001",
  "status": "processing"
}
```

Esse endpoint deve ser permitido apenas para `admin`, porque ele faz parte do
fluxo de encerramento da coleta.

### 4.4 Start/stop no backend

O frontend chama comandos administrativos HTTP antes de alterar o estado local
da coleta. O backend deve tratar esses endpoints como o contrato oficial de
autorizacao.

Endpoints definidos pelo frontend:

```http
POST /telemetry/collection/start
POST /telemetry/collection/stop
Authorization: Bearer <token>
Content-Type: application/json
```

Semantica:

- `admin`: autorizado.
- `member`: `403 Forbidden`.
- Backend registra auditoria com usuario, horario e origem.

Body de start:

```json
{
  "requested_at": "2026-05-26T12:00:00.000Z"
}
```

Body de stop:

```json
{
  "requested_at": "2026-05-26T12:10:00.000Z",
  "log_start_unix": null,
  "log_stop_unix": null
}
```

No fluxo atual, `stop` e chamado antes de desligar a coleta local; por isso os
bounds seguem como `null` nesse endpoint e sao enviados em seguida para
`POST /telemetry/log-session-bounds`.

## 5. UX da aba Downloads

### 5.1 Layout

Primeira versao:

- cabecalho compacto com titulo `Downloads`;
- botao de atualizar;
- filtros em uma barra unica;
- tabela/lista de logs;
- acoes por linha.

Colunas sugeridas:

- Nome
- Inicio
- Fim
- Duracao
- Formato
- Tamanho
- Status
- Acao

Estados:

- carregando: skeleton ou mensagem curta;
- vazio: mensagem operacional indicando que nao ha logs para os filtros;
- erro: mensagem com botao de tentar novamente;
- `processing`: linha visivel, download desabilitado;
- `failed` ou `expired`: linha visivel com status claro e sem download.

### 5.2 Download

Fluxo:

1. usuario clica em baixar;
2. UI marca somente aquela linha como `downloading`;
3. `logDownloads.js` chama rota autenticada ou usa `download_url`;
4. browser inicia download com nome vindo do backend;
5. em erro, a linha mostra falha temporaria e permite tentar de novo.

## 6. Seguranca e autorizacao

Regras obrigatorias no backend:

1. validar JWT em todas as rotas de logs;
2. exigir `logs:read` para listar logs;
3. exigir `logs:download` para baixar logs;
4. exigir `telemetry:start` para iniciar coleta;
5. exigir `telemetry:stop` para encerrar coleta;
6. retornar `403` quando autenticado mas sem permissao;
7. nao confiar em permissao enviada pelo frontend;
8. registrar auditoria para start/stop e download, se possivel.

Regras no frontend:

1. esconder controles administrativos para `member`;
2. desabilitar acoes quando permissao estiver ausente;
3. tratar `401` limpando sessao e voltando ao login;
4. tratar `403` mostrando erro de permissao;
5. manter o token fora de logs de console.

## 7. Plano de execucao

Status atualizado: o frontend ja cobre sessao com perfil, guards de
`admin/member`, aba `Downloads`, services HTTP para logs, start/stop
administrativo, persistencia de bounds e proxy de desenvolvimento para
`/telemetry`. O backend deve se adequar aos contratos definidos aqui e nas
pendencias documentadas em
[backend-downloads-and-roles-pending.md](/Users/joaogabriel/Documents/TelemetriaV2.0/telemetry-server/static/docs/backend-downloads-and-roles-pending.md).

### Fase 1: Modelo de sessao e permissoes

1. Concluido: criar `src/utils/permissions.js`.
2. Concluido: atualizar `auth.js` para extrair `role` e `permissions` da resposta de login
   ou do JWT.
3. Concluido: atualizar `App.jsx` para guardar `role` e `permissions` na sessao.
4. Concluido: garantir fallback temporario para tokens antigos:
   - em desenvolvimento, assumir `admin` quando nao houver role;
   - em producao, preferir role `member` ou bloquear operacoes sensiveis.
5. Concluido no backend: `POST /login` retorna `user.role` e
   `user.permissions`, e o JWT tambem carrega essas claims. Ver
   [backend-access-roles.md](/Users/joaogabriel/Documents/TelemetriaV2.0/telemetry-server/static/docs/backend-access-roles.md).

### Fase 2: Controle administrativo de coleta

1. Concluido: adicionar `canControlTelemetry` e permissoes separadas em `App.jsx`.
2. Concluido: passar a permissao para `TopBar`.
3. Concluido: esconder o botao de iniciar/encerrar para `member`.
4. Concluido: proteger handlers `handleStartTelemetry` e `handleStopTelemetry` com guards
   de permissao.
5. Concluido no frontend: criar service para os comandos
   `POST /telemetry/collection/start` e `POST /telemetry/collection/stop`.
6. Concluido no frontend: sincronizar o estado local da coleta com a resposta
   real do backend.
7. Pendente de validacao integrada: testar `401`, `403` e `409` contra backend
   real.
8. Concluido no backend: `POST /telemetry/collection/start`,
   `POST /telemetry/collection/stop` e `POST /telemetry/log-session-bounds`
   exigem permissoes administrativas.

### Fase 3: Aba Downloads

1. Concluido: adicionar aba `downloads` ao `TABS`.
2. Concluido: criar `DownloadsPage` e CSS.
3. Concluido: criar `logDownloads.js` com:
   - `listTelemetryLogs(filters, token)`;
   - `downloadTelemetryLog(log, token)`.
4. Concluido: implementar tabela/lista com estados de carregamento, erro e vazio.
5. Concluido: implementar download por `Blob` para rota autenticada.
6. Concluido: respeitar `download_url` quando o backend enviar URL assinada.
7. Pendente apos backend: validar a tabela com payload real e ajustar somente
   detalhes de campos se o contrato final mudar.

### Fase 4: Integracao com backend

1. Documentado para backend: definir contrato final dos endpoints.
2. Concluido no frontend: atualizar `vite.config.js` com proxy `/telemetry`.
3. Concluido no frontend: enviar bounds reais para `/telemetry/log-session-bounds`.
4. Concluido no backend: implementar start/stop administrativo e
   `/telemetry/log-session-bounds` para persistir timestamps da coleta. Ver
   [backend-collection-timestamps.md](/Users/joaogabriel/Documents/TelemetriaV2.0/telemetry-server/static/docs/backend-collection-timestamps.md).
5. Pendente no frontend apos backend: validar com logs reais de formatos
   diferentes.
6. Pendente no frontend apos backend: consolidar tratamento global de `401` e
   `403` nos services autenticados.

### Fase 5: Testes e validacao

1. Testar login como `admin`:
   - ve botao de coleta;
   - inicia coleta;
   - encerra coleta;
   - visualiza e baixa logs.
2. Testar login como `member`:
   - nao ve controle acionavel de coleta;
   - acessa analise, cockpit e downloads;
   - baixa logs permitidos.
3. Testar `403` forjado:
   - chamar download sem permissao;
   - chamar start/stop sem permissao.
4. Testar lista vazia, erro de rede e download de arquivo grande.
5. Rodar build do frontend.

## 8. Riscos e decisoes pendentes

### Riscos

- Se o backend nao aplicar `403` nos endpoints administrativos, um usuario
  tecnico ainda pode tentar contornar a UI.
- Logs grandes podem consumir memoria se o download autenticado usar `Blob`.
  Para arquivos muito grandes, preferir URL assinada/temporaria servida pelo
  backend ou storage.
- Se o backend nao enviar `Content-Disposition`, o frontend precisara inferir
  nome e extensao por metadados.
- Tokens antigos sem `role` podem criar comportamento inconsistente se nao
  houver fallback definido.

### Decisoes pendentes

1. O backend vai devolver `role/permissions` no corpo do login, no JWT ou ambos?
2. Os logs serao baixados por URL assinada ou por endpoint autenticado?
3. Quais formatos iniciais precisam aparecer no filtro?
4. O backend aceitara o contrato HTTP de start/stop definido pelo frontend?
5. O membro pode ver todos os logs ou apenas logs de determinado escopo?
6. Havera auditoria de downloads?

## 9. Checklist de implementacao

- [x] Documentar plano de arquitetura da feature.
- [x] Documentar pendencias do backend em arquivo dedicado.
- [x] Criar helper de permissoes no frontend.
- [x] Atualizar sessao em `App.jsx`.
- [x] Bloquear start/stop para `member` na UI e nos handlers.
- [x] Adicionar aba `Downloads`.
- [x] Criar componentes da area de downloads.
- [x] Criar service HTTP para listar e baixar logs.
- [x] Implementar estados de loading/empty/error/downloading.
- [x] Respeitar download autenticado por `Blob`.
- [x] Respeitar `download_url` quando backend enviar URL pronta.
- [x] Atualizar proxy de desenvolvimento para `/telemetry`.
- [x] Backend: definir contrato final de login com perfil/permissoes.
- [x] Frontend: criar service de start/stop administrativo.
- [x] Frontend: sincronizar start/stop local com resposta real do backend.
- [x] Frontend: substituir mock de persistencia de bounds por chamada real.
- [x] Backend: implementar autorizacao real para start/stop.
- [ ] Backend: implementar listagem e download de logs.
- [x] Backend: implementar persistencia de bounds da coleta.
- [ ] Frontend: consolidar tratamento de `401`, `403` e `409` nos services.
- [ ] Frontend: validar payload real de logs e ajustar campos se necessario.
- [ ] Validar backend com `401`, `403`, arquivo pequeno e arquivo grande.
- [ ] Atualizar documentacao principal se a feature entrar em producao.


# Plano de migracao Rust: CSV -> DBC (telemetria em alta velocidade)

## Objetivo

Migrar a configuracao CAN de `csv_data/*.csv` para um modelo padronizado em `.dbc`, sem perder desempenho de telemetria e sem acoplamento a um unico arquivo (ex.: BMS).

O alvo e suportar varios DBCs em paralelo (BMS, VCU, IMU, etc.) com fonte unica de verdade e processo de auditoria de cobertura.

## Escopo

1. manter pipeline atual de ingestao em tempo real:
- ler frame bruto (`can_id`, `timestamp`, `raw_data`)
- buscar sinais por `can_id`
- decodificar
- persistir e publicar no WS

2. trocar apenas a fonte de configuracao CAN:
- de CSV manual/legado
- para DBC padronizado e versionado

3. preparar base para multiplos DBCs, nao apenas BMS.

## Estado atual (codigo)

- Loader atual: `src/decoder.rs` (`load_can_mappings` via CSV).
- Runtime atual: `src/main.rs` (`handle_client` usa `decoder_map.get(&can_id)` + `decode_signal`).
- Decoder atual assume extracao estilo Intel/LSB e inferencia de signed por texto (`value_type`).

## Requisito critico: performance

A migracao para DBC **nao pode** introduzir parsing por frame.

Regra de ouro:

- parse de DBC acontece **somente no boot** (ou em hot-reload controlado);
- runtime usa estruturas precompiladas (`HashMap<u32, MessageConfig>`) com lookup O(1);
- em cada frame, o custo deve ser equivalente ao atual: `get(can_id)` + loop de sinais + decode.

### Diretrizes de desempenho

1. **Zero regex no hot path**: parser DBC pode usar regex no boot, nunca durante `handle_client`.
2. **Sem alocacao desnecessaria por frame**:
- evitar `String` nova na decodificacao;
- sinal deve reaproveitar metadado ja carregado.
3. **Pre-validacao no boot**:
- descartar sinais invalidos no parse;
- evitar checks caros em runtime.
4. **Benchmarks**:
- adicionar benchmark simples de decode (N frames x M sinais) para comparar CSV vs DBC.

## Padronizacao DBC (multi-arquivo)

Em vez de um unico arquivo fixo, usar diretorio de DBCs, por exemplo:

- `./dbc_data/*.dbc`

Fluxo:

1. ler todos os `.dbc` do diretorio;
2. montar `DecoderMap` unificado por `can_id`;
3. detectar conflitos de definicao;
4. falhar no boot se houver conflito critico.

### Regra de conflito (obrigatoria)

Se o mesmo `can_id` aparecer em mais de um DBC com definicoes divergentes de sinal (`start_bit/len/byte_order/signed/factor/offset`), marcar como erro de configuracao.

Isso evita decodificacao ambigua em pista.

## Mudancas necessarias na decodificacao

Sim, precisa mudar para suportar DBC corretamente.

1. `byte_order`:
- suportar Intel (`@1`) e Motorola (`@0`).

2. signed:
- usar `+/-` do DBC (`is_signed`) e nao inferir por texto.

3. estrutura de mensagem:
- guardar `dlc` para validacao logica (mesmo que frame de transporte siga com 8 bytes).

## Modelo sugerido (Rust)

```rust
pub enum ByteOrder {
    Intel,
    Motorola,
}

pub struct SignalConfig {
    pub signal_name: String,
    pub start_bit: usize,
    pub length: usize,
    pub factor: f64,
    pub offset: f64,
    pub unit: String,
    pub is_signed: bool,
    pub byte_order: ByteOrder,
}

pub struct MessageConfig {
    pub can_id: u32,
    pub dlc: usize,
    pub signals: Vec<SignalConfig>,
    pub source_file: String,
    pub message_name: String,
}

pub type DecoderMap = HashMap<u32, MessageConfig>;
```

## Loader DBC

Adicionar:

- `load_can_mappings_from_dbc_dir(path: &Path) -> Result<DecoderMap, Error>`

Capacidades:

1. parse de `BO_` e `SG_`;
2. merge de multiplos arquivos;
3. deteccao de conflitos;
4. relatorio final de carga:
- total de arquivos
- total de mensagens
- total de sinais
- conflitos encontrados

## Compatibilidade e rollout seguro

Adicionar `CAN_MAP_SOURCE`:

- `dbc` (novo padrao)
- `csv` (fallback)

E opcional:

- `CAN_DBC_DIR=./dbc_data`

Rollout:

1. ativar `dbc` em homologacao;
2. rodar comparacao paralela contra `csv`;
3. ativar em producao;
4. remover csv quando estabilizar.

## Missao adicional: varredura de cobertura CSV x DBC

Como voce descreveu, precisamos mapear o status de migracao por sistema (BMS e outros).

### Objetivo da varredura

Responder com evidencia:

1. quais CAN IDs existem no legado CSV;
2. quais CAN IDs ja existem em DBC;
3. quais faltam migrar para DBC;
4. quais existem em DBC mas nao no CSV;
5. quais IDs batem, mas com divergencia de sinais/escala/unidade.

### Entregavel da varredura

Gerar relatorio versionado (ex.: `reports/can-coverage-report.md`) com:

1. resumo geral por data;
2. tabela por arquivo/sistema;
3. lista de gaps priorizados;
4. lista de conflitos de definicao;
5. status por item: `migrado`, `parcial`, `nao iniciado`.

### Metodologia sugerida

1. extrair inventario CSV:
- set de `can_id`
- sinais por `can_id`

2. extrair inventario DBC (todos os arquivos):
- set de `can_id`
- sinais por `can_id`
- metadados de decode

3. comparar em 3 niveis:
- nivel 1: existencia do `can_id`
- nivel 2: existencia de sinal por nome
- nivel 3: igualdade de parametros (`start_bit`, `len`, `byte_order`, `signed`, `factor`, `offset`, `unit`)

4. classificar diferencas:
- `missing_in_dbc`
- `missing_in_csv`
- `param_mismatch`
- `name_mismatch`

## Criticos de qualidade antes de fechar migracao

1. sem conflito de `can_id` entre DBCs ativos;
2. sinais criticos de operacao presentes (BMS/VCU/seguranca);
3. latencia e throughput sem regressao perceptivel;
4. regressao de valor aprovada em amostras reais.

## Sequencia recomendada

1. implementar loader DBC multi-arquivo com validacoes;
2. ajustar decode para Intel/Motorola + signed por DBC;
3. adicionar fallback por `CAN_MAP_SOURCE`;
4. implementar ferramenta de varredura CSV x DBC;
5. publicar primeiro relatorio de cobertura;
6. migrar por blocos (BMS, depois demais sistemas);
7. virar default para DBC e descontinuar CSV legado.

## Checklist

- [ ] parser DBC multi-arquivo funcionando
- [ ] conflitos de `can_id` detectados no boot
- [ ] decode Intel e Motorola testado
- [ ] signed baseado em DBC implementado
- [ ] benchmark sem regressao relevante
- [ ] varredura CSV x DBC implementada
- [ ] relatorio de cobertura atualizado
- [ ] fallback CSV disponivel para rollback rapido

## DBCs recebidos (status atual)

Arquivos ja recebidos para padronizacao DBC:

- [x] `/Users/joaogabriel/Downloads/EMUS-G1-BMS-DBC-v1_0_2.dbc` (BMS)
- [x] `/Users/joaogabriel/Downloads/Inversor_Private.dbc`
- [x] `/Users/joaogabriel/Downloads/Inversor_Public.dbc`
- [x] `/Users/joaogabriel/Downloads/VCU_GERAL.dbc`

Proximo passo dessa trilha:

1. consolidar esses arquivos em `./dbc_data/` no backend;
2. rodar varredura CSV x DBC com os quatro arquivos;
3. publicar primeiro `can-coverage-report.md` com gaps por sistema.

## Execução inicial da varredura (2026-05-24)

Relatórios gerados:

- `/Users/joaogabriel/Documents/TelemetriaV2.0/telemetry-server/reports/can-coverage-report.md`
- `/Users/joaogabriel/Documents/TelemetriaV2.0/telemetry-server/reports/can-coverage-report.json`

Resumo inicial:

- CSV files: `7`
- DBC files: `4`
- CAN IDs no CSV: `38`
- CAN IDs no DBC: `340`
- Interseção: `18`
- Faltando no DBC (vs CSV): `20`
- Só no DBC: `322`

Leitura desse resultado:

1. A padronização DBC já cobre uma área muito maior que o legado CSV.
2. Ainda há lacunas de migração para IDs do CSV que não apareceram nos DBCs atuais.
3. Parte relevante das diferenças na interseção é de nomenclatura (`_` vs espaço/sufixo), exigindo regra de normalização antes de classificar como incompatibilidade real de decode.


