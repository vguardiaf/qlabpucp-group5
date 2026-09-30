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