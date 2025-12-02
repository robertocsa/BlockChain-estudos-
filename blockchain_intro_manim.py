# blockchain_intro_manim.py
# Rode com: manim -pqh -r 1080,1080 blockchain_intro_manim.py BlockchainIntro
# ou simplesmente: manim -pqh blockchain_intro_manim.py BlockchainIntro (ele já detecta 9:12)

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
        self.camera.frame_height = 10.0 
        
        metade_largura=self.camera.frame_width/2
        metade_altura=self.camera.frame_height/2
        
        print("Largura em unidades Manim :", self.camera.frame_width)
        print("Altura em unidades Manim  :", self.camera.frame_height)
        print(f"Proporção → {self.camera.frame_width / self.camera.frame_height:.3f}:1")

        # Pixels finais (config é global, funciona em qualquer lugar)
        print(f"Pixels → {config.pixel_width} × {config.pixel_height}")
        print(f"Proporção pixels → {config.pixel_width / config.pixel_height:.3f}:1\n")

        # === TÍTULO GIGANTE E ANIMADO ===
        
        titulo = Text("Introdução ao Blockchain", font_size=51, color="#58a6ff")
        tam_titulo=titulo.width
        titulo.move_to(UP*(metade_altura-0.8))   #+LEFT*(metade_largura-tam_titulo/2))
        self.add(titulo)
        self.wait(1.0)
       
        # ============================= PARTE 1: O QUE É BLOCKCHAIN? =============================
        titulo2 = Text("O que é Blockchain?", font_size=50, gradient=(BLUE_B, TEAL)).move_to(UP*(metade_altura-(2.2*0.8)))
        self.add(titulo2)
        self.wait(0.6)

        # Subtítulo 1 (analogia do livro-caixa)
        subtitulo1 = Text(
            "Um livro-caixa digital\n"
            "que ninguém consegue apagar\n"
            "nem falsificar sem deixar rastro.\n"
            "Confiabilidade e transparência\n"
            "são os principais atributos\n"
            "dessa tecnologia.",
            font_size=32,
            color=GREY_A,
            line_spacing=1.2
        ).next_to(titulo2, DOWN, buff=1.0)

        self.play(Write(titulo), run_time=2)
        self.play(FadeIn(subtitulo1, shift=DOWN), run_time=1.5)
        self.wait(2.5)

        # ← FadeOut explícito do subtítulo 1
        self.play(FadeOut(titulo2, subtitulo1), run_time=1)                
        
        # ============================= ÁREAS BENEFICIADAS COM ROLAGEM SUAVE =============================
        subtitulo2 = Text(
            "Aplicações muito promissoras:",
            font_size=36,
            color="#ffd60a",
            weight=BOLD
        ).next_to(titulo, DOWN, buff=0.95)

        self.play(FadeIn(subtitulo2, shift=UP), run_time=1.5)
        self.wait(1)             

        itens_texto = [
            "Rastreamento de produtos",
            "Contratos inteligentes",
            "Registros de imóveis e cartórios",
            "Governança pública e privada",
            "Sistemas bancários e pagamentos",
            "Controle de origem de produção",
            "Votação eletrônica e sufrágios",
            "Cadeias de suprimentos globais",            
            "Registros médicos e prontuários",
            "Redução de custos de controles",
            "Gestão de direitos autorais",            
            "Emissão e controle de certificados",  
            "Gestão de seguros e sinistros",
            "Redução de custos em remessas",
            "Fiscalização sanitária",
            "....",
        ]
        
        quantidadeItens=len(itens_texto)

        itens_mobjects = self.criar_lista_com_bullets(itens_texto)
        
        tamanho_linha=Text(itens_texto[0]).width
        
        self.rolar_lista_fixa(itens_mobjects)
        
        
        '''
        # ============================= PARTE 2: CONCEITOS FUNDAMENTAIS =============================
        self.play(titulo.animate.become(
            Text("Conceitos Fundamentais", font_size=48, gradient=(YELLOW, ORANGE)).to_edge(UP, buff=0.8)
        ))

        # ================================== 1. UM BLOCO ==================================
        bloco_completo = VGroup()  # tudo junto, fácil de mover

        bloco = RoundedRectangle(
            width=5.2, height=4.0, corner_radius=0.3,
            color="#118ab2", fill_opacity=0.9, stroke_width=6
        )
        titulo_bloco = Text("Bloco", font_size=48, color=WHITE, weight=BOLD).move_to(bloco.get_top() + UP*0.6)

        conteudo = BulletedList(
            "Transações", "Hash do bloco anterior", "Timestamp", "Nonce", "Merkle Root",
            font_size=34, buff=0.6
        ).next_to(bloco, DOWN, buff=0.8)

        bloco_completo.add(bloco, titulo_bloco, conteudo)

        self.play(FadeIn(bloco_completo, shift=DOWN), run_time=2)
        self.wait(2)

        # ================================== 2. HASH ==================================
        self.play(bloco_completo.animate.shift(LEFT*5.5))

        seta_hash = Arrow(start=LEFT*2, end=LEFT*0.2, color=YELLOW, stroke_width=12, buff=0)
        eq = MathTex(r"\text{Hash} = \text{SHA-256}(\text{todos os dados})", font_size=44).next_to(seta_hash, RIGHT, buff=1)
        resultado = Text("a3f9c2...8e1d", color="#06d6a0", font_size=48).next_to(eq, DOWN, buff=0.8)

        hash_group = VGroup(seta_hash, eq, resultado)

        self.play(GrowArrow(seta_hash), Write(eq))
        self.play(FadeIn(resultado, shift=UP))
        self.wait(1)

        alerta = Text("Mude 1 bit → hash muda completamente!", color=RED, font_size=38).to_edge(DOWN)
        self.play(Write(alerta), Flash(resultado, color=RED, flash_radius=1, num_lines=30))
        self.wait(3)

        self.play(FadeOut(hash_group, alerta, bloco_completo), run_time=1.2)

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
    def rolar_lista_fixaOLD(self, itens_mobjects, linhas_visiveis, buff, inicio_y):
        posicoes = [inicio_y - i*buff for i in range(linhas_visiveis)]
        posicoes_fixas = [UP * y for y in posicoes]
        
        # inicializa
        visiveis = VGroup()
        for i in range(linhas_visiveis):
            item = itens_mobjects[i].copy().move_to(posicoes_fixas[i])
            visiveis.add(item)
            self.add(item)
        
        # rolagem
        for i in range(linhas_visiveis, len(itens_mobjects)):
            novo = itens_mobjects[i].copy()
            novo.move_to(posicoes_fixas[-1] + DOWN*buff).set_opacity(0)
            self.add(novo)
            
            anims = [visiveis[j].animate.move_to(posicoes_fixas[j-1]).set_opacity(0 if j==0 else 1)
                     for j in range(linhas_visiveis)]
            anims.append(novo.animate.move_to(posicoes_fixas[-1]).set_opacity(1))
            
            self.play(LaggedStart(*anims, lag_ratio=0.3), run_time=1.2)
            visiveis.remove(visiveis[0])
            visiveis.add(novo)
            self.wait(0.6)
            
    def criar_lista_com_bullets(self, textos):
        itens = VGroup()
        for txt in textos:
            bullet = Text("•", font_size=34, color="#ffd60a")
            conteudo = Text(txt, font_size=34, color="#06d6a0")
            linha = VGroup(bullet, conteudo).arrange(RIGHT, buff=0.4)
            itens.add(linha)
        itens.arrange(DOWN, buff=0.6, aligned_edge=LEFT)
        return itens

    def rolar_lista_fixa(self, itens_mobjects, linhas_visiveis=7, buff=0.85, inicio_y=1.75, margem_esquerda=0.5):
        """
        Exibe uma lista com rolagem suave, com posições fixas na tela e alinhada à esquerda.
        
        margem_esquerda: distância da borda esquerda da tela (em unidades Manim)
        """
        # Metade da largura útil da tela (em unidades Manim)
        metade_largura = self.camera.frame_width / 2

        # Cria as posições Y fixas (vertical)
        posicoes_y = [inicio_y - i * buff for i in range(linhas_visiveis)]
        
        # Grupo com as posições finais (X + Y) — será usado para move_to
        posicoes_fixas = VGroup()
        
        # Inicializa os itens visíveis
        visiveis = VGroup()

        # === FASE 1: ANIMAÇÃO DE ENTRADA PROGRESSIVA (1 por 1) ===
        for i in range(linhas_visiveis):
            item = itens_mobjects[i].copy()
            
            # Calcula a posição X: alinhado à esquerda
            largura_item = item.width
            x_pos = LEFT * (metade_largura - margem_esquerda - largura_item / 2)
            pos_final = x_pos + UP * posicoes_y[i]
            
            # Começa fora da tela (de baixo) e invisível
            item.move_to(pos_final + DOWN * buff).set_opacity(0)
            self.add(item)
            visiveis.add(item)
            posicoes_fixas.add(Dot(pos_final).set_opacity(0))

            # Animação: sobe e aparece (igual à rolagem!)
            self.play(
                item.animate.move_to(pos_final).set_opacity(1),
                run_time=1.0,
                rate_func= linear
            )
            self.wait(0.8)  # pausa entre entradas

        # pausa antes de começar a rolar
        self.wait(1)

        # === ROLAGEM ===
        for i in range(linhas_visiveis, len(itens_mobjects)):
            novo = itens_mobjects[i].copy()
            
            # Posição inicial do novo item: mesma X (alinhado à esquerda), mas 1 linha abaixo
            largura_novo = novo.width
            x_novo = LEFT * (metade_largura - margem_esquerda - largura_novo / 2)
            novo.move_to(x_novo + UP * (posicoes_y[-1] - buff))
            novo.set_opacity(0)
            self.add(novo)

            # Animações
            anims = []
            for j in range(linhas_visiveis):
                item_atual = visiveis[j]
                largura_atual = item_atual.width
                x_destino = LEFT * (metade_largura - margem_esquerda - largura_atual / 2)
                y_destino = posicoes_y[j-1] if j > 0 else posicoes_y[0] - buff  # o primeiro sai
                
                anim = item_atual.animate.move_to(x_destino + UP * y_destino)
                if j == 0:
                    anim = anim.set_opacity(0)
                anims.append(anim)

            # Novo item entra na última posição fixa
            x_final_novo = LEFT * (metade_largura - margem_esquerda - largura_novo / 2)
            anims.append(
                novo.animate.move_to(x_final_novo + UP * posicoes_y[-1]).set_opacity(1)
            )

            self.play(LaggedStart(*anims, lag_ratio=0.4), run_time=1.5)

            # Atualiza lista lógica
            visiveis.remove(visiveis[0])
            visiveis.add(novo)

            self.wait(2.0)
        self.wait(2.0)