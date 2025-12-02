# blockchain_alimentos_seguro_8blocos_corrigido.py

import hashlib
import json
from datetime import datetime
from rich.console import Console
from rich.table import Table
from rich import box
from rich.panel import Panel

console = Console()

class Transacao:
    def __init__(self, id_tx, dados, hash_anterior=""):
        self.id = id_tx
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.dados = dados  # dict com responsavel, evento, local, temp
        self.hash_anterior = hash_anterior
        self.hash = self.calcular_hash()

    def calcular_hash(self):
        dados_str = json.dumps({
            "id": self.id,
            "timestamp": self.timestamp,
            "dados": self.dados,
            "hash_anterior": self.hash_anterior
        }, sort_keys=True, ensure_ascii=False)
        return hashlib.sha256(dados_str.encode()).hexdigest()

class Bloco:
    def __init__(self, index, transacoes, hash_anterior=""):
        self.index = index
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.transacoes = transacoes
        self.hash_anterior = hash_anterior
        self.merkle_root = self.calcular_merkle_root()
        self.hash = self.calcular_hash()

    def calcular_merkle_root(self):
        hashes = [tx.hash for tx in self.transacoes]
        while len(hashes) > 1:
            if len(hashes) % 2:
                hashes.append(hashes[-1])
            nova = []
            for i in range(0, len(hashes), 2):
                nova.append(hashlib.sha256((hashes[i] + hashes[i+1]).encode()).hexdigest())
            hashes = nova
        return hashes[0] if hashes else "0"*64

    def calcular_hash(self):
        dados = {
            "index": self.index,
            "timestamp": self.timestamp,
            "merkle_root": self.merkle_root,
            "hash_anterior": self.hash_anterior
        }
        return hashlib.sha256(json.dumps(dados, sort_keys=True).encode()).hexdigest()

