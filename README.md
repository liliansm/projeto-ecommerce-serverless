# Protótipo de E-commerce Serverless

Este é um projeto para a disciplina de sistemas distríbuidos, que demonstra um backend serverless para processamento de pedidos construído com tecnologias da AWS.

## Tecnologias Utilizadas
* **Backend:** AWS Lambda (Python 3.9), Amazon API Gateway
* **Frontend:** HTML5, CSS3, JavaScript
* **Controle de Versão:** Git & GitHub

## Como Executar e Testar

1.  **Backend:** O backend está hospedado na AWS e pode ser acessado através do seguinte endpoint:
    * `https://jdjuebj1l7.execute-api.us-east-1.amazonaws.com/default/processar-pedido-ecommerce`

2.  **Frontend:** Para testar a aplicação, baixe o arquivo `index.html` deste repositório, abra-o em qualquer navegador de internet e clique no botão "Enviar Pedido". A interface irá interagir diretamente com o endpoint da API.

## Alunos
* Lilian Souza, Luana Marques, Alisson Gabriel

1. Problema

Uma startup de e-commerce deseja desenvolver um backend serverless para processar pedidos, realizar cobranças com cartão de crédito e enviar notificações aos usuários.
O sistema deve ser escalável, com custo reduzido e sem necessidade de gerenciar infraestrutura.


---

2. Objetivo

Projetar e implementar uma solução serverless para processar pedidos de forma confiável, aplicando os princípios de Function as a Service (FaaS).

A solução precisa contemplar:

Processamento de pedidos

Integração com gateway de pagamento

Envio de notificações

Escalabilidade, baixo custo e facilidade de manutenção



---

3. Arquitetura Serverless

Fluxo proposto:

1. O cliente envia um pedido (JSON) via HTTP.


2. O Amazon API Gateway expõe o endpoint REST.


3. A AWS Lambda (Ingress) valida e registra o pedido no DynamoDB e publica um evento em fila/event-bus.


4. A Lambda de Pagamento processa o evento, integra-se ao gateway de pagamento e atualiza o status no DynamoDB.


5. A Lambda de Notificação envia mensagens via SNS/SES (e-mail, SMS, push) para o usuário.


6. CloudWatch/X-Ray fazem monitoramento e logs.


7. Secrets Manager guarda credenciais do gateway de pagamento.

Diagrama (representação simplificada):

Cliente → API Gateway → Lambda (Ingress) → DynamoDB
                                  │
                                  ▼
                      EventBridge / SQS
                                  │
                   ┌──────────────┴──────────────┐
                   ▼                             ▼
          Lambda (Pagamento)             Lambda (Notificação)
                   │                             │
                   ▼                             ▼
              Gateway Externo               SNS / SES (E-mail/SMS)


4. Justificativa das Escolhas

AWS Lambda (FaaS): escala automaticamente com a demanda, cobrando apenas pelo uso.

API Gateway: expõe endpoints REST sem necessidade de servidores dedicados.

DynamoDB: banco NoSQL serverless, altamente escalável e sem administração.

SQS/EventBridge: garante desacoplamento entre pedidos, pagamentos e notificações.

SNS/SES: envio de notificações simples e escalável.

CloudWatch/X-Ray: logs, métricas e rastreamento para facilitar manutenção.

Secrets Manager: armazena segredos e credenciais de forma segura.


Essa arquitetura garante escalabilidade, baixo custo operacional e facilidade de manutenção.

