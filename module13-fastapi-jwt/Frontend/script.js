const API = "http://127.0.0.1:8000";


// 🔐 REGISTER
async function register() {
  const email = document.getElementById("email").value;
  const password = document.getElementById("password").value;

  try {
    const res = await fetch(API + "/users/register", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ email, password })
    });

    const data = await res.json();

    if (res.ok) {
      document.getElementById("msg").innerText = "Registered successfully";
    } else {
      document.getElementById("msg").innerText = "error";
    }

  } catch (err) {
    console.error(err);
    document.getElementById("msg").innerText = "error";
  }
}


// 🔐 LOGIN (CRITICAL FIX)
async function login() {
  const email = document.getElementById("email").value;
  const password = document.getElementById("password").value;

  const formData = new URLSearchParams();
  formData.append("username", email);
  formData.append("password", password);

  try {
    const res = await fetch(API + "/users/login", {
      method: "POST",
      headers: {
        "Content-Type": "application/x-www-form-urlencoded"
      },
      body: formData
    });

    const data = await res.json();

    if (res.ok) {
      localStorage.setItem("token", data.access_token);   // 🔥 important
      document.getElementById("msg").innerText = "Login successful";
    } else {
      document.getElementById("msg").innerText = "error";
    }

  } catch (err) {
    console.error(err);
    document.getElementById("msg").innerText = "error";
  }
}


// ➕ ADD CALCULATION
async function addCalc() {
  let token = localStorage.getItem("token");

  try {
    let res = await fetch(API + "/calculations", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + token
      },
      body: JSON.stringify({
        operand1: Number(document.getElementById("op1").value),
        operand2: Number(document.getElementById("op2").value),
        operation: document.getElementById("operation").value
      })
    });

    let data = await res.json();

    if (data.result !== undefined) {
      document.getElementById("results").innerText =
        `${data.operand1} ${data.operation} ${data.operand2} = ${data.result}`;
    } else {
      document.getElementById("results").innerText = "error";
    }

  } catch (error) {
    console.error(error);
    document.getElementById("results").innerText = "error";
  }
}


// 📥 LOAD CALCULATIONS (BROWSE)
async function loadCalcs() {
  let token = localStorage.getItem("token");

  try {
    let res = await fetch(API + "/calculations", {
      method: "GET",
      headers: {
        "Authorization": "Bearer " + token
      }
    });

    let data = await res.json();

    if (Array.isArray(data)) {
      document.getElementById("results").innerText =
        data.map(c => `${c.operand1} ${c.operation} ${c.operand2} = ${c.result}`).join("\n");
    } else {
      document.getElementById("results").innerText = "error";
    }

  } catch (error) {
    console.error(error);
    document.getElementById("results").innerText = "error";
  }
}


// ❌ DELETE CALCULATION
async function deleteCalc(id) {
  let token = localStorage.getItem("token");

  try {
    await fetch(API + "/calculations/" + id, {
      method: "DELETE",
      headers: {
        "Authorization": "Bearer " + token
      }
    });

    loadCalcs();

  } catch (error) {
    console.error(error);
  }
}