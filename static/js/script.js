const messageInput = document.getElementById("messageInput");
const sendButton = document.getElementById("sendButton");
const chatArea = document.getElementById("chatArea");


function addMessage(message, sender) {

    const messageDiv = document.createElement("div");

    messageDiv.classList.add("message");

    if (sender === "user") {

        messageDiv.innerHTML = `
            <div class="message-content">
                <strong>You</strong>
                <p>${message}</p>
            </div>
        `;

    } else {

        messageDiv.innerHTML = `
            <div class="avatar">
                🩺
            </div>

            <div class="message-content">
                <strong>MediGuide AI</strong>
                <p>${message}</p>
            </div>
        `;
    }

    chatArea.appendChild(messageDiv);

    chatArea.scrollTop = chatArea.scrollHeight;
}


async function sendMessage() {

    const message = messageInput.value.trim();

    if (message === "") {
        return;
    }

    addMessage(message, "user");

    messageInput.value = "";

    sendButton.disabled = true;
    sendButton.textContent = "Thinking...";


    try {

        const response = await fetch("/api/chat", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                message: message
            })

        });


        const data = await response.json();


                if (data.reply) {

            addMessage(data.reply, "bot");

        } else if (data.error) {

            addMessage(
                "Error: " + data.error,
                "bot"
            );

        } else {

            addMessage(
                "Sorry, I couldn't process your question.",
                "bot"
            );

        }

    } catch (error) {

        console.error(error);

        addMessage(
            "Something went wrong. Please try again.",
            "bot"
        );

    }


    sendButton.disabled = false;
    sendButton.textContent = "Send";
}


sendButton.addEventListener("click", sendMessage);


messageInput.addEventListener("keydown", function(event) {

    if (event.key === "Enter") {
        sendMessage();
    }

});