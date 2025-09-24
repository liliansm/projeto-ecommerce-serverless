# 🛒 Backend Serverless para Processamento de Pedidos

Este projeto é um **protótipo acadêmico** de um backend **serverless** para um sistema de e-commerce.  
O objetivo é processar pedidos, realizar cobranças simuladas e enviar notificações, sem necessidade de gerenciar infraestrutura.

---

## 🚀 Tecnologias Utilizadas
- **AWS Lambda** (modelo de execução serverless)  
- **API Gateway** (exposição da função via HTTP)  
- **Python 3.x**  

---

## 📌 Funcionalidades
- **Processamento de pedidos** → Simula o salvamento do pedido.  
- **Cobrança com cartão de crédito** → Integração simulada com um gateway de pagamento.  
- **Envio de notificações** → Simulação de envio de notificação para o usuário.  
- **Resposta HTTP estruturada** → Retorna mensagens em JSON, com suporte a CORS.  

---

## 🧩 Fluxo de Execução
1. O **API Gateway** recebe uma requisição HTTP.  
2. O **Lambda Handler** é acionado e:  
   - Valida os dados recebidos.  
   - Processa o pedido.  
   - Cobra o cartão de crédito (simulação).  
   - Envia a notificação (simulação).  
3. O resultado é retornado em formato JSON.  

---

## 💡 Justificativa de Escolhas

### 🔹 Escalabilidade
A solução serverless permite que o sistema escale automaticamente de acordo com a quantidade de pedidos.  
Se houver muitos acessos simultâneos, novas instâncias da função Lambda são criadas sob demanda, sem precisar configurar servidores manualmente.  

### 🔹 Custo
O modelo de cobrança do AWS Lambda é **pay-per-use**.  
Isso significa que a startup de e-commerce só paga pelo tempo de execução da função e não precisa manter servidores ativos 24/7, reduzindo custos operacionais.  

### 🔹 Facilidade de Manutenção
Por ser baseado em **Functions as a Service (FaaS)**:  
- Cada responsabilidade (pedido, pagamento, notificação) pode ser isolada em funções independentes.  
- O código é simples e modular, facilitando futuras alterações.  
- Não é necessário gerenciar infraestrutura, apenas o código da lógica de negócio.  

---

## 👩‍💻 Integrantes do Grupo
- Lilian Souza  
- Luana Marques  
- Alisson Gabriel  

---

## 📜 Observações
Este projeto é um **protótipo acadêmico** e utiliza simulações em vez de integrações reais com banco de dados e gateways de pagamento.  
Em um ambiente de produção, recomenda-se:  
- Persistência em **DynamoDB** ou outro banco serverless.  
- Integração real com provedores de pagamento.  
- Filas de mensagens (ex.: SQS) para melhorar a resiliência.  

---
✨ Desenvolvido como parte da disciplina de **Sistemas Distríbuidos** no IFPE.
