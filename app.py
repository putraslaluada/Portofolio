

from flask import Flask, render_template, request, jsonify
import random
import time

app = Flask(__name__)

# Struktur respons baru, mudah ditambah
AI_RESPONSES = {
    "hai": ["Halo! Ada yang bisa saya bantu?", "Hai juga!"],
    "halo": ["Halo! Selamat datang di Neoput Assistant."],
    "nama kamu": ["Nama saya Neoput Assistant."],
    "siapa kamu": ["Saya adalah AI asisten digital yang siap membantu kamu."],
    "terima kasih": ["Sama-sama!", "Senang bisa membantu.", "Kapan saja!"],
    "fitur": ["Saya bisa menjawab pertanyaan, membantu tugas, dan ngobrol santai!"],
    "bisa apa": ["Saya bisa membantu analisis data, ide kreatif, dan support 24/7!"],
    "ai itu apa": ["AI adalah kecerdasan buatan yang bisa belajar dan membantu manusia."],
    # Tanya jawab tentang M.Putra Nur Firdaus
    "putra nur firdaus": [
        "M.Putra Nur Firdaus adalah seorang Full Stack Developer dengan pengalaman lebih dari 5 tahun.",
        "Beliau ahli dalam pengembangan aplikasi web modern dan solusi digital inovatif.",
        "Keahlian utama: HTML5, CSS3, JavaScript, Python, Networking, Bisnis Digital, Service Hardware.",
        "M.Putra Nur Firdaus juga suka mendaki gunung dan membaca buku desain produk.",
        "Portofolio lengkap bisa dilihat di halaman profile."],
    "siapa putra nur firdaus": [
        "Dia adalah seorang pelajar dari Gunung Sindur, Bogor, yang bersekolah di SMKN 1 Gunung Sindur dan memiliki minat serta bakat di bidang teknologi.",
        "Putra Nur Firdaus adalah pelajar berbakat dari Gunung Sindur, Bogor, yang bersekolah di SMKN 1 Gunung Sindur dan sangat tertarik dengan dunia teknologi."],
    "siapa yang menciptakan kamu": [
        "Putra Nur Firdaus yang menciptakan saya."],
    "keahlian putra nur firdaus": [
        "Keahlian utama: HTML5, CSS3, JavaScript, Python, Networking, Bisnis Digital, Service Hardware."],
    "pengalaman putra nur firdaus": [
        "Pengalaman lebih dari 5 tahun di bidang pengembangan web dan aplikasi digital."],
    "kontak putra nur firdaus": [
        "Bisa dihubungi via WhatsApp: 6289530929113, email: hello@portofolio.dev, atau media sosial di profile."],
    "hobi putra nur firdaus": [
        "Hobi beliau adalah mendaki gunung, membaca buku desain produk, dan eksplorasi teknologi baru."]
}

def get_ai_reply(user_input):
    user_input = user_input.lower()
    for key in sorted(AI_RESPONSES, key=len, reverse=True):
        if key in user_input:
            return random.choice(AI_RESPONSES[key])
    # fallback jika tidak dikenali
    return "Maaf, saya belum paham pertanyaan itu. Coba tanya yang lain!"

@app.route('/')
def index():
    return render_template('index.html')  # Flask otomatis cari di folder 'templates'

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_msg = data.get('msg', '')
    time.sleep(1)  # efek mengetik
    reply = get_ai_reply(user_msg)
    return jsonify({'reply': reply})

if __name__ == '__main__':
    app.run(debug=True)