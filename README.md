#  GUIA GOODWE

###  INTEGRANTES:
* **Gabriela Batista Costa** - 573583
* **Anna Luiza Cavalhares** - 573330
* **Samara Carvalho** - 573666
* **Kethelyn Rocha** - 574016

---

### ⚠️ PROBLEMA ABORDADO: 

As estações de recarga atuais operam de forma "isolada" (sem inteligência nativa), o que gera problemas para a empresa:

 **Vagas Presas (Desperdício de Janela de Carga):** Quando um veículo atinge 100% da bateria e continua plugado, ele bloqueia a energia que poderia estar alimentando outro carro. Isso reduz a eficiência da estação e gera o desperdício de "potência ociosa" da infraestrutura disponível.

**Falta de Orquestração Dinâmica:** Sem um sistema inteligente para ler a capacidade da rede em tempo real, os carregadores operam de forma cega. Isso pode sobrecarregar a grade nos horários de pico (gerando multas e desperdício financeiro com tarifas mais altas) ou entregar menos potência do que o sistema suportaria nos horários de vale.

 **Alto Custo de Suporte:** Novos usuários sobrecarregam o atendimento humano com dúvidas repetitivas sobre onboarding, acompanhamento e formas de faturamento (Pix/Cartão).

---

###  COMO A IA PODE AJUDAR NISSO?

**--CHATBOT CRIADO PARA SUPORTE DE POSTOS COMERCIAIS.**

* **Para o Usuário:** Explica de forma firme e educativa a cobrança da taxa após os 15 minutos de tolerância, forçando a rotatividade das vagas.
* **Para o Técnico:** Traduz os relatórios de eficiência e ciclos em linguagem natural, permitindo que ele identifique rapidamente quais eletropostos precisam ser reiniciizados ou calibrados para evitar fuga de energia.
* **Orquestração de Demanda de Potência**
Para evitar que a rede elétrica local entre em colapso quando vários veículos carregam ao mesmo tempo, a solução central é:

Smart Charging (Recarga Inteligente): Um sistema de software que monitora a carga total disponível na edificação ou na rede.

Balanceamento de Carga (Load Balancing): Se a potência disponível for limitada, o sistema distribui a energia equitativamente entre os carregadores ativos ou prioriza veículos com baterias mais baixas, garantindo que o disjuntor geral não desarme.

Limite de carregamento: quado o veículo atinge 100% de carga automaticamente a entrega de energia é interrompida.
* **Pagamento:**
Modelos de Negócio Diversificados: Implementação de cobrança por kWh consumido, por tempo de permanência ou modelos de assinatura para frotas.

---

### 🛠️ TECNOLOGIAS ULTILIZADAS:

* **Google Gemini:** (IA de Apoio, design do modelfile)
* **Google Colab:** (Ambiente de Desenvolvimento, para criar, testar e rodar o código Python)
* **Ollama:** (Motor de Inferência Local, modelfile) Para executar o modelo de linguagem final diretamente na infraestrutura controlada pela empresa, garantindo autonomia.

---

### 📝 MELHORIAS DO SYSTEM PROMPT (SPRINT2):
# 🚀 Evolução Técnica: Sprint 1 para Sprint 2

* **Especialização do Conhecimento (Datasets):** A base de conhecimento do chatbot foi expandida com **quatro novos datasets estruturados**. Agora, o modelo é especializado em **diagnóstico de erros técnicos** (documentados no repositório como datasets2), **interpretação de estados de sinalização (LEDs)** em carregadores, **inteligência de carga**, **tarifação**, **fluxo comercial**, além de **requisitos elétricos, protocolos e hardware**. Essa segmentação eliminou respostas genéricas, permitindo que a IA ofereça diagnósticos precisos e alinhados aos manuais da GoodWe.

* **Ollama para Gemini API:** primeiramente, mudamos do processamento local via Ollama para a API **`gemini-2.5-flash`**, mas mantendo a mesma estrutura do código. A carga de processamento exigida pelos novos datasets tornava a execução local inviável, causando muita instabilidade na interface interativa. A solução em nuvem permitiu uma performance mais consistente e permitiu que a IA processe volumes maiores de datasets com um melhor desempenho.

