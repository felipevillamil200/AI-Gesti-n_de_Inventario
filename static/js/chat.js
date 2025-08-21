window.chatApp = function() {
    return {
        message: '',
        messages: [],
        selectedModel: 'gemma:2b',
        loading: false,
        secondsElapsed: 0,
        timer: null,

        startTimer() {
            this.secondsElapsed = 0;
            this.timer = setInterval(() => { this.secondsElapsed++ }, 1000);
        },

        stopTimer() {
            clearInterval(this.timer);
            this.timer = null;
        },

        scrollToBottom() {
            this.$nextTick(() => {
                const container = this.$refs.chatContainer;
                container.scrollTop = container.scrollHeight;
            });
        },

        sendMessage() {
            if (!this.message.trim()) return;

            // Agregar mensaje del usuario
            this.messages.push({ id: Date.now(), text: this.message, type: 'user' });
            const userMessage = this.message;
            this.message = '';

            // Mostrar indicador de carga
            this.loading = true;
            this.startTimer();

            // Llamada al backend
            fetch('/chat', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ message: userMessage, model: this.selectedModel })
            })
            .then(res => res.json())
            .then(data => {
                this.messages.push({ id: Date.now() + 1, text: data.response, type: 'bot' });
                this.scrollToBottom();
            })
            .catch(() => {
                this.messages.push({ id: Date.now() + 2, text: "Error al enviar el mensaje.", type: 'bot' });
                this.scrollToBottom();
            })
            .finally(() => {
                this.loading = false;
                this.stopTimer();
            });

            this.scrollToBottom();
        }
    }
}
