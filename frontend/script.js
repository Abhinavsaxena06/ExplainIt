async function explainText() {
    const textarea = document.getElementById("inputText");
    const output = document.getElementById("output");
    const text = textarea.value.trim();

    if (!text) {
        alert("Please enter some text");
        return;
    }

    output.innerText = "🤖 Thinking... Please wait";

    /* 🎬 CINEMATIC SCROLL (SLOW + BUTTERY) */
    let isScrolling = false;

    const cinematicScrollToCenter = (element, duration = 1600) => {
        if (isScrolling) return;
        isScrolling = true;

        const rect = element.getBoundingClientRect();
        const targetY =
            rect.top + window.pageYOffset - (window.innerHeight / 2) + (rect.height / 2);

        const startY = window.pageYOffset;
        const distance = targetY - startY;
        let startTime = null;

        // ✨ Extra-smooth cinematic easing
        const easeInOutCubic = (t) =>
            t < 0.5
                ? 4 * t * t * t
                : 1 - Math.pow(-2 * t + 2, 3) / 2;

        const animate = (currentTime) => {
            if (!startTime) startTime = currentTime;
            const elapsed = currentTime - startTime;
            const progress = Math.min(elapsed / duration, 1);
            const eased = easeInOutCubic(progress);

            window.scrollTo(0, startY + distance * eased);

            if (progress < 1) {
                requestAnimationFrame(animate);
            } else {
                isScrolling = false;
            }
        };

        requestAnimationFrame(animate);
    };

    // 🌊 Slow cinematic scroll
    cinematicScrollToCenter(output);

    try {
        const response = await fetch("https://explainit-2.onrender.com//explain", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                text,
                age: selectedAge
            })
        });

        if (!response.ok) throw new Error("Server error");

        const data = await response.json();
        output.innerText = data.result;

        // 🔁 Re-center again slowly after content expands
        setTimeout(() => {
            cinematicScrollToCenter(output, 1800);
        }, 300);

    } catch (error) {
        console.error(error);
        output.innerText = "❌ Something went wrong. Please try again.";

        setTimeout(() => {
            cinematicScrollToCenter(output, 1800);
        }, 300);
    }
}
