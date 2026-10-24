from langchain_openai import ChatOpenAI


def generar_mensaje_motivacional(resumen: dict) -> str:
    """Genera un mensaje corto y motivador según la racha del hábito."""
    estado = "Hoy ya lo cumplió." if resumen["cumplido_hoy"] else "Hoy todavía no lo marca."
    prompt = (
        f"Escribe una frase breve (máximo 15 palabras), en español, con tono "
        f"cercano, divertido y motivador, y con un emoji al final, "
        f"para alguien que lleva {resumen['racha']} días seguidos cumpliendo "
        f"el hábito '{resumen['nombre']}'. {estado} "
        f"No repitas frases típicas como 'sigue así' o 'tú puedes'."
    )
    try:
        llm = ChatOpenAI(model="gpt-4o-mini", temperature=1.0)
        return llm.invoke(prompt).content
    except Exception:
        return "No pude generar el mensaje ahora. Intenta de nuevo más tarde."