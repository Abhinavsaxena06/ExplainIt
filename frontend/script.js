async function explainText() {
    const text = document.getElementById("inputText").value;

    if (!text.trim()) {
        alert("Please enter some text");
        return;
    }

    const outputBox = document.getElementById("output");
    outputBox.innerText = "⏳ Thinking...";

    try {
        const response = await fetch("https://explainit-1.onrender.com/explain", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                text: text,
                age: selectedAge
            })
        });

        if (!response.ok) {
            throw new Error("Backend error");
        }

        const data = await response.json();
        outputBox.innerText = data.result;

    } catch (error) {
        console.error(error);
        outputBox.innerText = "❌ Something went wrong. Please try again.";
    }
}
