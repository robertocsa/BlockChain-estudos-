# blockchain_intro_manim1.py
# Rode com: manim -pqh -r 1080,1080 blockchain_intro_manim1.py BlockchainIntro

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