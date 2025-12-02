# blockchain_intro_manim.py
# Rode com: 
# manim -pqh -r 1920,1080 blockchain_intro_manim6.py BlockchainAnim6

from manim import *
import os

# Caso 2: Registro Imobiliário – versão corrigida e bonita
class BlockchainAnim6(Scene):
    def construct(self):
        # Título
        titulo = Text("Registro Imobiliário (Cartório Digital)", font_size=42, color=ORANGE)
        titulo.to_edge(UP, buff=0.2)
        self.play(Write(titulo))
        self.wait(1)

        # Ícone de casa (triângulo + quadrado + texto)
        triangulo = Triangle(fill_color=RED, fill_opacity=1).scale(1.2)
        quadrado  = Square(fill_color=BLUE_D, fill_opacity=1, stroke_width=4).scale(0.9)
        quadrado.next_to(triangulo, DOWN, buff=0)                    
        
        texto_imovel = Text("Imóvel", font_size=28, color=WHITE).move_to(quadrado)

        casa = VGroup(triangulo, quadrado, texto_imovel)
        casa.scale(1.3).shift(LEFT*4)

        self.play(DrawBorderThenFill(casa), run_time=2)
        self.wait(1)

        # Cartório antigo vs Cartório digital (blockchain)
        cartorio_antigo = self.criar_cartorio("Antigo", GREY_D, RED).shift(RIGHT*4 + DOWN*2)

        cartorio_novo = self.criar_cartorio("Blockchain", BLUE_E, GREEN).shift(RIGHT*4 + DOWN*2)

        self.play(FadeIn(cartorio_antigo, shift=DOWN))
        seta1 = Arrow(casa.get_right()+DOWN*0.5, cartorio_antigo.get_left(), color=YELLOW, buff=0.5)
        label1 = Text("Venda tradicional", font_size=28, color=YELLOW).next_to(seta1, UP)
        self.play(
            GrowArrow(seta1),
            Write(label1)
        )
        self.wait(2)
        self.play(FadeOut(cartorio_antigo, seta1, label1))        
        
        self.play(FadeIn(cartorio_novo, shift=UP*0.2))
        self.wait(1)

        # Setas de transferência        
        seta2 = Arrow(casa.get_right()+DOWN*0.5, cartorio_novo.get_left(), color=BLUE_E, buff=0.5)        
        label2 = Text("Registro na Blockchain", font_size=28, color=BLUE_E).next_to(seta2, UP)

        self.play(
            GrowArrow(seta2),
            Write(label2),
            Flash(seta2.get_center(), color=BLUE_E, num_lines=25, flash_radius=1)
        )
        self.wait(2)
        self.play(FadeOut(seta2, label2))

        # Benefícios aparecendo
        beneficios = VGroup(
            Text("Benefícios:",font_size=30, color=BLUE_D),
            Text("✓ Imutável",font_size=28, color=BLUE_D),
            Text("✓ Sem intermediários", font_size=28, color=BLUE_D),
            Text("✓ Transparente", font_size=28, color=BLUE_D),
            Text("✓ Instantâneo", font_size=28, color=BLUE_D),
        ).arrange(DOWN).next_to(cartorio_novo, LEFT*0.2, buff=0.2)

        for beneficio in beneficios:
            self.play(Write(beneficio), run_time=1.8)
        self.wait(4)

        # Final
        self.play(
            FadeOut(titulo, casa, cartorio_novo, beneficios),
            run_time=0.1
        )
        
    def criar_cartorio(self, texto_baixo, cor_retangulo, cor_texto_baixo):
        ret = Rectangle(width=3.2, height=2.4, color=cor_retangulo, fill_opacity=1, stroke_width=4)
        telhado = VGroup(
            Triangle(fill_color=cor_retangulo.darker()).scale(1).next_to(ret, UP, buff=0).shift(LEFT*0.8),
            Triangle(fill_color=cor_retangulo.darker()).scale(1).next_to(ret, UP, buff=0).shift(RIGHT*0.8),
        )
        titulo = Text("Cartório", color=WHITE, font_size=36).move_to(ret.get_center() + UP*0.4)
        subtitulo = Text(texto_baixo, color=cor_texto_baixo, font_size=36, weight=BOLD).move_to(ret.get_center() + DOWN*0.18)

        return VGroup(ret, telhado, titulo, subtitulo)

    # Uso
    #cartorio_antigo = criar_cartorio("Antigo", GREY_D, RED).shift(RIGHT*4 + DOWN*2)
    #cartorio_novo   = criar_cartorio("Blockchain", BLUE_E, GREEN).shift(RIGHT*4 + UP*2)