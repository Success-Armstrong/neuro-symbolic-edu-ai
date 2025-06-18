document.getElementById("aiForm").addEventListener("submit", async function (e) {
  e.preventDefault();

  const data = {
    name: document.getElementById("name").value,
    html: parseInt(document.getElementById("html").value),
    css: parseInt(document.getElementById("css").value),
    js: parseInt(document.getElementById("js").value),
    confidence: document.getElementById("confidence").value
  };

  try {
    const response = await fetch("http://127.0.0.1:8000/predict", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(data)
    });

    const result = await response.json();

    document.getElementById("result").innerHTML = `
      <h3>Hello, ${result.name}!</h3>
      <p><strong>Weak Area:</strong> ${result.weak_area}</p>
      <p><strong>Advice:</strong> ${result.advice}</p>
    `;
  } catch (error) {
    document.getElementById("result").innerHTML = `
      <p style="color:red;">Error contacting the server. Is FastAPI running?</p>
    `;
    console.error("Error:", error);
  }
});
