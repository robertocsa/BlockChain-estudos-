# assinatura_blockchain.py
# manim -pqh assinatura_blockchain.py AssinaturaBlockchain

# assinatura_simples.py
# Versão 100% limpa, conceitual e sem erros (Manim 2025)

from manim import *

class AssinaturaSimples(Scene):
    def construct(self):
        # Cores personalizadas
        CYAN = "#00FFFF"
        AZUL_ESCURO = "#0f172a"  # azul-escuro
        DARK_RED = "#A10003"
        GREEN_RCS = "#20FF88"
        
        # ==================== CONFIGURAÇÃO VERTICAL 1080x1080 ====================
        self.camera.background_color = AZUL_ESCURO
        self.camera.frame_width = 26.0
        self.camera.frame_height = 16.0 
        
        # ==================== 1. O que é uma assinatura digital? ====================
        titulo = Tex(r"\textbf{Assinatura Digital na Blockchain}", font_size=64, color=BLUE)
        explicacao = Tex(r"Prova que \\ \textbf{você} escreveu a mensagem \\ e que \textbf{ninguém mudou nada depois}", 
                        font_size=48)
        explicacao.next_to(titulo, DOWN, buff=1)

        self.play(Write(titulo), run_time=2)
        self.wait(1)
        self.play(Write(explicacao), run_time=4)
        self.wait(6)
        self.play(FadeOut(titulo, explicacao))

        # ==================== 2. As duas chaves (o coração de tudo) ====================
        linha1 = Tex(r"Você tem \textbf{duas chaves} que são um par perfeito:", font_size=50)
        priv = Tex(r"• Chave PRIVADA $\to$ seu segredo absoluto", color=RED, font_size=48)
        pub  = Tex(r"• Chave PÚBLICA $\to$ você pode compartilhar publicamente", color=GREEN_D, font_size=48)
        
        VGroup(linha1, priv, pub).arrange(DOWN, aligned_edge=LEFT, buff=0.6).shift(UP*0.5)

        self.play(Write(linha1))
        self.wait(2)
        self.play(Write(priv))
        self.wait(3)
        self.play(Write(pub))
        self.wait(5)

        magia = Tex(r"A mágica: \\ só a chave privada consegue assinar \\ mas \textbf{qualquer pessoa} verifica com a chave pública", 
                    font_size=52, color=YELLOW)
        magia.next_to(pub, DOWN, buff=1.2)

        self.play(Write(magia), run_time=5)
        self.wait(8)
        self.play(FadeOut(*self.mobjects))

        # ==================== 3. Como funciona na prática (passo a passo) ====================
        passos = VGroup(
            Tex(r"1. Você escreve uma mensagem ou transação", font_size=48),
            Tex(r"2. O computador tira a ``impressão digital'' da mensagem (chamada HASH)", font_size=48),
            Tex(r"3. Você ``tranca'' o HASH com sua chave privada $\to$ nasce a ASSINATURA", font_size=48),
            Tex(r"4. Você envia: mensagem + assinatura + sua chave pública", font_size=48),
            Tex(r"5. Qualquer pessoa no mundo faz o cálculo ao contrário com a chave pública", font_size=48),
            Tex(r"6. Se o resultado bater com a impressão digital da mensagem $\to$ tudo certo!", font_size=48),
            Tex(r"   Se não bater $\to$ alguém mexeu ou não foi você que assinou", font_size=48),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.45)

        self.play(LaggedStart(*[Write(p) for p in passos], lag_ratio=0.9), run_time=12)
        self.wait(10)

        self.play(FadeOut(passos))

        # ==================== 4. Por que é impossível falsificar ====================
        por_que = Tex(r"Por que ninguém consegue falsificar?", font_size=64, color=ORANGE)
        por_que.shift(UP*7.6)
        self.play(Write(por_que))
        self.wait(2)

        motivos = VGroup(
            Tex(r"• Sem a chave privada é \textbf{matematicamente impossível} criar uma assinatura válida", font_size=46),
            Tex(r"• Se alguém mudar \textbf{uma única letra} ou um espaço, o hash muda completamente", font_size=46),
            Tex(r"• A verificação falha imediatamente $\to$ a blockchain rejeita na hora", font_size=46),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.7)
        motivos.next_to(por_que, DOWN, buff=0.8)

        self.play(Write(motivos[0]), run_time=3)
        self.wait(3)
        self.play(Write(motivos[1]), run_time=3)
        self.wait(3)
        self.play(Write(motivos[2]), run_time=3)
        self.wait(6)

        # ==================== 5. Exemplo mínimo com números (só para ver que funciona) ====================
        self.play(FadeOut(por_que, motivos))

        exemplo = Tex(r"Vamos ver com números bem pequenos (na vida real são gigantes)", font_size=50)
        exemplo.shift(UP*7.6)
        self.play(Write(exemplo))
        self.wait(3)

        tabela = VGroup(
            Tex(r"Mensagem correta: ``RCSantos Scripts'' $\to$ hash simplificado = 47", font_size=44),
            Tex(r"Você assina com chave privada $\to$ assinatura = 91", font_size=44),
            Tex(r"Todo mundo verifica com chave pública $\to$ 91 vira novamente 47 $\to$ OK", color=GREEN_RCS, font_size=44),
            Tex(r"-------------------------------------------------------------------", font_size=44),  # linha em branco
            Tex(r"Mensagem alterada: ``RCSantos ScriptS'' $\to$ hash vira 61", color=RED, font_size=44),
            Tex(r"Verificação com a mesma assinatura 91 $\to$ dá 47 (não 61) $\to$ REJEITADO", color=RED, font_size=44),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        tabela.next_to(exemplo, DOWN, buff=0.8)

        self.play(FadeIn(tabela, shift=UP), run_time=4)
        self.wait(12)

        # ==================== 6. Conclusão ====================
        self.play(FadeOut(exemplo, tabela))

        final = VGroup(
            Tex(r"Resumo em uma frase:", font_size=60),
            Tex(r"``Você tranca com o segredo. \\ O mundo abre com a chave pública.''", font_size=64, color=YELLOW),
            Tex(r"Se abrir e estiver tudo certo $\to$ foi você e ninguém mudou nada.", font_size=52),
            Tex(r"É exatamente assim que \\ \textbf{todas as blockchains} funcionam.", 
                font_size=56, color=BLUE)
        ).arrange(DOWN, buff=0.8)
        final.shift(UP*4)

        self.play(Write(final[0]))
        self.wait(2)
        self.play(Write(final[1]), run_time=4)
        self.wait(4)
        self.play(Write(final[2]))
        self.wait(4)
        self.play(Write(final[3]), run_time=5)
        self.wait(10)

        self.play(FadeOut(final))