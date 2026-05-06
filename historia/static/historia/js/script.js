document.addEventListener('DOMContentLoaded', () => {
    const btnComenzar = document.getElementById('btn-comenzar');
    const pantallaInicio = document.getElementById('pantalla-inicio');
    const contenidoPrincipal = document.getElementById('contenido-principal');
    const musica = document.getElementById('musica-fondo');
    const menuPrincipal = document.getElementById('menu-principal');

    function reproducirCancionAleatoria() {
        const indiceAleatorio = Math.floor(Math.random() * nuestraPlaylist.length);
        
        // Le asignamos esa ruta a la etiqueta de audio
        musica.src = nuestraPlaylist[indiceAleatorio];
        
        // Volumen al 50% para que sea música de fondo y no moleste
        musica.volume = 0.2; 
        
        // ¡Play!
        musica.play();
        console.log("Reproduciendo canción número: " + (indiceAleatorio + 1));
    }

    if (btnComenzar) {
        btnComenzar.addEventListener('click', () => {
            console.log("Botón pulsado, iniciando magia...");
            
            if (musica) {
                reproducirCancionAleatoria();
            }
            
            pantallaInicio.classList.add('fade-out');

            setTimeout(() => {
            pantallaInicio.style.display = 'none';
            contenidoPrincipal.classList.remove('seccion-oculta');
            contenidoPrincipal.classList.add('fade-in');
            
            // Mostramos el menú de navegación
            if (menuPrincipal) {
                menuPrincipal.classList.remove('seccion-oculta');
                menuPrincipal.classList.add('fade-in');
            }
            
        }, 800);
        });
    }

    if (musica) {
        musica.addEventListener('ended', reproducirCancionAleatoria);
    }
});