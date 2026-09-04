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

    // Buscar la primera casilla libre desde abajo (gravedad)
    let filaValida = -1;
    for (let r = FILAS - 1; r >= 0; r--) {
        if (tablero[r][col] === '-') {
            filaValida = r;
            break;
        }
    }

    if (filaValida === -1) return; // Columna llena

    // Aplicar la ficha 'x' del humano
    tablero[filaValida][col] = 'x';
    actualizarGUI();

    // Turno de la IA: Llamar a FastAPI
    textoEstado.innerText = "La IA está pensando...";
    
    try {
        const respuesta = await fetch("http://127.0.0.1:8000/api/app.py", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ tablero: tablero, columna_jugador: col })
        });

        const data = await respuesta.json();
        const colIA = data.columna;

        // Aplicar la ficha 'o' de la IA en la columna recibida
        for (let r = FILAS - 1; r >= 0; r--) {
            if (tablero[r][colIA] === '-') {
                tablero[r][colIA] = 'o';
                break;
            }
        }
        
        actualizarGUI();
        textoEstado.innerText = "Tu turno (Fichas rojas)";

    } catch (error) {
        console.error("Error conectando con la API:", error);
        textoEstado.innerText = "Error de conexión con la IA";
    }
}

function reiniciarJuego() {
    tablero = Array(FILAS).fill(null).map(() => Array(COLUMNAS).fill('-'));
    juegoTerminado = false;
    textoEstado.innerText = "Tu turno (Fichas rojas)";
    actualizarGUI();
}

crearTableroGUI();