class BlockchainAlimentos:
    def __init__(self):
        self.cadeia = [self.criar_genesis()]

    def criar_genesis(self):
        return Bloco(0, [], "0"*64)

    def fraudar_evento(self, num_bloco, num_tx, novo_evento):
        if num_bloco <= 0 or num_bloco >= len(self.cadeia):
            console.print("[bold red]Bloco inválido para fraude.[/]")
            return

        bloco = self.cadeia[num_bloco]

        if num_tx < 1 or num_tx > len(bloco.transacoes):
            console.print("[bold red]Transação inválida.[/]")
            return

        tx_index = num_tx - 1
        tx = bloco.transacoes[tx_index]

        console.print(f"\n>>> [bold red]SIMULANDO ALTERAÇÃO NO BLOCO {num_bloco}, TX {num_tx}[/]")
        console.print(f"Evento original: [dim]{tx.dados['evento']}[/]")

        tx.dados["evento"] = novo_evento
        tx.hash = tx.calcular_hash()

        bloco.merkle_root = bloco.calcular_merkle_root()
        bloco.hash = bloco.calcular_hash()

        console.print("[bold red]Evento da transação alterado e hashes recalculados no bloco.[/]\n")

    def adicionar_bloco_legitimo(self, transacoes_novas):
        ultimo = self.cadeia[-1]
        txs_encadeadas = []
        hash_ant = ""
        # Correção na lógica de numeração dos IDs das transações
        base_id = (len(self.cadeia) - 1) * 10 
        for i, dados in enumerate(transacoes_novas):
            tx = Transacao(base_id + i + 1, dados, hash_ant if txs_encadeadas else "")
            hash_ant = tx.hash
            txs_encadeadas.append(tx)

        if len(txs_encadeadas) > 0:
             novo_bloco = Bloco(len(self.cadeia), txs_encadeadas, ultimo.hash)
             self.cadeia.append(novo_bloco)
    
    def verificar(self):
        for i in range(1, len(self.cadeia)):
            bloco = self.cadeia[i]
            anterior = self.cadeia[i-1]

            # 1. Checa a integridade do bloco atual em relação ao anterior
            if bloco.hash_anterior != anterior.hash:
                return i, "link_quebrado"

            # 2. Recalcula o hash do bloco para verificar se ele mesmo está íntegro
            if bloco.hash != bloco.calcular_hash():
                return i, "hash_bloco_invalido"

            # 3. Recalcula a Merkle Root para verificar se as transações internas foram adulteradas
            if bloco.merkle_root != bloco.calcular_merkle_root():
                 return i, "merkle_root_invalida"
            
            # 4. Checa o encadeamento individual das transações dentro do bloco
            for j, tx in enumerate(bloco.transacoes):
                 if tx.hash != tx.calcular_hash():
                     return i, f"hash_transacao_{j+1}_invalido"
                 # O encadeamento de transações é verificado apenas a partir da segunda transação
                 if j > 0 and tx.hash_anterior != bloco.transacoes[j-1].hash:
                      return i, f"link_transacao_{j}_quebrado"
                 # No primeiro item, se o hash anterior estiver preenchido, é um problema.
                 elif j == 0 and tx.hash_anterior != "":
                      return i, f"link_primeira_transacao_{j+1}_quebrado"

        return -1, "integro"


    def verificarOLD(self):
        for i in range(1, len(self.cadeia)):
            bloco = self.cadeia[i]
            anterior = self.cadeia[i-1]

            if bloco.hash != bloco.calcular_hash():
                return i, "hash_bloco_invalido"

            if bloco.hash_anterior != anterior.hash:
                return i, "link_quebrado"

            if bloco.merkle_root != bloco.calcular_merkle_root():
                 return i, "merkle_root_invalida"
            
            for j, tx in enumerate(bloco.transacoes):
                 if tx.hash != tx.calcular_hash():
                     return i, f"hash_transacao_{j+1}_invalido"
                 if j > 0 and tx.hash_anterior != bloco.transacoes[j-1].hash:
                      return i, f"link_transacao_{j+1}_quebrado"
                 elif j == 0 and tx.hash_anterior != "":
                      pass # A primeira TX do bloco não tem hash anterior definido nesta implementação

        return -1, "integro"       

    def mostrar(self):
        ponto, motivo = self.verificar()
        console.print("\n" + "="*80 + "\n")

        for idx, bloco in enumerate(self.cadeia):
            if idx == 0:
                console.print(Panel("[dim]Bloco Gênesis[/]", style="dim"))
                continue

            cor = "green" if (ponto == -1 or idx < ponto) else "red"
            status = "ÍNTEGRO" if idx < ponto or ponto == -1 else "CORROMPIDO!"

            table = Table(title=f"[bold {cor}]BLOCO {bloco.index} | Status: {status}[/]", box=box.DOUBLE)
            table.add_column("ID Tx", style="cyan")
            table.add_column("Responsável", style="yellow")
            table.add_column("Evento", style="green")
            table.add_column("Local", style="blue")
            table.add_column("Temp", style="white")
            table.add_column("Hash Tx Atual", style="bold")

            for j, tx in enumerate(bloco.transacoes):
                cor_tx = "green" if (ponto == -1 or idx < ponto) else "red"
                table.add_row(
                    str(tx.id),
                    tx.dados["responsavel"],
                    tx.dados["evento"],
                    tx.dados["local"],
                    f"{tx.dados.get('temperatura','—')}{'°C' if tx.dados.get('temperatura') is not None else ''}",
                    f"[{cor_tx}]{tx.hash[:10]}...[/]",
                )
            console.print(table)
            console.print(f"[bold]Hash Anterior Bloco: {bloco.hash_anterior[:16]}...[/]")
            console.print(f"[bold]Merkle Root: {bloco.merkle_root[:16]}...[/]")
            console.print(f"[bold]Hash do Bloco: {bloco.hash[:16]}... \n")

        if ponto != -1:
            console.print(Panel(
                f"[bold red]VIOLAÇÃO DE INTEGRIDADE DETECTADA NO BLOCO {ponto}!\n"
                f"Motivo: {motivo.replace('_', ' ').title()}\n\n"
                f"[white]→ Blocos a partir do {ponto} são considerados inválidos.[/]",
                title="IMUTABILIDADE", border_style="bright_red"
            ))
        else:
            console.print(Panel("[bold green]CADEIA 100% ÍNTEGRA![/]", border_style="green"))

