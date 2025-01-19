import os
import subprocess

def clonar_repositorios(lista_repositorios, directorio_destino="repositorios"):
    """
    Clona una lista de repositorios Git.

    Args:
        lista_repositorios: Una lista de URLs de repositorios.
        directorio_destino: El directorio donde se clonarán los repositorios.
    """

    if not os.path.exists(directorio_destino):
        os.makedirs(directorio_destino)

    for repo_url in lista_repositorios:
        try:
            nombre_repo = repo_url.split("/")[-1].split(".")[0]  # Extrae el nombre del repo
            ruta_destino = os.path.join(directorio_destino, nombre_repo)

            if os.path.exists(ruta_destino):
                print(f"El repositorio {nombre_repo} ya existe. Omitiendo.")
                continue

            print(f"Clonando {repo_url} en {ruta_destino}...")
            subprocess.run(["git", "clone", repo_url, ruta_destino], check=True)
            print(f"Repositorio {nombre_repo} clonado exitosamente.")

        except subprocess.CalledProcessError as e:
            print(f"Error al clonar {repo_url}: {e}")
        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")

# Ejemplo de uso:
repositorios_a_clonar = [
    "https://github.com/JaimeVelascoG/gh-actions-controlling-workflows.git",
    "https://github.com/JaimeVelascoG/gh-actions-env-vars.git",
    "https://github.com/JaimeVelascoG/gh-actions-data.git",
    "https://github.com/JaimeVelascoG/gh-actions-demo2.git"

    # ... más repositorios
]

clonar_repositorios(repositorios_a_clonar)
#clonar_repositorios(repositorios_a_clonar, "otros_repos") # Clonar en otro directorio