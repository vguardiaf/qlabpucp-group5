# PARTE 1 - Bitácora de Uso de IA - scraping_emergencias.ipynb

## Registro de interacciones y errores corregidos con apoyo de la IA

Durante el desarrollo de la Parte 1 se utilizó la IA como herramienta de apoyo en momentos puntuales para revisar el código, identificar errores de ejecución y verificar que los procedimientos realizados cumplieran con las indicaciones del trabajo.

1. Consulta sobre la organización del procedimiento de scraping de los decretos de emergencia publicados por la PCM entre enero y mayo de 2022. La IA brindó orientación para organizar los resultados mensuales y verificar la cantidad de registros obtenidos.

2. Consulta sobre un error relacionado con el nombre de una variable. La IA propuso inicialmente utilizar `df_decretos_original`, pero esta variable no existía en el notebook. Se revisaron las variables disponibles para identificar el DataFrame que realmente correspondía utilizar.

3. Consulta sobre la recuperación de los títulos completos de las normas. Se revisó el uso de `requests` y `BeautifulSoup`, así como la incorporación de una pausa de un segundo entre solicitudes.

4. Consulta sobre la clasificación de las normas mediante palabras clave. Se revisó la creación de las variables `es_lluvia`, `tipo` y `motivo`, así como los registros que quedaron clasificados como `"otro"`.

5. Consulta sobre la exportación de los resultados. Se revisó la estructura de los archivos `decretos_lluvias.csv` y `decretos_por_departamento.csv` para comprobar que contuvieran las columnas solicitadas en las instrucciones.

## Momentos en que la IA dio algo incorrecto, incompleto o que no funcionó

1. Se solicitó apoyo para revisar la clasificación de las normas obtenidas mediante el scraping, utilizando el título completo para identificar si estaban relacionadas con lluvias y determinar su tipo y motivo. La IA sugirió realizar la clasificación mediante palabras clave como "lluvia", "precipitaciones", "prórroga", "declara", "peligro inminente" e "impacto de daños".
Al revisar los resultados obtenidos se observó que 22 registros presentaban al menos una clasificación como "otro". La explicación inicial de la IA resultó incompleta, ya que podía interpretarse que estos casos correspondían a registros que no habían podido clasificarse adecuadamente. Por ello, se revisaron manualmente algunos de los títulos y se comprobó que varios simplemente no contenían de forma literal las expresiones establecidas como criterio de clasificación.
Para resolverlo, se mantuvieron los criterios definidos en las instrucciones del trabajo y se utilizó el título completo recuperado de cada norma en minúsculas. Además, se revisaron los casos clasificados como "otro" y se incorporó una explicación en el notebook indicando que esta categoría responde a la ausencia de las palabras establecidas en el título y no necesariamente a un error en el scraping.

2. Se solicitó apoyo para identificar automáticamente los departamentos mencionados en los títulos de las normas relacionadas con lluvias. La IA sugirió inicialmente buscar el nombre de cada departamento directamente dentro del texto mediante coincidencias de cadenas.
Al revisar este procedimiento se identificó que una búsqueda simple podía producir coincidencias parciales incorrectas. Por ejemplo, buscar "Ica" únicamente con una condición de pertenencia podía identificar esa secuencia dentro de nombres más largos como "Huancavelica". Asimismo, si un departamento aparecía más de una vez dentro del título, existía el riesgo de contabilizarlo más de una vez.
Para resolverlo se mejoró el procedimiento utilizando expresiones regulares y límites de palabra con re.search(r"\b" + re.escape(departamento) + r"\b", titulo), trabajando sobre el título original para respetar los nombres de los departamentos. Finalmente, al aplicar el procedimiento al Decreto Supremo N.° 032-2022-PCM se identificaron correctamente los departamentos de Amazonas, Ayacucho y Piura, sin generar coincidencias parciales ni duplicados.

# PARTE 2 - Bitácora de Uso de IA - api_lluvias.ipynb

## Registro de interacciones y errores humanos corregidos por la IA. 

1. Consulta sobre Error: ImportError: Import lxml failed. Claude Code indicó que pd.read_html requiere el paquete "lxml", para ello debía instalar con pip install lxml.

2. Consulta sobre error en código para acceder a la url de Wikipedia. Claude Code indicó que faltaba import io y el request.get se había escrito directo sin definir la variable "respuesta". 

3. Consulta sobre incorporar las columnas a obtener en los params del código de acceso a la url de Wikipedia. Claude Code indicó que Wikipedia no era un API y no lee params, que las columnas se eligen después. 

4. Consulta de código para obtener solo las columnas de "departamento" y "capital" de la tabla[1] obtenida de Wikipedia. Claude Code brindó el código explicando el df[["departamento","capital"]].copy() -> doble corchete selecciona varias columnas.

5. Consulta de código manual para incorporar Callao, ya que tabla[3] era compleja. Inicialmente se agregó solo el siguiente código: df.loc[len(df)] = ["Callao","Callao"]. Claude Code explicó que ese código agregaba filas con Callao cada vez que se ejecutaba. Corrigió el código con el if "Callao" not in df.

6. Consulta sobre código para obtener latitud y longitud de las 25 capitales. Inicialmente el código escrito solo obtenía los valores de la última fila type(df) = dict y len(df) = 2. Claude Code definió la aplicación de los parámetros en bucle. Luego brindó código para merge con df base. Y finalmente indicó que el request.get estaba fuera del for.

7. Consulta sobre código para obtener lluvia diaria por capital. Claude Code definió código de búsqueda en bucle y parámetros, pero para el periodo 2023 y estableció el time.sleep en 0.5. Se corrigió la fecha al 2022 y el tiempo de espera a 1 seg.  

8. Consulta de código para calcular suma de lluvia por departamento. Agregó al código as_index=False y la definición de la variable "lluvia_mm". Después de correr habían y hacer el export a csv habían muchos valores con varios decimales, por lo que se agregó el round(1). 

9. Consulta sobre el código para calcular días con más de 20 mm por departamento. Claude Code brindó el código. Inicialmente cambié el nombre de la columna en assign pero no en grouby, generando un error. Claude ayudó a identificar y corregir el error. 

10. Consulta sobre código para unificar las tres tablas. Se intentó unificar las tres en un solo merge de la siguiente manera df = df.merge(tabla1, tabla2, on="departamento", how="left"). Claude Code explicó que la tabla2 es tomada como argumento how y eso genera un error, indicó que se debían encadenar dos merge. 

11. Consulta sobre exportación de archivos a formato csv. Al exportar y aplicar la tabulación con separador coma, se eliminaban los decimales de las latitudes, longitudes y lluvia total en mm. Claude Code indicó código para definir sep=";", y decimal=".".

## Momentos que la IA dio algo incorrecto, incompleto o que no funcionó

1. Se solicitó el código para exportar la tabla correctamente en formato csv. Claude Code brindó el siguiente código: 

    df.to_csv(lluvias_por_departamento.csv", index=False, encoding="utf-8-sig")

    Sin embargo, cuando se exportó el documento en csv, se notaron dos cosas: 1. Los valores no estaban redondeados y los valores se mostraban como números sin decimal (ejemplo: 39e16 en vez de 39.2). 2. Al convertir el texto en columnas se iban los decimales de lat y long. 

    Para resolver el problema del redondeo se verificó que por ejemplo Lima tenía un valor de 39.19999999999996 producto de la suma de sus valores diarios de lluvia. Se aplicó la función round() a un decimal. 

    Para resolver el problema de los separadores se mejoró el código incorporando los criterios sep=";" y decimal=".".  