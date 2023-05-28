# Parcial 3 - Big Data e Ingeniería de datos
Este repositorio contiene el código y los recursos necesarios para el Parcial 2, que se enfoca en el procesamiento de datos de noticias y el análisis de acciones utilizando Pyspark ML y AWS Kinesis.

## Estructura del repositorio
El repositorio está estructurado de la siguiente manera:

```
- punto2/
  - periodicos_pipeline.ipynb       # Jupyter Notebook con el procesamiento de datos con pyspark
- punto3/
  - producer_1.py                   # Código del primer productor para enviar datos a Kinesis
  - producer_2.py                   # Código del segundo productor para enviar datos a Kinesis
  - consumer_upper.py               # Código del consumidor para la franja superior de Bollingener
  - consumer_lower.py               # Código del consumidor para la franja inferior de Bollingener
  - test_producer.py                # Pruebas unitarias para el análisis de acciones
  - test_consumers.py               # Pruebas unitarias para el análisis de acciones
- README.md                         # Documentación del proyecto
```

## Procesamiento de datos de noticias
El procesamiento de datos de noticias se realiza utilizando Pyspark ML y se implementa un pipeline de procesamiento que incluye la vectorización de los textos utilizando TF-IDF.

Para ejecutar el procesamiento de datos de noticias, sigue los pasos a continuación:

Configura un entorno de ejecución con Pyspark y ejecuta el Jupyter Notebook procesamiento.ipynb en la carpeta notebooks/.

El notebook guiará el proceso de carga de los datos de noticias desde el archivo data/noticias.csv, realizará el preprocesamiento de los textos, y aplicará la vectorización utilizando TF-IDF. También se incluirán otras transformaciones o pasos necesarios según los requisitos específicos.

Una vez que se haya ejecutado el notebook, los datos procesados estarán listos para su posterior análisis y modelado.

## Análisis de acciones financieras
El análisis de acciones se realiza utilizando Pyspark ML y se implementa un sistema de productores y consumidores utilizando AWS Kinesis para el streaming de datos de acciones.

**Para ejecutar el análisis de acciones, sigue los pasos a continuación:**

Configura una máquina EC2 en AWS y clona este repositorio en la máquina.

Ejecuta el código del primer productor productor1.py en la máquina EC2 para enviar los datos de acciones a un stream en AWS Kinesis. Asegúrate de configurar las credenciales de AWS adecuadas y especificar el nombre del stream correspondiente.

Ejecuta el código del segundo productor productor2.py en la máquina EC2 para enviar los datos de acciones a un stream en AWS Kinesis. Asegúrate de configurar las credenciales de AWS adecuadas y especificar el nombre del stream correspondiente.

Ejecuta el código del consumidor consumidor1.py en la máquina EC2 para recibir los datos del stream de Kinesis y mostrar una alerta cada vez que el precio de alguna acción supere la franja superior de Bollingener.

Ejecuta el código del consumidor consumidor2.py en la máquina EC2 para recibir los datos del stream de Kinesis y mostrar una alerta cada vez que el precio de alguna acción esté por debajo de la franja inferior de Bollingener.

## Pruebas unitarias
Se proporcionan pruebas unitarias en los archivos test_consumers.py y test_producer.py dentro de la carpeta punto3/. Estas pruebas se centran en verificar la funcionalidad del análisis de acciones implementado. Para ejecutar las pruebas, asegúrate de tener las dependencias necesarias instaladas y ejecuta el archivo de pruebas.

## Recursos adicionales
* [Apache Spark MLlib - Pipeline](https://spark.apache.org/docs/latest/ml-pipeline.html)

* [AWS Kinesis Documentation](https://aws.amazon.com/kinesis/)

* [AWS SDK for Python (Boto3) Documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
