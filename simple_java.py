from code_video import CodeScene
from tts import local_tts


class MyScene(CodeScene):
    def construct(self):
        # La contrucción de la escena va aquí
        # path,length = local_tts("Hola, bienvenidos a la clase de programación orientada a objetos en Java. En esta clase vamos a aprender sobre la creación de clases y objetos en Java. Para ello, vamos a crear una clase llamada Publicacion que representará una publicación en una red social. La clase Publicacion tendrá dos atributos: un String llamado contenido y un String llamado autor. Además, la clase Publicacion tendrá un método llamado mostrar que mostrará el contenido y el autor de la publicación. Ahora, vamos a ver cómo se implementa la clase Publicacion en Java.")
        # print(path, length)
        self.animate_code_comments("examples/Publicacion.java",keep_comments=True, start_line=7, end_line=10)

        # Espera 5 segundos antes de terminar 
        self.wait(5)
