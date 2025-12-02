# blockchain_intro_manim.py
# Rode com: 
# manim -pqh -r 1920,1080 blockchain_intro_manim5.py BlockchainAnim4

from manim import *
import os

class BlockchainAnim5(Scene):
          
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
           
        # ============================= CASOS DE USO =============================
        self.play(titulo.animate.become(
            Text("Casos de Uso", font_size=66, gradient=(PINK, GOLD)).to_edge(UP*-11.0, buff=0.8)
        ))
        
        # Caso 2: Registro Imobiliário
        
        # Ícone de casa (triângulo + quadrado + texto)
        triangulo = Triangle(fill_color=RED, fill_opacity=1).scale(1.2)
        quadrado  = Square(fill_color=BLUE_D, fill_opacity=1, stroke_width=4).scale(0.9)
        quadrado.next_to(triangulo, DOWN, buff=0)                    
        
        texto_imovel = Text("Imóvel", font_size=28, color=WHITE).move_to(quadrado)

        casa = VGroup(triangulo, quadrado, texto_imovel)
        casa.scale(1.3).shift(LEFT*4)

        self.play(DrawBorderThenFill(casa), run_time=2)
        self.wait(1)       
        
        titulo_caso2 = Text("Registro imobiliário (Cartório digital)", font_size=42, color=GOLD).to_edge(UP*-10.0, buff=1.5)
       
        self.play(FadeIn(titulo_caso2), FadeIn(casa))

        joao = Text("João", color=RED, font_size=52).next_to(casa, RIGHT, buff=2.5)
        seta1 = Arrow(joao.get_left(), casa.get_right(), color=YELLOW)
        livro = RoundedRectangle(width=3.8, height=4.2, color=GREY_D, fill_opacity=0.9).next_to(joao, RIGHT, buff=2.5).shift(DOWN*1.2)
        livro_texto = Text("Registro\nImobiliário\nem\nLivro\nDigital\nImutável", font_size=34, color=WHITE).move_to(livro)        
        seta2 = Arrow(joao.get_right(), livro.get_left(), color=YELLOW)
        maria = Text("Maria", color=GREEN, font_size=52).next_to(joao, DOWN, buff=2.5)
        seta3 = Arrow(livro.get_left(),maria.get_right(), color=YELLOW)        
        seta4 = Arrow(maria.get_left(), casa.get_right(), color=YELLOW)        

        self.play(Write(joao), GrowArrow(seta1))
        self.wait(1.5)
        self.play(FadeOut(seta1))
        self.play(Create(livro), Write(livro_texto))
        self.wait(1.5)        
        self.play(GrowArrow(seta2))
        self.wait(1.5)
        self.play(Flash(livro, 
                  color=YELLOW,              # cor do flash (YELLOW, WHITE, RED, etc.)
                  flash_radius=1.8,          # tamanho do flash
                  line_length=1.3,           # comprimento das linhas que saem
                  num_lines=30,              # quantidade de raios (12–30 fica ótimo)
                  time_width=0.5,            # espessura temporal (quanto mais alto, mais “lento”)
                  run_time=1.5               # duração total da animação
                  ))
        self.play(FadeOut(joao))
        self.play(FadeOut(seta2))
        self.play(Write(maria), GrowArrow(seta3))
        self.wait(1.5)
        self.play(FadeOut(seta3))
        self.play(GrowArrow(seta4))
        self.wait(1.5)        
        self.play(Flash(livro, 
                  color=GOLD,              # cor do flash (YELLOW, WHITE, RED, etc.)
                  flash_radius=0.8,          # tamanho do flash
                  line_length=1.3,           # comprimento das linhas que saem
                  num_lines=30,              # quantidade de raios (12–30 fica ótimo)
                  time_width=0.5,            # espessura temporal (quanto mais alto, mais “lento”)
                  run_time=0.5               # duração total da animação
                  ))
        self.wait(1.5)
        self.play(FadeOut(seta4))
        
        grupoRegImovel=VGroup(maria, livro, livro_texto)
        self.play(FadeOut(grupoRegImovel))
        
        casa.shift(DOWN*1.5).shift(RIGHT*4)
        
        # MSG FINAL 
        final = Text("Blockchain = Confiança, agilidade e transparência", 
                     font_size=46, gradient=(TEAL, PINK, GOLD), line_spacing=1.4)
        self.play(Write(final), run_time=4)
        self.wait(6)

        self.play(FadeOut(final, titulo_caso2, casa))
       