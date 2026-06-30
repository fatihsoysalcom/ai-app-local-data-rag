import re

# 1. Your proprietary data source - this is the "defensible" part.
# This data is unique to your application and provides core value.
PRODUCT_DATABASE = {
    "Akıllı Saat X1": {
        "description": "Gelişmiş sağlık takibi, uzun pil ömrü ve şık tasarımıyla öne çıkan akıllı saat.",
        "features": ["Nabız ölçer", "Uyku takibi", "GPS", "Su geçirmez", "10 gün pil ömrü"],
        "price": "2500 TL"
    },
    "Kablosuz Kulaklık Y2": {
        "description": "Yüksek ses kalitesi, aktif gürültü engelleme ve ergonomik tasarımıyla müzik keyfini ikiye katlar.",
        "features": ["Aktif Gürültü Engelleme", "Bluetooth 5.2", "24 saat pil ömrü (şarj kutusuyla)", "Dokunmatik kontroller"],
        "price": "1800 TL"
    },
    "Robot Süpürge Z3": {
        "description": "Akıllı navigasyon, güçlü emiş gücü ve mobil uygulama kontrolü ile ev temizliğini kolaylaştırır.",
        "features": ["Lidar Navigasyon", "Otomatik şarj", "Halı algılama", "Mobil uygulama kontrolü"],
        "price": "4500 TL"
    }
}

def retrieve_product_info(query: str) -> str:
    """
    Simulates retrieving relevant product information from a proprietary database
    based on keywords in the query. This is your custom business logic,
    adding unique value beyond a simple LLM wrapper.
    """
    query_lower = query.lower()
    found_info = []
    
    for product_name, details in PRODUCT_DATABASE.items():
        # Simple keyword matching for demonstration
        if re.search(r'\b' + re.escape(product_name.lower().replace(' ', r'\s*')) + r'\b', query_lower) or \
           any(keyword in query_lower for keyword in [product_name.lower(), details["description"].lower()]):
            
            info = f"Ürün Adı: {product_name}\n" \
                   f"Açıklama: {details['description']}\n" \
                   f"Özellikler: {', '.join(details['features'])}\n" \
                   f"Fiyat: {details['price']}\n"
            found_info.append(info)
            # For simplicity, return the first matching product's info.
            # A real RAG system would rank, combine, or chunk results.
            return "\n---\n".join(found_info)
            
    return ""

def simulate_llm_response(user_query: str, context: str) -> str:
    """
    Simulates an LLM generating a response. This function demonstrates how
    the LLM (if it were real) would prioritize and use the provided 'context'
    (your proprietary data) to formulate its answer.
    """
    if context:
        # The LLM uses the provided context to answer, making the application
        # less dependent on the LLM's internal knowledge and more on your curated data.
        response = f"İşte sorduğunuz ürün hakkında bilgi:\n\n{context}\n\n" \
                   f"Başka bir sorunuz varsa lütfen çekinmeyin."
        if "fiyat" in user_query.lower() and "Fiyat:" in context:
            price_match = re.search(r"Fiyat: (.*)", context)
            if price_match:
                response += f"\nÖzellikle fiyatını merak ettiğiniz için belirtmek isterim: {price_match.group(1)}."
        elif "özellik" in user_query.lower() and "Özellikler:" in context:
            features_match = re.search(r"Özellikler: (.*)", context)
            if features_match:
                response += f"\nBaşlıca özellikleri şunlardır: {features_match.group(1)}."
    else:
        response = "Üzgünüm, bu konuda özel bir bilgi bulamadım. Belki başka bir ürün hakkında yardımcı olabilirim?"
    
    return response

def ask_ai_product_assistant(query: str) -> str:
    """
    The main function orchestrating the "defensible AI application".
    It combines proprietary data retrieval with a simulated LLM interaction.
    """
    # 2. Your custom logic to retrieve relevant data based on the user's query.
    # This step is crucial for making the application "defensible" as it leverages
    # your unique data and retrieval strategy.
    retrieved_context = retrieve_product_info(query) 
    
    # 3. The LLM (simulated here) then uses this context to generate a response.
    # The LLM acts as a sophisticated text generator, but the core informational
    # value comes from the context you provide, not its general knowledge.
    llm_output = simulate_llm_response(query, retrieved_context)
    
    return llm_output

if __name__ == "__main__":
    print("Yapay Zeka Ürün Asistanına Hoş Geldiniz!")
    print("Çıkmak için 'çıkış' yazın.")
    
    while True:
        user_input = input("\nSorunuz: ")
        if user_input.lower() == "çıkış":
            print("Güle güle!")
            break
        
        response = ask_ai_product_assistant(user_input)
        print(f"Asistan: {response}")
