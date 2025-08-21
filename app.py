from flask import Flask, request, jsonify, render_template
from supabase_client import supabase
from services.ollama_service import ask_ollama
from utils.prompts import SYSTEM_PROMPT

app = Flask(__name__)
DEFAULT_MODEL = 'gemma:2b'

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/ask_product', methods=['POST'])
def ask_product():
    user_question = request.json.get('message')
    
    # 1️⃣ Traer productos del inventario desde Supabase
    response = supabase.table("inventory").select("*").execute()
    inventory_data = response.data

    # 2️⃣ Crear el prompt para la IA con productos reales
    products_list = "\n".join(
        [f"{p['product_name']}: {p['description']} (${p['price']}, stock {p['stock']})"
         for p in inventory_data]
    )
    
    prompt = SYSTEM_PROMPT + "\nEstos son los productos disponibles:\n" + products_list + \
             f"\nUsuario pregunta: {user_question}"

    # 3️⃣ Pedir respuesta a la IA
    answer = ask_ollama(prompt, DEFAULT_MODEL, SYSTEM_PROMPT)

    # 4️⃣ Detectar si el usuario quiere comprar un producto
    for product in inventory_data:
        if product['product_name'].lower() in user_question.lower() and "comprar" in user_question.lower():
            return buy_product_internal(product['product_name'])

    return jsonify({"response": answer})


@app.route('/buy_product', methods=['POST'])
def buy_product():
    product_name = request.json.get("product_name")
    return buy_product_internal(product_name)


def buy_product_internal(product_name):
    # Buscar producto en Supabase
    response = supabase.table("inventory").select("*").eq("product_name", product_name).single().execute()
    product = response.data

    if not product:
        return jsonify({"response": f"No encontré el producto {product_name}."})

    if product['stock'] <= 0:
        return jsonify({"response": f"El producto {product_name} está agotado."})

    # Actualizar stock
    supabase.table("inventory").update({"stock": product['stock'] - 1}).eq("id", product['id']).execute()

    return jsonify({"response": f"¡Compra realizada! Te vendí 1 {product_name}. Stock restante: {product['stock'] - 1}."})


@app.route('/info')
def info():
    return render_template('info.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
