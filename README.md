
# 🧮🗨️  ChromaDB | Ollama | Docker
### Usar modelos ia locales con ollama para preguntar a tus documentos pdf´s

🚀 [Youtube](https://youtu.be/xTZwhgdj6z4)

¿Qué es una base de datos vectorial? ChromaDB es una base de datos vectorial optimizada para almacenar, indexar y consultar datos en formato vectorial. Las bases de datos vectoriales están diseñadas para manejar datos de alta dimensionalidad, como los vectores generados por modelos de machine learning y procesamiento del lenguaje natural (NLP).

¿Qué es ollama? Ollama es una herramienta que permite ejecutar modelos de lenguaje de inteligencia artificial (IA) localmente en tu computadora, sin necesidad de conectarse a la nube. Está diseñada para facilitar el uso de grandes modelos de IA, como GPT, directamente en dispositivos personales, manteniendo la privacidad y reduciendo la latencia. Ollama simplifica la instalación y el uso de estos modelos a través de una interfaz de línea de comandos. Es útil para desarrolladores y usuarios que desean experimentar con modelos de IA avanzados sin depender de servicios en la nube.

¿Qué es docker y docker-compose? Docker es una plataforma de contenedorización que permite empaquetar aplicaciones y sus dependencias en contenedores ligeros y portátiles, asegurando que funcionen de manera consistente en cualquier entorno. Docker Compose es una herramienta que facilita la definición y gestión de aplicaciones multicontenedor, permitiendo describir la configuración de todos los servicios, redes y volúmenes necesarios en un archivo YAML (docker-compose.yml) y luego desplegarlos juntos con un solo comando.

Para ejecutar esta aplicación es necesario contar con:
* [Docker](https://docs.docker.com/engine/install/)
* [Ollama](https://ollama.com/) 
* [Streamlit](https://streamlit.io/)


## ¿Cómo funciona?
1. Divide documento en pedacitos (o chunks)
2. Crea los embeddings de los pedacitos de texto
3. Guarda los pedacitos y los embeddings en ChromaDB
4. Busca los pedacitos más similares a la pregunta del usuario gracias a los embeddings.
5. Pasa los pedacitos más similares junto a la pregunta al servicio de ollama usando el modelo llama3.1 que generará la respuesta


## Instalación

1. Clone o descargue el repositorio en su máquina local.
2. Instale las bibliotecas requeridas ejecutando el siguiente comando en su terminal (recomiendo un entorno virtual como venv):
    ```bash
    pip install -r requirements.txt
    ```
3. Desplegar ChromaDB usando `docker-compose up -d` en una terminal posicionado en la raiz del proyecto. Esto levantará la base de datos vectorial accesible para la aplicacion desde `http://localhost:8000`. Puedes verificar la api del servicio en `http://localhost:8000/docs` (openapi)
4. Ejecute la aplicación con el siguiente comando:
    ```bash
    streamlit run app.py
    ```
1. Suba un documento a la aplicación.
2. Escriba su pregunta y disfrute de la magia.

## Agradecimientos
Me basé en proyectos de estos dos grandes maestros para crear este útil Frankenstein

- [NechuBM](https://www.youtube.com/@NechuBM)
- [CodingMindsetIO](https://www.youtube.com/@CodingMindsetIO)