def carregar_dados_iniciais():
    bc = BlockchainAlimentos()

    # Bloco 1 (Produção)
    bc.adicionar_bloco_legitimo([
        {"responsavel": "Produtor Fazenda A", "evento": "Colheita de tomates", "local": "Campo, MG", "temperatura": 25},
        {"responsavel": "Transportadora X", "evento": "Carregamento para distribuição", "local": "Galpão, MG", "temperatura": 10},
        {"responsavel": "Centro de Distribuição Y", "evento": "Recebimento e armazenamento", "local": "CD, SP", "temperatura": 8},
        {"responsavel": "Supermercado Z", "evento": "Exposição na gôndola", "local": "Loja, SP", "temperatura": 5},
        {"responsavel": "Cliente Ana", "evento": "Compra de 1kg de tomates", "local": "Supermercado Z, SP", "temperatura": None},
        {"responsavel": "App RastreiaFood", "evento": "Cliente escaneou QR Code", "local": "Online", "temperatura": None},
        {"responsavel": "Produtor Fazenda A", "evento": "Início do plantio da próxima safra", "local": "Campo, MG", "temperatura": 27},
        {"responsavel": "Governo Local", "evento": "Inspeção sanitária no CD Y", "local": "CD, SP", "temperatura": None},
        {"responsavel": "Transportadora X", "evento": "Entrega para outro supermercado", "local": "Galpão, MG", "temperatura": 10},
        {"responsavel": "Cliente João", "evento": "Feedback positivo sobre o tomate", "local": "App RastreiaFood", "temperatura": None},
    ])
    
    # Bloco 2 (Logística)
    bc.adicionar_bloco_legitimo([
         {"responsavel": "Produtor Fazenda B", "evento": "Colheita de alfaces", "local": "Estufa, PR", "temperatura": 22},
         {"responsavel": "Transportadora W", "evento": "Carregamento para distribuição", "local": "Galpão, PR", "temperatura": 12},
         {"responsavel": "Centro de Distribuição V", "evento": "Recebimento alfaces", "local": "CD, SC", "temperatura": 9},
         {"responsavel": "Supermercado U", "evento": "Exposição na gôndola alfaces", "local": "Loja, SC", "temperatura": 6},
         {"responsavel": "Cliente Pedro", "evento": "Compra de alface", "local": "Supermercado U, SC", "temperatura": None},
         {"responsavel": "App RastreiaFood", "evento": "Cliente Pedro escaneou QR Code", "local": "Online", "temperatura": None},
         {"responsavel": "Governo Local", "evento": "Inspeção Fazenda B", "local": "Estufa, PR", "temperatura": None},
         {"responsavel": "Transportadora W", "evento": "Entrega para outro CD", "local": "Galpão, PR", "temperatura": 11},
         {"responsavel": "Cliente Maria", "evento": "Feedback neutro sobre alface", "local": "App RastreiaFood", "temperatura": None},
         {"responsavel": "Produtor Fazenda B", "evento": "Preparo do solo", "local": "Estufa, PR", "temperatura": 20},
    ])

    # Bloco 3 (Engajamento/Social) - Seus exemplos
    bc.adicionar_bloco_legitimo([
        {"responsavel": "Cliente Sofia (12 anos)", "evento": "Fez trabalho escolar usando o QR do tomate", "local": "Colégio Santa Cruz, SP", "temperatura": None},
        {"responsavel": "Programa 'Do Campo à Mesa'", "evento": "Sofia ganhou 50 pontos por escanear", "local": "Online", "temperatura": None},
        {"responsavel": "Fazenda Orgânica Raiz", "evento": "Doou 1kg para cada 100 escaneamentos", "local": "Atibaia → ONG", "temperatura": None},
        {"responsavel": "ONG Banco de Alimentos", "evento": "Recebeu 127kg de tomates orgânicos", "local": "São Paulo", "temperatura": 6},
        {"responsavel": "Cliente Gustavo", "evento": "Plantou mudas com sementes do QR", "local": "Horta urbana, SP", "temperatura": 26},
        {"responsavel": "App Rastreia+", "evento": "Lançou versão com realidade aumentada", "local": "Online", "temperatura": None},
        {"responsavel": "Câmara Municipal SP", "evento": "Aprovou lei de rastreabilidade obrigatória", "local": "São Paulo", "temperatura": None},
        {"responsavel": "Ministério da Agricultura", "evento": "Tomate orgânico SP como case nacional", "local": "Brasília", "temperatura": None},
        {"responsavel": "Cliente Bruno", "evento": "Compartilhou no Instagram", "local": "Online", "temperatura": None},
        {"responsavel": "StartUp AgriTech", "evento": "Monitoramento de dados em tempo real", "local": "Nuvem", "temperatura": None},
    ])

    # Bloco 4 (Processamento Industrial)
    bc.adicionar_bloco_legitimo([
        {"responsavel": "Indústria Alimentícia A", "evento": "Recebimento do lote de tomates para molho", "local": "Fábrica, GO", "temperatura": 12},
        {"responsavel": "Linha de Produção 1", "evento": "Lavagem e seleção automatizada", "local": "Fábrica, GO", "temperatura": 15},
        {"responsavel": "Controle de Qualidade", "evento": "Análise de pH e acidez (aprovado)", "local": "Laboratório, GO", "temperatura": None},
        {"responsavel": "Cozinheiro Chefe", "evento": "Adição de temperos e cozimento a 90°C", "local": "Fábrica, GO", "temperatura": 90},
        {"responsavel": "Envase Asséptico", "evento": "Envasamento em potes de vidro", "local": "Fábrica, GO", "temperatura": 85},
        {"responsavel": "Etiquetagem", "evento": "Aplicação de rótulos e data de validade", "local": "Fábrica, GO", "temperatura": 25},
        {"responsavel": "Estoque Central", "evento": "Armazenamento do produto final", "local": "Galpão, GO", "temperatura": 20},
        {"responsavel": "Logística Indústria", "evento": "Preparação para despacho", "local": "Galpão, GO", "temperatura": 20},
        {"responsavel": "App RastreiaFood", "evento": "Novo QR Code gerado para o produto final (molho)", "local": "Online", "temperatura": None},
        {"responsavel": "Cliente Fernanda", "evento": "Comentário sobre novo molho", "local": "Site Fabricante", "temperatura": None},
    ])

    # Bloco 5 (Varejo)
    bc.adicionar_bloco_legitimo([
        {"responsavel": "Atacadista XYZ", "evento": "Recebimento do molho de tomate", "local": "CD, BA", "temperatura": 22},
        {"responsavel": "Supermercado Nordeste", "evento": "Compra e transporte para loja", "local": "Loja, PE", "temperatura": 25},
        {"responsavel": "Gerente de Loja", "evento": "Organização do molho na prateleira", "local": "Loja, PE", "temperatura": 25},
        {"responsavel": "Cliente Rodrigo", "evento": "Compra do molho", "local": "Loja, PE", "temperatura": None},
        {"responsavel": "App RastreiaFood", "evento": "Rodrigo escaneou o molho", "local": "Online", "temperatura": None},
        {"responsavel": "Governo PE", "evento": "Fiscalização de validade e armazenamento", "local": "Loja, PE", "temperatura": None},
        {"responsavel": "Atacadista XYZ", "evento": "Venda para outro mercado", "local": "CD, BA", "temperatura": 22},
        {"responsavel": "Supermercado Nordeste", "evento": "Promoção de molho ativada", "local": "Loja, PE", "temperatura": None},
        {"responsavel": "Cliente Camila", "evento": "Feedback sobre embalagem", "local": "Site Fabricante", "temperatura": None},
        {"responsavel": "Logística Reversa", "evento": "Potes de vidro coletados para reciclagem", "local": "PE", "temperatura": None},
    ])

    # Bloco 6 (Certificação/Auditoria)
    bc.adicionar_bloco_legitimo([
        {"responsavel": "Auditor ABC Certificações", "evento": "Início da auditoria anual da Fazenda A", "local": "Online/Local", "temperatura": None},
        {"responsavel": "Fazenda A", "evento": "Envio de documentos de manejo orgânico", "local": "Online", "temperatura": None},
        {"responsavel": "Laboratório Externo", "evento": "Análise de solo da Fazenda A (aprovado)", "local": "Laboratório, SP", "temperatura": None},
        {"responsavel": "Auditor ABC Certificações", "evento": "Visita in loco para verificação de processos", "local": "Campo, MG", "temperatura": None},
        {"responsavel": "Fazenda A", "evento": "Correção de não-conformidade menor identificada", "local": "Campo, MG", "temperatura": None},
        {"responsavel": "Auditor ABC Certificações", "evento": "Emissão do novo Certificado Orgânico 2025-2026", "local": "Online", "temperatura": None},
        {"responsavel": "BlockchainAlimentos", "evento": "Registro do novo certificado na cadeia", "local": "Nuvem", "temperatura": None},
        {"responsavel": "Indústria Alimentícia A", "evento": "Atualização de fornecedor certificado no sistema", "local": "Fábrica, GO", "temperatura": None},
        {"responsavel": "Governo MG", "evento": "Acompanhamento de subsídios para orgânicos", "local": "Online", "temperatura": None},
        {"responsavel": "Fazenda A", "evento": "Planejamento de expansão de área plantada", "local": "Campo, MG", "temperatura": None},
    ])

    # Bloco 7 (Inovação e Tecnologia)
    bc.adicionar_bloco_legitimo([
        {"responsavel": "Startup IoTGreen", "evento": "Instalação de novos sensores de umidade na Fazenda A", "local": "Campo, MG", "temperatura": None},
        {"responsavel": "Sistema IoTGreen", "evento": "Primeiros dados de umidade e temperatura coletados", "local": "Nuvem", "temperatura": 24},
        {"responsavel": "App RastreiaFood", "evento": "Integração com dados em tempo real dos sensores", "local": "Online", "temperatura": None},
        {"responsavel": "Cliente Mariana", "evento": "Visualização de dados climáticos da fazenda no app", "local": "Casa do Consumidor", "temperatura": None},
        {"responsavel": "Startup AgriTech", "evento": "Lançamento de IA para predição de safra", "local": "Nuvem", "temperatura": None},
        {"responsavel": "Fazenda A", "evento": "Adoção da IA para otimização de irrigação", "local": "Campo, MG", "temperatura": None},
        {"responsavel": "Governo Local", "evento": "Incentivo fiscal para uso de tecnologia em campo", "local": "Online", "temperatura": None},
        {"responsavel": "Cliente Carlos", "evento": "Relato de frescor superior no produto com rastreamento IoT", "local": "App RastreiaFood", "temperatura": None},
        {"responsavel": "Startup IoTGreen", "evento": "Manutenção preventiva em sensores", "local": "Campo, MG", "temperatura": None},
        {"responsavel": "Universidade Rural", "evento": "Parceria para estudo de caso em rastreabilidade", "local": "Online", "temperatura": None},
    ])

    # Bloco 8 (Sustentabilidade/Impacto)
    bc.adicionar_bloco_legitimo([
        {"responsavel": "ONG CarbonZero", "evento": "Cálculo da pegada de carbono do Bloco 1 de tomates", "local": "Online", "temperatura": None},
        {"responsavel": "Fazenda A", "evento": "Plano de compensação de carbono iniciado (plantio de árvores)", "local": "Reserva legal, MG", "temperatura": None},
        {"responsavel": "Cliente ONG Banco de Alimentos", "evento": "Doação de 1000kg de alimentos recebida", "local": "São Paulo", "temperatura": 5},
        {"responsavel": "Programa 'Do Campo à Mesa'", "evento": "Meta de doação do mês batida", "local": "Online", "temperatura": None},
        {"responsavel": "Supermercado Z", "evento": "Campanha de marketing focada em sustentabilidade", "local": "Loja, SP", "temperatura": None},
        {"responsavel": "Cliente Social", "evento": "Escanear QR Code contribui para doações", "local": "App RastreiaFood", "temperatura": None},
        {"responsavel": "Governo SP", "evento": "Reconhecimento de iniciativa sustentável", "local": "São Paulo", "temperatura": None},
        {"responsavel": "Conselho Comunitário", "evento": "Feedback positivo sobre impacto social das doações", "local": "Online", "temperatura": None},
        {"responsavel": "ONG CarbonZero", "evento": "Certificado de neutralidade de carbono emitido para Fazenda A", "local": "Online", "temperatura": None},
        {"responsavel": "BlockchainAlimentos", "evento": "Registro do certificado de carbono na cadeia", "local": "Nuvem", "temperatura": None},
    ])

    return bc

# ========================
# EXECUÇÃO DO PROGRAMA
# ========================
if __name__ == "__main__":

    # --- CENÁRIO 1: CADEIA ÍNTEGRA ---
    console.print(Panel("[bold cyan]CENÁRIO 1: DEMONSTRAÇÃO DE CADEIA ÍNTEGRA (8 BLOCOS)[/]", title_align="center"))
    bc_integro = carregar_dados_iniciais()
    bc_integro.mostrar()

    # --- CENÁRIO 2: SIMULAÇÃO DE ALTERAÇÃO (FRAUDE DETECTADA EM CADEIA) ---
    console.print(Panel("[bold cyan]CENÁRIO 2: SIMULAÇÃO DE ALTERAÇÃO EM EVENTO (BLOCO 6)[/]", title_align="center", border_style="red"))
    bc_fraude = carregar_dados_iniciais()

    # Simula uma alteração no Bloco 6, Transação 2 
    bc_fraude.fraudar_evento(num_bloco=6, num_tx=2, novo_evento="Planejamento aprovado sem problemas (FRAUDE!)")

    bc_fraude.mostrar()
