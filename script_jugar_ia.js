const FILAS = 6;
const COLUMNAS = 7;
let tablero = Array(FILAS).fill(null).map(() => Array(COLUMNAS).fill('-'));
let juegoTerminado = false;
let esperandoIA = false;

const contenedorTablero = document.getElementById('tablero');
const textoEstado = document.getElementById('estado');
const textoVictoria = document.getElementById('mensaje-victoria');

// Inicializar el tablero en pantalla
function crearTableroGUI() {
    contenedorTablero.innerHTML = '';
    for (let r = 0; r < FILAS; r++) {
        for (let c = 0; c < COLUMNAS; c++) {
            const casilla = document.createElement('div');
            casilla.classList.add('casilla');
            casilla.dataset.col = c;
            casilla.addEventListener('click', () => realizarJugadaHumano(c));
            contenedorTablero.appendChild(casilla);
        }
    }
}

function actualizarGUI() {
    const casillas = document.querySelectorAll('.casilla');
    casillas.forEach((casilla, index) => {
        const r = Math.floor(index / COLUMNAS);
        const c = index % COLUMNAS;
        casilla.className = 'casilla'; // Resetear clases
        if (tablero[r][c] === 'x') casilla.classList.add('humano');
        if (tablero[r][c] === 'o') casilla.classList.add('ia');
    });
}


// Manejar el clic del usuario
async function realizarJugadaHumano(col) {
    // No permitir jugar si el juego terminó o la IA está pensando
    if (juegoTerminado || esperandoIA) return;

    let filaValida = -1;
    for (let r = FILAS - 1; r >= 0; r--) {
        if (tablero[r][col] === '-') {
            filaValida = r;
            break;
        }
    }

    if (filaValida === -1) return;

    // Colocar ficha del humano
    tablero[filaValida][col] = 'x';
    actualizarGUI();

    // Bloquear el tablero mientras piensa la IA
    esperandoIA = true;

    textoEstado.innerText = "La IA está pensando...";
    textoEstado.style.color = "yellow";

    try {
        const respuesta = await fetch("http://127.0.0.1:8000/api/movimiento-ia", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ tablero: tablero })
        });

        const data = await respuesta.json();

        // Colocar ficha de la IA si el juego sigue
        if (data.columna_ia !== undefined && data.columna_ia !== null) {
            for (let r = FILAS - 1; r >= 0; r--) {
                if (tablero[r][data.columna_ia] === '-') {
                    tablero[r][data.columna_ia] = 'o';
                    break;
                }
            }
        }

        // Evaluar si hubo ganador y quien ganó
        procesarEstadoJuego(data.estado);

    } catch (error) {
        console.error("Error conectando con la API:", error);
        textoEstado.innerText = "Error de conexión con la IA";
    } finally {
        // Volver a permitir jugar cuando la IA haya terminado
        esperandoIA = false;
    }
}

//  función exclusiva para gestionar mensajes y finalización del juego
function procesarEstadoJuego(estado) {
    if (estado === "GANA_x") {
        textoEstado.style.display = "none";
        textoVictoria.innerText = "¡Gana el jugador rojo!";
        textoVictoria.style.color = "red";
        textoVictoria.style.display = "block";
        juegoTerminado = true;
        actualizarGUI();
        return true; // Indica que el juego terminó
    } 
    
    if (estado === "GANA_o") {
        textoEstado.style.display = "none";
        textoVictoria.innerText = "¡Gana el jugador amarillo!";
        textoVictoria.style.color = "yellow";
        textoVictoria.style.display = "block";
        juegoTerminado = true;
        actualizarGUI();
        return true;
    } 
    
    if (estado === "EMPATE") {
        textoEstado.style.display = "none";
        textoVictoria.innerText = "¡Empate!";
        textoVictoria.style.color = "#38bdf8";
        textoVictoria.style.display = "block";
        juegoTerminado = true;
        actualizarGUI();
        return true;
    }

    // El juego continúa
    textoEstado.innerText = "Tu turno (Fichas rojas)";
    textoEstado.style.color = "red"
    actualizarGUI();
    return false;
}
function limpiarResultado() {
    textoEstado.style.color = "red"
    textoEstado.style.display = "block";
    textoVictoria.innerText = "";
    
    // Oculta el div para volver a centrar todo al reiniciar
    textoVictoria.style.display = "none"; 
}


function reiniciarJuego() {
    limpiarResultado();
    tablero = Array(FILAS).fill(null).map(() => Array(COLUMNAS).fill('-'));
    juegoTerminado = false;
    textoEstado.innerText = "Tu turno (Fichas rojas)";
    actualizarGUI();
}

crearTableroGUI();
