public abstract class Publicacion {
    public abstract void publicar();
}

public class Libro extends Publicacion {
    @Override
    // Este es un ejemplo de un comentario en java
    public void publicar() {
        System.out.println("Publicando un libro");
    }
}