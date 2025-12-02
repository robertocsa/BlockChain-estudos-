# blockchain_intro_manim.py
# Rode com: 
# manim -pqh -r 1920,1080 blockchain_intro_manim4.py BlockchainAnim4

from manim import *
import os

class BlockchainAnim4(Scene):
          
    def construct(self):
        
        # Cores personalizadas
        CYAN = "#00FFFF"
        AZUL_ESCURO = "#0f172a"  # azul-escuro
        DARK_RED = "#A10003"
        
        # ==================== CONFIGURAÇÃO VERTICAL 1080x1080 ====================
        self.camera.background_color = AZUL_ESCURO
        self.camera.frame_width = 22.0
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
   
        # ================================== CADEIA DE BLOCOS ==================================
        cadeia = VGroup()
        hashes_texto = VGroup()

        for i in range(5):
            b = RoundedRectangle(width=2.8, height=2.8, corner_radius=0.25,
                                color=["#1e3a8a","#1e40af","#2563eb","#3b82f6","#60a5fa"][i],
                                fill_opacity=0.9)
            b.move_to(RIGHT * (i-2) * 4.8)  # centralizado perfeitamente
            
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
                buff=0.2,
                color=YELLOW,
                stroke_width=10,
                max_tip_length_to_length_ratio=0.18
            )
            setas.add(seta)

        self.play(LaggedStart(*[GrowArrow(s) for s in setas], lag_ratio=0.3), run_time=3.2)

        imutabilidade = Text("Alterar um bloco antigo\nquebra toda a cadeia", 
                             color=RED, font_size=46, weight=BOLD).next_to(hashes_texto, DOWN, buff=0.4)
        self.play(Write(imutabilidade))
        self.wait(4)
        self.play(FadeOut(imutabilidade))

        # ================================== REDE DISTRIBUÍDA ==================================
        self.play(FadeOut(cadeia, hashes_texto, setas))

        nodes = VGroup()
        for angle in np.arange(0, 360, 40):
            rad = np.deg2rad(angle)
            pos = 4.0 * np.array([np.cos(rad), np.sin(rad), 0])
            dot = Dot(pos, radius=0.8, color="#06d6a0", fill_opacity=1)
            label = Text("Nó", font_size=32, color=WHITE).next_to(dot, direction=pos, buff=0.0)
            nodes.add(VGroup(dot, label))

        centro_texto = Text("Todos têm a mesma\n cópia exata do\n 'livro-digital'", 
                            font_size=40, color="#ffd60a", weight=BOLD)

        self.play(LaggedStartMap(GrowFromCenter, nodes, lag_ratio=0.25), run_time=4)
        self.play(Write(centro_texto))
        self.wait(4)

        self.play(FadeOut(nodes, centro_texto))

        # ============================= PARTE 3: CASOS DE USO =============================
        self.play(titulo.animate.become(
            Text("Casos de Uso", font_size=66, gradient=(PINK, GOLD)).to_edge(UP*-11.0, buff=0.8)
        ))

        # Caso 1: Rastreabilidade de Alimentos 

        # Título
        titulo = Text("Rastreabilidade de Alimentos", font_size=58, color=ORANGE)
        titulo.to_edge(UP*-10.0, buff=0.8)
        self.play(Write(titulo))
        self.wait(1)

        # Tomate + rótulo agrupados
        tomate = Circle(radius=1.0, fill_color=RED, fill_opacity=1, stroke_width=4, stroke_color=DARK_RED)
        tomate_label = Text("Tomate", color=WHITE, font_size=36).move_to(tomate)
        tomate_grupo = VGroup(tomate, tomate_label)
        tomate_grupo.move_to(LEFT*7 + DOWN*1.5)

        self.play(GrowFromCenter(tomate_grupo))
        self.wait(0.8)

        # === Ícones feitos à mão (sem SVG) ===
        icons = VGroup()

        # 1. Fazenda → árvore simples
        tree = VGroup(
            Rectangle(width=0.6, height=1.4, color=GREEN_D, fill_opacity=1),  # tronco
            Circle(radius=0.8, color=GREEN, fill_opacity=1).shift(UP*0.8)     # copa
        )

        # 2. Transporte → caminhão simples
        truck = VGroup(
            Rectangle(width=2.2, height=0.9, color=BLUE_D, fill_opacity=1),
            Rectangle(width=0.8, height=0.8, color=BLUE_D, fill_opacity=1).shift(LEFT*1.2),
            Circle(radius=0.3, color=BLACK, fill_opacity=1).shift(LEFT*0.8 + DOWN*0.5),
            Circle(radius=0.3, color=BLACK, fill_opacity=1).shift(RIGHT*0.8 + DOWN*0.5),
        )

        # 3. Fábrica → chaminé + prédio
        factory = VGroup(
            Rectangle(width=1.6, height=1.6, color=PURPLE_D, fill_opacity=1),
            Rectangle(width=0.4, height=1.0, color=RED).shift(LEFT*0.7 + UP*0.8),
            Rectangle(width=0.1, height=0.6, color=GREY).shift(LEFT*0.7 + UP*1.4),
        )

        # 4. Distribuidor/Mercado → prateleira
        store = VGroup(
            Rectangle(width=2.0, height=0.3, color=YELLOW_D, fill_opacity=1),
            Rectangle(width=2.0, height=0.3, color=YELLOW_D, fill_opacity=1).shift(UP*0.5),
            Rectangle(width=0.2, height=1.4, color=YELLOW_E).shift(LEFT*0.8 + UP*0.2),
            Rectangle(width=0.2, height=1.4, color=YELLOW_E).shift(RIGHT*0.8 + UP*0.2),
        )

        # 5. Consumidor → pessoa (cabeça + corpo)
        person = VGroup(
            Circle(radius=0.5, color=TEAL, fill_opacity=1),
            Rectangle(width=0.8, height=1.4, color=TEAL, fill_opacity=1).shift(DOWN*0.9)
        )

        icons.add(tree, truck, factory, store, person)

        # Textos das etapas
        textos = VGroup(
            Text("Fazenda", color=GREEN, font_size=40),
            Text("Transporte", color=BLUE, font_size=40),
            Text("Fábrica", color=PURPLE, font_size=40),
            Text("Mercado", color=YELLOW, font_size=40),
            Text("Você", color=TEAL, font_size=40),
        ).arrange(RIGHT, buff=2.4).next_to(titulo, DOWN, buff=3.2)

        # Posiciona ícones acima dos textos
        for icon, texto in zip(icons, textos):
            icon.next_to(texto, UP, buff=0.5)

        tudo_etapas = VGroup(textos, icons)
        self.play(FadeIn(tudo_etapas, shift=DOWN))
        self.wait(1)

        # Linha tracejada do caminho
        caminho = DashedLine(LEFT*7, RIGHT*7, color=GREY_C).shift(DOWN*1.5)
        self.play(Create(caminho), run_time=2)

        # Movimento do tomate por todas as etapas
        for i in range(5):
            destino = textos[i].get_center() + DOWN*1.5
            self.play(
                Indicate(textos[i], color=WHITE, scale_factor=1.4),
                tomate_grupo.animate.move_to(destino),
                run_time=2,
                rate_func=linear
            )
            self.wait(0.4)

        # QR Code aparece no tomate quando chega no consumidor
        qr_fundo = Square(side_length=1.8, fill_color=BLACK, stroke_color=WHITE, stroke_width=8)
        qr_fundo.next_to(tomate, LEFT, buff=0.4)
        
        qr_pontos = VGroup(*[
            Square(0.2, fill_color=WHITE) for _ in range(20)
        ]).arrange_in_grid(5, 4, buff=0.12).move_to(qr_fundo)

        qr = VGroup(qr_fundo, qr_pontos)
        qr_texto = Text("Escaneie o QR Code", font_size=32, color=WHITE).next_to(qr, DOWN, buff=0.5)

        self.play(
            GrowFromCenter(qr),
            Write(qr_texto),
            tomate_grupo.animate.scale(0.85)
        )
        self.play(Wiggle(qr), Indicate(qr, color=YELLOW))
        self.wait(3)

        # Fade out final
        self.play(
            FadeOut(VGroup(titulo, tudo_etapas, caminho, tomate_grupo, qr, qr_texto)),
            run_time=2
        )
        self.wait(1)

        