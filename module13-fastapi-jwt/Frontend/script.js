const API = "http://localhost:8000";

// ➕ Add Calculation
async function addCalc() {
  let token = document.getElementById("token").value;

  try {
    let res = await fetch(API + "/calculations", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "Authorization": token
      },
      body: JSON.stringify({
        operand1: Number(document.getElementById("op1").value),
        operand2: Number(document.getElementById("op2").value),
        operation: document.getElementById("operation").value
      })
    });

    let data = await res.json();

    console.log("ADD RESPONSE:", data);

    if (data.result !== undefined) {
      document.getElementById("results").innerText =
        `${data.operand1} ${data.operation} ${data.operand2} = ${data.result}`;
    } else {
      document.getElementById("results").innerText =
        "Error: " + JSON.stringify(data);
    }

  } catch (error) {
    console.error("Error:", error);
    document.getElementById("results").innerText = "Request failed";
  }
}


// 📥 Load all calculations
async function loadCalcs() {
  let token = document.getElementById("token").value;

  try {
    let res = await fetch(API + "/calculations", {
      method: "GET",
      headers: {
        "Authorization": token
      }
    });

    let data = await res.json();

    console.log("LOAD RESPONSE:", data);

    if (Array.isArray(data)) {
      document.getElementById("results").innerText =
        data.map(c => `${c.operand1} ${c.operation} ${c.operand2} = ${c.result}`).join("\n");
    } else {
      document.getElementById("results").innerText =
        "Error: " + JSON.stringify(data);
    }

  } catch (error) {
    console.error("Error:", error);
    document.getElementById("results").innerText = "Request failed";
  }
}


// ❌ Delete calculation
async function deleteCalc(id) {
  let token = document.getElementById("token").value;

  try {
    await fetch(API + "/calculations/" + id, {
      method: "DELETE",
      headers: {
        "Authorization": token
      }
    });

    loadCalcs();

  } catch (error) {
    console.error("Delete error:", error);
  }
}