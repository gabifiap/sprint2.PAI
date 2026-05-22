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

### 📝 DESCRIÇÃO DO SYSTEM PROMPT:

O processo de desenvolvimento do ChargeGrid Intelligence foi dividido em 5 etapas principais, cobrindo desde a análise do problema até a validação das respostas da IA.

 **Passo 1: Modelagem do Domínio** O projeto começou com o mapeamento das regras de negócio da Good-We e das dores operacionais (desperdício de energia, ociosidade de vagas e alto custo de suporte). Nesta etapa, determinou-se que um sistema rígido de árvore de decisões não seria eficiente, optando-se por uma Solução Baseada em Modelos de Linguagem (LLMs).

 **Passo 2: Estruturação do Dataset de Referência**
Para garantir que a IA respondesse corretamente e não inventasse informações, criamos um dataset de referência com perguntas e respostas fixas baseadas em dados simulados de telemetria e faturamento.

 **Passo 3: Prototipagem no Google Colab**
Usamos o Google Gemini para nos apoiar na escrita das primeiras versões das instruções e na formatação das regras. No Colab, validamos a lógica inicial em Python para garantir que o script conseguia capturar o perfil selecionado pelo usuário e concatenar a pergunta corretamente antes de enviar para um modelo.

 **Passo 4: Configuração e Governança do Modelo Local via Modelfile**
Com a lógica validada, migramos para o ambiente local utilizando o Ollama com o modelo Llama 3. Para customizar e blindar o modelo, criamos um arquivo de configuração chamado Modelfile: Ajuste: Definimos a temperatura em 0.2 para tornar as respostas precisas, reduzindo a margem para respostas "criativas" (alucinações).

 **Passo 5: Desenvolvimento da Interface Conversacional (Streamlit)**
Por fim, desenvolvemos o front-end utilizando o framework Streamlit em Python: Implementamos a janela de chat que envia a pergunta do usuário junto com o contexto do perfil para a API local do Ollama (ollama.chat).
