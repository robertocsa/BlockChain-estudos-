# blockchain_intro_manim.py
# Rode com: 
# manim -pqh -r 1080,1512 blockchain_intro_manim3.py BlockchainIntro

from manim import *
import os

class BlockchainIntro(Scene):
          
    def construct(self):
        
        # Cores personalizadas
        CYAN = "#00FFFF"
        AZUL_ESCURO = "#0f172a"  # azul-escuro
        
        # ==================== CONFIGURAÇÃO VERTICAL 1080x1080 ====================
        self.camera.background_color = AZUL_ESCURO
        self.camera.frame_width = 10.0
        self.camera.frame_height = 14.0 
        # Ajuste da câmera para 10x10 (útil em vídeos menores ou slides)
        # self.camera.frame_scale=0.78  # 10/12.8 ≈ 0.78
        
        metade_largura=self.camera.frame_width/2
        metade_altura=self.camera.frame_height/2
        
        print("Largura em unidades Manim :", self.camera.frame_width)
        print("Altura em unidades Manim  :", self.camera.frame_height)
        print(f"Proporção → {self.camera.frame_width / self.camera.frame_height:.3f}:1")

        # Pixels finais (config é global, funciona em qualquer lugar)
        print(f"Pixels → {config.pixel_width} × {config.pixel_height}")
        print(f"Proporção pixels → {config.pixel_width / config.pixel_height:.3f}:1\n")

        # === TÍTULO GIGANTE E ANIMADO ===
        
        titulo = Text("Introdução ao Blockchain", font_size=50, color="#58a6ff")
        tam_titulo=titulo.width
        titulo.move_to(UP*(metade_altura-1.0))   
        self.add(titulo)
        self.wait(1.0)     
                
        # ============================= PARTE 3: CONCEITOS FUNDAMENTAIS =============================
        self.play(titulo.animate.become(
            Text("Conceitos Fundamentais", font_size=46, gradient=(YELLOW, ORANGE)).move_to(UP*(metade_altura-1.35))
        ))

        # ================================== 1. UM BLOCO ==================================
        bloco_completo = VGroup()  # tudo junto, fácil de mover
        bloco = RoundedRectangle(
            width=4.8, height=5.0, corner_radius=0.3,
            color="#118ab2", fill_opacity=0.9, stroke_width=6
        )
        titulo_bloco = Text("Bloco", font_size=45, color=WHITE, weight=BOLD
                           ).move_to(bloco.get_top() + DOWN*0.35)  # ajustado para caber

        conteudo = BulletedList(
            "Transações",
            "Hash do bloco anterior",
            "Timestamp",
            "Nonce",
            "Merkle Root",
            font_size=40, buff=0.5
        ).next_to(titulo_bloco, DOWN, buff=0.6)  

        bloco_completo.add(bloco, titulo_bloco, conteudo)
        self.play(FadeIn(bloco_completo, shift=DOWN), run_time=2)
        self.wait(2)
        
        
        # ================================== 2. HASH ==================================
        self.play(bloco_completo.animate.shift(LEFT*6.2))  # menos deslocamento (cabe no 10x10)

        seta_hash = Arrow(start=LEFT*4.5, end=LEFT*3.0, color=YELLOW, stroke_width=10, buff=0.2
                         ).shift(RIGHT*0.5).shift(UP*1.5)
        eq = MathTex(r"\text{Hash} = \text{SHA-256}(\text{todos os dados})", 
                     font_size=40).next_to(seta_hash, RIGHT, buff=0.25)
        resultado = Text("a3f9c262sR...fd38e1d", color="#06d6a0", font_size=40
                        ).next_to(eq, DOWN, buff=0.6)

        hash_group = VGroup(seta_hash, eq, resultado)

        self.play(GrowArrow(seta_hash), Write(eq))
        self.play(FadeIn(resultado, shift=UP))
        self.wait(1)

        alerta = Text("Se alguém alterar \nqualquer dado no bloco, \n "
                      "ainda que mínimo, \nmesmo que em apenas 1 bit,\n"
                      "isso faz o código hash\n alterar-se completamente!", 
                      color=RED, font_size=36, line_spacing=1.06).next_to(hash_group, DOWN, buff=0.2).shift(DOWN*0.3).shift(RIGHT*0.3)
        self.play(Write(alerta), Flash(resultado, color=RED, flash_radius=1.2, num_lines=30))
        self.wait(4)

        self.play(FadeOut(hash_group, alerta, bloco_completo), run_time=1.2)
        self.wait(1)

        # ================================== 3. EXPLICAÇÕES DETALHADAS (após o fadeout) ==================================
        titulo.shift(UP*0.5)
        titulo_explic = Text("Conceitos pertinentes a Blocos", font_size=36, color=YELLOW
                            ).move_to(UP*metade_altura).shift(DOWN*1.7)
        self.play(Write(titulo_explic))
        self.wait(1)

        itens = [
            ("Transações / Registros / Eventos",
             "Conjunto das ações registradas no bloco.\n"
             "Exemplos:\n"
             "• Transferência de criptomoeda ou token\n"
             "• Execução de contrato inteligente\n"
             "• Voto em eleição ou assembleia\n"
             "• Registro de ato civil (cartório digital)\n"
             "• Certificado de origem de um produto\n"
             "• Laudo sanitário de fiscalização\n"
             "• Emissão de diploma/certificado digital\n"
             "• Atualização de estoque em supply chain\n"
             "Qualquer fato que necessite registro e\n"
             "prova digital permanente"),

            ("Hash do bloco anterior",
             "O identificador criptográfico único  do\n"
             "                         bloco anterior.\n"
             "É o que transforma  milhares  de  blocos\n"
             "soltos em uma cadeia única, cronológica,\n"
             "e impossível de  ser  alterada  sem  que\n"
             "todos   percebam.   É  o  coração  da\n" 
             "imutabilidade em qualquer blockchain."),

            ("Timestamp",
             "Data e hora oficial  em  que  o  bloco\n"
             "foi selado. Esse registro  serve para:\n"
             "• Provar quando  um  evento  aconteceu\n"
             "     (ex.: hora exata de um voto)\n"
             "• Ordenar  todos  os  blocos  da  rede\n"
             "• Impedir que alguém repita  uma  ação\n"
             "      antiga (ataque de replay)\n"
             "• Cumprir prazos legais \n"
             "   (ex.: validade de um certificado)"),

            ("Nonce ou prova  de consenso",
             "Campo que prova  que  alguém, ou um \n"
             "grupo empregou esforços  ou foi legi-\n" 
             "timamente escolhido para criar o bloco.\n"
             "Pode ser:\n"
             "• Nonce  clássico:       Proof-of-Work\n"
             "• Assin. de validadores: Proof-of-Stake\n"
             "• VRF ou sorteio criptográfico\n"
             "• Votos de comitê BFT\n"
             "• Assinatura de órgão certificador\n"
             "          (blockchain permissionada)\n"
             "O importante é que: só quem tem  di-\n"
             "                  reito cria o bloco."),

            ("Merkle Root ou raiz transações/estados",
             "Um único hash que 'resume' as transa-\n"
             "ções do bloco de forma criptograficamen-\n"
             "te segura. Permite que qualquer pessoa\n"
             "prove, com poucos kilobytes, que deter-\n" 
             "minado evento está, ou não está, naque-\n" 
             "le bloco.       Usado em:\n"
             "• Carteiras leves de criptomoedas\n"
             "• Verificação de diploma sem baixar\n"
             "  toda a blockchain da universidade\n"
             "• Comprovação de que um lote de \n"
             "    medicamento foi inspecionado\n"
             "• Auditoria de votos sem necessidade\n"
             "      de abertura das urnas digitais")
        ]

        explicacoes = VGroup()
        for item_texto, explic in itens:
            # Destaca o item da lista original
            item = Text("• " + item_texto, font_size=35, color="#06d6a0", line_spacing=1.0)
            caixa = SurroundingRectangle(item, color=YELLOW, buff=0.15, corner_radius=0.15)
            destaque = VGroup(item, caixa)
            destaque.next_to(titulo_explic,DOWN, buff=0.84)

            # Texto explicativo abaixo
            texto_exp = Text(explic, font_size=32, color=WHITE, line_spacing=1.0).next_to(destaque, DOWN, buff=0.4) 
            grupo = VGroup(destaque, texto_exp).arrange(DOWN, buff=0.95)
            explicacoes.add(grupo)

        # Animação sequencial das explicações
        for exp in explicacoes:
            self.play(FadeIn(exp, shift=DOWN, buff=0.4), run_time=1.5)
            self.wait(5)  # tempo suficiente para ler cada explicação
            self.play(FadeOut(exp), run_time=0.2)

        self.wait(0.2)
        self.play(FadeOut(titulo_explic, explicacoes))        
        
        '''

        # ================================== 3. CADEIA DE BLOCOS ==================================
        cadeia = VGroup()
        hashes_texto = VGroup()

        for i in range(5):
            b = RoundedRectangle(width=4.0, height=2.8, corner_radius=0.25,
                                color=["#1e3a8a","#1e40af","#2563eb","#3b82f6","#60a5fa"][i],
                                fill_opacity=0.9)
            b.move_to(RIGHT * (i-2) * 4.5)  # centralizado perfeitamente
            
            num = Text(str(i), font_size=72, color=WHITE, weight=BOLD).move_to(b)
            h = Text("Genesis" if i == 0 else "hash anterior", font_size=26, color=GREY_B).next_to(b, DOWN, buff=0.6)
            
            cadeia.add(VGroup(b, num))
            hashes_texto.add(h)

        self.play(LaggedStartMap(FadeIn, cadeia, shift=UP, lag_ratio=0.3), run_time=3)
        self.play(FadeIn(hashes_texto, shift=DOWN))
        self.wait(1)

        # Setas da cadeia
        setas = VGroup()
        for i in range(4):
            seta = Arrow(
                cadeia[i][0].get_right(),
                cadeia[i+1][0].get_left(),
                buff=0.4,
                color=YELLOW,
                stroke_width=10,
                max_tip_length_to_length_ratio=0.18
            )
            setas.add(seta)

        self.play(LaggedStart(*[GrowArrow(s) for s in setas], lag_ratio=0.3), run_time=3.2)

        imutabilidade = Text("Alterar um bloco antigo\nquebra toda a cadeia", 
                             color=RED, font_size=46, weight=BOLD).to_edge(DOWN)
        self.play(Write(imutabilidade))
        self.wait(4)
        self.play(FadeOut(imutabilidade))

        # ================================== 4. REDE DISTRIBUÍDA ==================================
        self.play(FadeOut(cadeia, hashes_texto, setas))

        nodes = VGroup()
        for angle in np.arange(0, 360, 60):
            rad = np.deg2rad(angle)
            pos = 4.3 * np.array([np.cos(rad), np.sin(rad), 0])
            dot = Dot(pos, radius=0.6, color="#06d6a0", fill_opacity=1)
            label = Text("Nó", font_size=32, color=WHITE).next_to(dot, direction=pos, buff=1.1)
            nodes.add(VGroup(dot, label))

        centro_texto = Text("Todos têm a mesma cópia\nexata do livro-caixa", 
                            font_size=48, color="#ffd60a", weight=BOLD)

        self.play(LaggedStartMap(GrowFromCenter, nodes, lag_ratio=0.25), run_time=4)
        self.play(Write(centro_texto))
        self.wait(4)

        self.play(FadeOut(nodes, centro_texto))

        # ============================= PARTE 3: CASOS PRÁTICOS =============================
        self.play(titulo.animate.become(
            Text("Casos Reais", font_size=66, gradient=(PINK, GOLD)).to_edge(UP, buff=0.8)
        ))

        # Caso 1: Rastreabilidade de Alimentos
        titulo_caso1 = Text("Rastreabilidade de Alimentos", font_size=54, color=ORANGE).to_edge(UP, buff=1.5)

        tomate = Circle(radius=1.2, color=RED, fill_opacity=1).move_to(LEFT*3.5 + UP*1)
        tomate_label = Text("Tomate", color=WHITE, font_size=32).move_to(tomate)

        self.play(FadeIn(titulo_caso1), GrowFromCenter(tomate), Write(tomate_label))

        etapas = VGroup(*[
            Text(etapa, font_size=36, color=cor) for etapa, cor in [
                ("Fazenda", GREEN), ("Transporte", BLUE), ("Fábrica", PURPLE),
                ("Mercado", YELLOW), ("Você", TEAL)
            ]
        ]).arrange(RIGHT, buff=1.8).next_to(titulo_caso1, DOWN, buff=1.2)

        self.play(FadeIn(etapas, shift=DOWN))
        self.wait(1)

        qr = Square(side_length=2.2, fill_color=BLACK, stroke_color=WHITE).move_to(RIGHT*3.5)
        qr_text = Text("QR Code", font_size=42, color=WHITE).move_to(qr)
        self.play(GrowFromCenter(qr), Write(qr_text))
        self.play(Indicate(tomate), Indicate(qr))
        self.wait(3)
        self.play(FadeOut(titulo_caso1, tomate, tomate_label, etapas, qr, qr_text))

        # Caso 2: Registro Imobiliário
        casa = VGroup(
            Triangle(fill_color=RED, fill_opacity=1).scale(1),
            Square(fill_color=BLUE_D, fill_opacity=1).scale(1).next_to(Triangle(), DOWN, buff=0)
        ).move_to(LEFT*3.5)

        titulo_caso2 = Text("Imóvel sem Cartório", font_size=34, color=GOLD).to_edge(UP, buff=1.5)
        self.play(FadeIn(titulo_caso2), FadeIn(casa))

        joao = Text("João", color=RED, font_size=52).next_to(casa, RIGHT, buff=2.5)
        maria = Text("Maria", color=GREEN, font_size=52).next_to(joao, RIGHT, buff=2.5)

        seta1 = Arrow(joao.get_left(), casa.get_right(), color=YELLOW)
        seta2 = Arrow(maria.get_left(), joao.get_right(), color=YELLOW)

        livro = RoundedRectangle(width=4.5, height=6, color=GREY_D, fill_opacity=0.9).to_edge(RIGHT)
        livro_texto = Text("Livro\nImutável", font_size=40, color=WHITE).move_to(livro)

        self.play(Write(joao), GrowArrow(seta1))
        self.wait(1)
        self.play(Transform(joao, maria), GrowArrow(seta2))
        self.play(Create(livro), Write(livro_texto))
        self.play(Flash(livro, color=YELLOW))
        self.wait(3)

        # MSG FINAL 
        final = Text("Blockchain =\nConfiança Programada", 
                     font_size=80, gradient=(TEAL, PINK, GOLD), line_spacing=1.4)
        self.play(Write(final), run_time=4)
        self.wait(6)

        self.play(FadeOut(final, titulo_caso2, casa, joao, livro))
        '''