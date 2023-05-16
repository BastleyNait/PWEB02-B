const fecha = new Date();
const dia = fecha.getDay();

function diaSemana (num) {
    const semana = {
    0 : "Domingo",
    1 : "Lunes",
    2 : "Martes",
    3 : "Miercoles",
    4 : "Jueves",
    5 : "Viernes",
    6 : "Sabado",
    }
    return semana[num];
}

console.log(diaSemana(dia));
