import json

# =====================================================
# Função: Processar Pedido
# =====================================================
def processar_pedido(dados):
    """
    Simula salvar o pedido em um banco de dados.
    """
    print("Salvando pedido no banco de dados...")
    return {"status": "ok", "pedido_id": "PED-12345"}


# =====================================================
# Função: Cobrar Cartão de Crédito
# =====================================================
def cobrar_cartao(cartao, valor):
    """
    Simula integração com um gateway de pagamento.
    """
    print(f"Cobrando cartão {cartao} no valor de R${valor}...")
    return {"status": "pago", "valor": valor}


# =====================================================
# Função: Enviar Notificação
# =====================================================
def enviar_notificacao(pedido_id):
    """
    Simula envio de notificação para o usuário.
    """
    print(f"Enviando notificação do pedido {pedido_id}...")
    return {"status": "notificação enviada"}


# =====================================================
# Função Principal (Lambda Handler)
# =====================================================
def lambda_handler(event, context):
    """
    Função Lambda chamada pelo API Gateway.
    Processa o pedido, realiza a cobrança e envia notificação.
    """
    print("Iniciando processamento do pedido...")

    try:
        # O corpo chega como string → converter para dict
        dados_pedido = json.loads(event['body'])

        # Extrair dados
        produto_id = dados_pedido.get('produto_id')
        quantidade = dados_pedido.get('quantidade')
        cartao_credito = dados_pedido.get('cartao_credito')

        # Validação simples
        if not produto_id or not quantidade or not cartao_credito:
            return {
                'statusCode': 400,
                'body': json.dumps({'mensagem': 'Dados do pedido incompletos.'})
            }

        # Passo 1: Processar pedido
        pedido = processar_pedido(dados_pedido)

        # Passo 2: Cobrar cartão
        pagamento = cobrar_cartao(cartao_credito, quantidade * 100)  # simulação: 100 por unidade

        # Passo 3: Enviar notificação
        notificacao = enviar_notificacao(pedido["pedido_id"])

        # Retorno final
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Methods': 'OPTIONS,POST'
            },
            'body': json.dumps({
                'mensagem': f"Pedido {pedido['pedido_id']} processado com sucesso!",
                'pedido': pedido,
                'pagamento': pagamento,
                'notificacao': notificacao
            })
        }

    except Exception as e:
        print(f"Erro inesperado: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps({'mensagem': 'Erro interno ao processar pedido.'})
        }
