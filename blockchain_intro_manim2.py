# Rode com:
# manim -pqh -r 1080:1440 blockchain_intro_manim2.py BlockchainAnimation

from manim import *

class BlockchainAnimation(Scene):
    def construct(self):
        # === CONFIGURAÇÃO DA TELA VERTICAL (1080x1440) ===
        self.camera.frame_width = 9
        self.camera.frame_height = 12  # Proporção 1080:1440

        # Fundo azul-marinho profundo (o verdadeiro 3B1B)
        self.camera.background_color = "#0d1b2a"

        # Paleta de cores elegante e profissional
        BLOCK_COLOR     = "#F2E4D5"    
        BLOCK_BORDER    = "#FFF2B4"
        SUBTITULO       = "#E19891"
        TX_BG           = "#16213e"      # Azul muito escuro (quase preto) - ótimo contraste
        TX_BORDER       = "#7EBAFF"
        HASH_COLOR      = "#FF0520"      
        HASH_ANT_BLOCO  = "#0F0502"
        HASH_ANT_COLOR  = "#DFD510"        
        TEXT_COLOR      = "#f1fafe"      # Branco-creme suave
        ARROW_EXTERNO   = "#FF7D20"
        ARROW_INTERNO   = "#442D10"
        TITLE_COLOR     = "#F38708"
        VERDE_RCS       = "#C9FFC0"
        TITULO_BLOCK    = "#A922A0"

        # === DADOS DOS BLOCOS (mantive exatamente os nomes/hash originais + 3 novos) ===
        blocks_data = [
            { # Bloco 1 - 
                "hash": "22EF4412342944ABC34578",
                "hash_ant": "0000000000000000000000",
                "txs": [
                    {"nome": "Jon Doe", "nasc": "02/10/1960", "acao": "venda a Mary Silva", "valor": "R$ 45.800", "ts": "2025-06-15 14:32", 
                    "hash_ant": "0000000000000000000000", "hash": "19AAE44FFF1429555C3A7D"},
                    {"nome": "Mary Silva", "nasc": "01/02/1980", "acao": "venda a João Dutra", "valor": "R$ 72.300", "ts": "2025-06-15 15:01", 
                    "hash_ant": "19AAE44FFF1429555C3A7D", "hash": "62ABE4BB42956295292547"},
                    {"nome": "João Dutra", "nasc": "11/05/1970", "acao": "venda a Ana Lúcia", "valor": "R$ 119.000", "ts": "2025-06-15 15:45", 
                    "hash_ant": "62ABE4BB42956295292547", "hash": "F20DBCaAWBUFKC5NFGR95P"}
                ]
            },
            { # Bloco 2 
                "hash": "KUC*@GSHKJJSDCIO*FJ%JD",
                "hash_ant": "22EF4412342944ABC34578",
                "txs": [
                    {"nome": "Ana Lúcia", "nasc": "22/11/1975", "acao": "venda a Ary Sobral", "valor": "R$ 189.500", "ts": "2025-06-16 09:12", 
                    "hash_ant": "F20DBCaAWBUFKC5NFGR95P","hash": "TUCL3K@7K245&%0G996786"},
                    {"nome": "Ary Sobral", "nasc": "10/03/1990", "acao": "venda a Rita de Sá", "valor": "R$ 263.200", "ts": "2025-06-16 10:27", 
                    "hash_ant": "TUCL3K@7K245&%0G996786","hash": "23879kkH9shkvmnJHKjgu8"},
                    {"nome": "Rita de Sá", "nasc": "15/04/1968", "acao": "venda a Dany Ross", "valor": "R$ 397.750", "ts": "2025-06-16 11:03", 
                    "hash_ant": "23879kkH9shkvmnJHKjgu8","hash": "F42hs60gDBgCGRjd9srv5P"}
                ]
            },
            { # Bloco 3 
                "hash": "X9DK7P2M8Q5R2025TUVE7W",
                "hash_ant": "KUC*@GSHKJJSDCIO*FJ%JD",
                "txs": [
                    {"nome": "Dany Ross", "nasc": "03/08/1985", "acao": "venda a Carla Mota", "valor": "R$ 434.000", "ts": "2025-06-17 08:19", 
                    "hash_ant": "F42hs60gDBgCGRjd9srv5P","hash": "CR#T456MN789PQR2025XYZ"},
                    {"nome": "Carla Mota", "nasc": "19/12/1992", "acao": "venda a Pedro Alle", "valor": "R$ 482.400", "ts": "2025-06-17 09:55", 
                    "hash_ant": "CR#T456MN789PQR2025XYZ","hash": "PEye5R72025GYNFI*DK%88"},
                    {"nome": "Pedro Alle", "nasc": "27/07/1978", "acao": "venda a Luan Costa", "valor": "R$ 456.300", "ts": "2025-06-17 10:31", 
                    "hash_ant": "PEye5R72025GYNFI*DK%88","hash": "2UA9y4y7AE3D2g25B1O6KX"}
                ]
            },
            { # Bloco 4 
                "hash": "3IN4LCFQIN2d5X6YZs89AG",
                "hash_ant": "X9DK7P2M8Q5R2025TUVE7W",
                "txs": [
                    {"nome": "Luan Costa", "nasc": "05/01/1987", "acao": "venda a Ralf Lima", "valor": "R$ 501.500", "ts": "2025-06-18 13:22", 
                    "hash_ant": "2UA9y4y7AE3D2g25B1O6KX","hash": "R4eA2025HJA7S4H6E76D99"},
                    {"nome": "Ralf Lima", "nasc": "30/09/1995", "acao": "venda a Suse Duarte", "valor": "R$ 578.900", "ts": "2025-06-18 14:10", 
                    "hash_ant": "R4eA2025HJA7S4H6E76D99","hash": "15FI42025D53RLTA259fh8"},
                    {"nome": "Suse Duarte", "nasc": "12/06/1983", "acao": "venda a Robert Saint", "valor": "R$ 625.000", "ts": "2025-06-18 15:00", 
                    "hash_ant": "15FI42025D53RLTA259fh8","hash": "E5D6FC30IN2F2537g7Sf3G"}
                ]
            }
        ]

        # === CRIAÇÃO DOS BLOCOS ===
        block_width = 5.8
        block_height = 9.0
        start_x = -1

        all_blocks = VGroup()
        all_arrows = VGroup()

        for idx, data in enumerate(blocks_data):
            x_pos = start_x + idx * 7.0

            # Bloco principal
            block = RoundedRectangle(
                width=block_width, height=block_height,
                corner_radius=0.1, stroke_color=BLOCK_BORDER,
                fill_color=BLOCK_COLOR, fill_opacity=0.95,
                stroke_width=4
            )
            block.move_to(RIGHT * x_pos+DOWN * 0.15)          

            # Título do bloco
            title = Text(f"Bloco {idx+1}", font_size=18, color=TITULO_BLOCK, weight=BOLD)
            title.next_to(block.get_top(), DOWN, buff=0.2)

            hashcode = Text(f"HashCode atual: {data["hash"]}", font="Monospace", font_size=18, color=HASH_COLOR, weight=BOLD)
            hashcode.next_to(title, DOWN, buff=0.2)
            
            hashcodeant = Text(f"Hash anterior: {data["hash_ant"]}", font="Monospace", font_size=18, color=HASH_ANT_BLOCO, weight=BOLD)
            hashcodeant.next_to(hashcode, DOWN, buff=0.15)

            # Grupo de transações
            txs_group = VGroup()
            for i, tx in enumerate(data["txs"]):
                tx_rect = RoundedRectangle(
                    width=5.6, height=2.25, corner_radius=0.1, 
                    fill_color=TX_BG, fill_opacity=1,
                    stroke_color=TX_BORDER, stroke_width=2
                )

                content = VGroup(
                    Text(f"Nome: {tx['nome']}, data nasc.: {tx['nasc']}", font_size=17, color=TEXT_COLOR),
                    Text(f"Transação: {tx['acao']}", font_size=17, color=ORANGE),
                    Text(f"Valor:{tx['valor']}, data/hr:{tx['ts']}", font_size=17, color=VERDE_RCS),
                    Text(f"Hash anterior: {tx['hash_ant']}", font="Monospace", font_size=17, color=HASH_ANT_COLOR),
                    Text(f"Hash atual: {tx['hash']}", font="Monospace", font_size=17, color=HASH_COLOR)
                ).arrange(DOWN, aligned_edge=LEFT, buff=0.12)
                content.move_to(tx_rect.get_center())

                full_tx = VGroup(tx_rect, content)
                txs_group.add(full_tx)

            txs_group.arrange(DOWN, buff=0.45, center=True)
            txs_group.move_to(block.get_center() + DOWN * 0.52)

            # Setas entre transações
            tx_arrows = VGroup()
            for i in range(len(txs_group)-1):
                arrow = Arrow(
                    txs_group[i].get_bottom(), txs_group[i+1].get_top(),
                    color=ARROW_INTERNO, 
                    stroke_width=10,
                    max_tip_length_to_length_ratio=0.25  # ponta bem visível
                )
                tx_arrows.add(arrow)

            # Monta o bloco completo
            full_block = VGroup(block, title, hashcode, hashcodeant, txs_group, tx_arrows)
            all_blocks.add(full_block)

        for i in range(len(all_blocks)-1):
            arrow = Arrow(
                all_blocks[i].get_right(),
                all_blocks[i+1].get_left(),
                color=ARROW_EXTERNO,
                stroke_width=10,
                buff=0.12,                     # buff pequeno
                max_tip_length_to_length_ratio=0.25  # ponta bem visível
            )
            all_arrows.add(arrow)

        # === TÍTULO ===
        main_title = Text("Blockchain: Cadeia Imutável", font_size=32, color=TITLE_COLOR, weight=BOLD)
        main_title.move_to(UP*5.5)
        subtitle = Text("Cada bloco contém o hash do anterior", font_size=28, color=SUBTITULO, weight=BOLD)
        subtitle.next_to(main_title, DOWN, buff=0.4)

        # === ANIMAÇÃO ===
        self.play(Write(main_title), Write(subtitle), run_time=2)
        self.wait(1)

        # Entrada dos blocos um a um
        self.play(FadeIn(all_blocks[0], shift=RIGHT*20), FadeIn(all_arrows[0]), run_time=15)
        self.wait(0.6)

        for i in range(1, len(all_blocks)):
            self.play(
                FadeIn(all_blocks[i], shift=RIGHT*20),
                FadeIn(all_arrows[i-1] if i > 0 else None),
                run_time=1.0
            )
            self.wait(0.6)

        self.wait(0.8)

        # Rolagem horizontal suave e contínua
        self.play(
            all_blocks.animate.shift(LEFT * 30),
            all_arrows.animate.shift(LEFT * 30),
            run_time=20,
            rate_func=linear
        )

        self.wait(1)
        self.play(FadeOut(all_blocks[0], shift=UP*9.5),FadeOut(all_arrows[0], shift=UP*9.5))

        # Mensagem final
        final = Text("• Imutável • \n • Transparente • \n • Descentralizada •", font_size=32, color=TITLE_COLOR, weight=BOLD)        
        final.move_to(ORIGIN)      # ORIGIN é o mesmo que CENTER (0, 0, 0)
        self.play(FadeIn(final, shift=UP*0.5))
        self.wait(4)
        self.play(FadeOut(final, shift=UP*10.5))