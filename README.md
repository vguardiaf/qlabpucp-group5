# qlabpucp-assignment1-group5
# Assignment 2 - Scraping, APIs y Cruce por Ubigeo 

## Pregunta del trabajo

¿El Estado declara emergencia donde más llueve?

Cada temporada de lluvias, la Presidencia del Consejo de Ministros (PCM) publica decretos supremos que declaran el Estado de Emergencia en distritos afectados por lluvias intensas. En este trabajo van a reunir esos decretos, medir cuánto llovió en cada departamento y cruzar ambas fuentes por ubigeo para responder la pregunta.

## Temporada asignada

1 de enero al 31 de mayo de 2022

## Precisiones 

- `assignment_1/` no se toca.
- Todo el trabajo se hace en VS Code, con commits y pushes desde GitHub Desktop (o Git).

## Issues como espacio de coordinación

- Hay un Issue por parte.
- En los Issues se discute, se preguntan dudas, se reportan avances y se anota cuándo termina la parte.
- **No se escribe código en los Issues.** El código va en el notebook `.ipynb` correspondiente.
- Cuando la parte está terminada y revisada, el responsable cierra el Issue.

## Orden de trabajo

1. **Partes 1 y 2 en paralelo.** No dependen una de la otra.
   - La Parte 1 produce `decretos_lluvias.csv` y `decretos_por_departamento.csv`.
   - La Parte 2 produce `lluvias_por_departamento.csv`.
2. **Parte 3.** Empieza cuando ya existen los CSV de las Partes 1 y 2. Mientras tanto, se puede avanzar con `ubigeos.csv` y la lectura con `dtype`.
3. **Parte 4 durante todo el proceso.** Cada vez que la IA dé algo incorrecto, incompleto o que no funcione, se anota en el momento en `bitacora_ia.md` (qué se pidió, qué respondió, qué estaba mal, cómo se corrigió). No se deja para el final.

## Commits y participación
- Cada integrante hace sus propios commits y pushes en sus **branches**, con mensajes claros (por ejemplo: `Parte 1: extracción de decretos de enero`).
- Antes de empezar a trabajar: **Pull / Fetch** para traer los cambios del grupo.
- Antes de subir: **Pull** otra vez, para evitar conflictos.
- La participación se verifica en los Issues y en el historial de commits, así que todos deben tener evidencia visible.

## Uso de IA
- Se puede usar Claude, OpenCode (Muse) u otra herramienta.
- Nada se acepta sin revisar: se comprueban los datos, se ejecutan las verificaciones pedidas y se explican las decisiones en celdas de texto.
- Todo error de la IA se registra en la bitácora.

## Revisión antes de cerrar cada parte
- El notebook corre de principio a fin sin errores y se entrega **ejecutado**, con todos los resultados visibles.
- Se cumplieron las verificaciones de esa parte.
- Las decisiones están explicadas en celdas de texto.
- Los archivos CSV están guardados en `datos/`.
- Otro integrante revisó el notebook antes de cerrar el Issue.

---------------------------------------------------------------------------

# Assignment 1 – Lists, Tuples, Dictionaries, and NumPy

Trabajo grupal del curso Fundamentos de Python (Grupo 5). Todo el desarrollo se realiza en este repositorio, con un notebook por cada parte.

## Estado inicial del repositorio

Los archivos **ya están creados** en la carpeta `assignment_1/`. No es necesario crear nuevos notebooks, solo completar el que te corresponde:

```
assignment_1/
├── lists.ipynb
├── tuples.ipynb
├── dictionaries.ipynb
└── numpy.ipynb
```

## Responsables

| Parte | Notebook | Responsable | Issue |
|---|---|---|---|
| Part 1 – Lists | `lists.ipynb` | @alvarorubencarhuamac  | #1 |
| Part 2 – Tuples | `tuples.ipynb` | @Ozymandias007 | #2 |
| Part 3 – Dictionaries | `dictionaries.ipynb` | @vguardiaf | #3 |
| Part 4 – NumPy | `numpy.ipynb` | @O-Chavx | #4 |

## Cómo trabajar
 1. Clonar el repositorio en GitHub Desktop
 2. Crear tu propia rama (branch)
 3. Trabajar solo en tu notebook
- Edita únicamente el notebook que te corresponde, para evitar conflictos.
- Sigue las instrucciones de tu parte en el orden indicado en el enunciado.
 4. Commits y push
 5. Abrir un Pull Request
 - Cuando termines, abre un Pull Request de tu rama hacia `main`. En la descripción escribe el número de tu Issue para que se cierre automáticamente al fusionarse.

## Comunicación: todo a través de Issues

- Comenta en el Issue de tu parte para reportar avances o hacer preguntas.
- **No escribas código dentro de los Issues.** El código va únicamente en los notebooks.
- Los Issues se cierran cuando la parte correspondiente está completada y fusionada.
