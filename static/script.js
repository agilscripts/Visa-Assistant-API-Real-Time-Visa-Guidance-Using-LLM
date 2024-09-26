function askAssistant() {
    const question = document.getElementById("question").value;
    if (!question) return;

    // Display user's message
    const chatMessages = document.getElementById("chatMessages");
    const userMessage = document.createElement("div");
    userMessage.classList.add("chat-message", "user-message");
    userMessage.textContent = "You: " + question;
    chatMessages.appendChild(userMessage);

    // Clear input box
    document.getElementById("question").value = '';

    // Send request to server
    fetch('/ask', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ question: question }),
    })
    .then(response => response.json())
    .then(data => {
        // Create a new div for the assistant's response
        const assistantMessage = document.createElement("div");
        assistantMessage.classList.add("chat-message", "assistant-message");

        // Use innerHTML to parse the response and replace **bold** with <strong>bold</strong>
        let formattedResponse = data.response
            .replace(/\n/g, '<br>')  // Line breaks
            .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');  // Bold text

        assistantMessage.innerHTML = "Assistant: " + formattedResponse;
        chatMessages.appendChild(assistantMessage);

        // Scroll to the bottom of the chat
        chatMessages.scrollTop = chatMessages.scrollHeight;
    })
    .catch(error => {
        console.error('Error:', error);
    });
}