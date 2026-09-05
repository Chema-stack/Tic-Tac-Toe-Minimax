const FILAS = 6;
const COLUMNAS = 7;
let tablero = Array(FILAS).fill(null).map(() => Array(COLUMNAS).fill('-'));
let juegoTerminado = false;

const contenedorTablero = document.getElementById('tablero');
const textoEstado = document.getElementById('estado');

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
    if (juegoTerminado) return;

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

    textoEstado.innerText = "La IA está pensando...";
    textoEstado.style.color = "yellow"
    
    try {
        const respuesta = await fetch("http://127.0.0.1:8000/api/movimiento-ia", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ tablero: tablero })
        });

        const data = await respuesta.json();
        
        

        // 2. Colocar ficha de la IA si el juego sigue
        if (data.columna_ia !== undefined && data.columna_ia !== null) {
            for (let r = FILAS - 1; r >= 0; r--) {
                if (tablero[r][data.columna_ia] === '-') {
                    tablero[r][data.columna_ia] = 'o';
                    break;
                }
            }
        }

        // 3. Evaluar si hubo ganador y quien gano
        procesarEstadoJuego(data.estado);

    } catch (error) {
        console.error("Error conectando con la API:", error);
        textoEstado.innerText = "Error de conexión con la IA";
    }
}

//  función exclusiva para gestionar mensajes y finalización del juego
function procesarEstadoJuego(estado) {
    console.log(estado);
    if (estado === "GANA_x") {
        console.log(estado);
        textoEstado.innerText = "¡Gana el jugador rojo!";
        juegoTerminado = true;
        actualizarGUI();
        return true; // Indica que el juego terminó
    } 
    
    if (estado === "GANA_o") {
        textoEstado.innerText = "¡Gana el jugador amarillo!";
        juegoTerminado = true;
        actualizarGUI();
        return true;
    } 
    
    if (estado === "EMPATE") {
        textoEstado.innerText = "¡Empate!";
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


function reiniciarJuego() {
    tablero = Array(FILAS).fill(null).map(() => Array(COLUMNAS).fill('-'));
    juegoTerminado = false;
    textoEstado.innerText = "Tu turno (Fichas rojas)";
    actualizarGUI();
}

crearTableroGUI();
