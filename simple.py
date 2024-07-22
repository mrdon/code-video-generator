from code_video import CodeScene


class MyScene(CodeScene):
    def construct(self):
        # La contrucción de la escena va aquí
        self.animate_code_comments("examples/simple.py")

        # Espera 5 segundos antes de terminar 
        self.wait(5)