* **Modernização da Interface (Frontend):** Desenvolvemos uma interface interativa baseada em **Streamlit**, rodando via VS Code e acessível diretamente pelo navegador. A mudança do Google Colab para o VScode foi fundamental para a fluidez do código, consdieramos a interface anterior limitada e o novo frontend oferece uma experiência mais natural e realista, permitindo a visualização clara das interações, melhor gestão do histórico da sessão e uma interação mais intuitiva com o usuário final.
* **Modernização da Interface (Frontend):** Desenvolvemos uma interface interativa baseada em **Streamlit**, rodando via VS Code e acessível diretamente pelo navegador. A mudança do Google Colab para o VScode foi fundamental para a fluidez do código, consideramos a interface anterior limitada e o novo frontend oferece uma experiência mais natural e realista, permitindo a visualização clara das interações, melhor gestão do histórico da sessão e uma interação mais intuitiva com o usuário final.

* **Segurança e Organização:** Implementamos o uso de **variáveis de ambiente (`.env`)** e o arquivo **`.gitignore`**, garantindo que as chaves de API permaneçam protegidas e não sejam expostas no repositório. 

* **Erros:** Adicionamos lógica de **tratamento de erros e reconexão automática**, garantindo que pequenas quedas na comunicação com a API não interrompam o atendimento ao usuário.

---

### 🧪 Validação do Modelo (Testes da Sprint 1)

Abaixo, documentamos os casos de teste estruturados na primeira fase do projeto, validados com o modelo atual após a implementação dos novos datasets e a migração para a API do Gemini.

| Caso | Pergunta Enviada | Resposta Obtida | Avaliação |
| :--- | :--- | :--- | :--- |
| **01** | Comércio com 5 carregadores GW7K: disjuntor geral não suporta. Como o ChargeGrid resolve sem trocar fiação? | "O ChargeGrid Intelligence resolve essa questão através do Controle Dinâmico de Carga (Dynamic Load Control). Este sistema monitora continuamente o consumo total de energia da sua edificação e ajusta ou pausa a velocidade de carregamento dos veículos conforme necessário." | **Adequada** |
| **02** | Se eu chegar com meu carro as 18 em um ponto e o sistema estiver em modo de prioridade solar, o que acontece com a velocidade da minha recarga? | "Neste modo, o sistema prioriza o uso da energia fotovoltaica (solar) disponível. Como às 18h a geração de energia solar é mínima ou inexistente, o carregamento será lento ou poderá ser pausado, pois o sistema aguardará a disponibilidade de energia solar para otimizar o custo." | **Adequada** |
| **03** | A IA consegue prever qual eletroposto estará mais lotado? | "Sim, o sistema ChargeGrid Intelligence utiliza a Inteligência Artificial para prever picos de consumo. Através da análise de sessões de recarga anteriores e padrões históricos, a IA consegue identificar períodos de maior demanda." | **Adequada** |
| **04** | O que o sistema faz se eu tentar carregar meu carro e o prédio já estiver usando muita energia? | "O sistema ChargeGrid Intelligence ativará o Controle Dinâmico de Carga (Dynamic Load Control). Ele ajustará ou pausará a velocidade de carregamento do seu veículo com base no consumo total da edificação, garantindo que a demanda contratada não seja excedida." | **Adequada** |
| **05** | Quais os benefícios de usar o modo de operação 2? | "O Modo de Operação 2, conhecido como 'Prioridade Solar', oferece o benefício de priorizar o uso da energia fotovoltaica (solar) gerada no local para a recarga dos veículos. Isso resulta em uma redução do consumo de energia da rede elétrica convencional." | **Adequada** |

#### 💡 Diagnóstico e Segurança
* **Emergências (Faíscas no conector):** "Desligue imediatamente o disjuntor do carregador para cortar o fornecimento de energia e evitar maiores riscos. Após isso, entre em contato com o suporte técnico da GoodWe."
* **Diagnóstico de Falhas (Luz vermelha):** "Acesse o aplicativo oficial SEMS Portal ou SolarGo em seu celular, localize o carregador e identifique o código de erro exato gerado pelo sistema. Com esse código, poderei fornecer a solução específica."*

 ---
## 🛠️ Instruções de Execução

### 📋 Dependências
Este projeto utiliza bibliotecas essenciais para a interface e a comunicação com a IA. Para instalar todas as dependências necessárias, execute o comando abaixo no terminal:

"python -m pip install streamlit google-genai python-dotenv"

em seguida, para rodar a interface no navegador: 

"python -m streamlit run sprint2/app.py"

## 📋 Variáveis de ambiente necessárias: 
GEMINI_API_KEY: Chave de autenticação gerada através do Google AI Studio. Ela permite que o backend se conecte aos modelos de inteligência artificial da Google para processar e responder às mensagens dos usuários.
